from email.utils import parsedate
from functools import wraps
import os
import json as JSON
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template, make_response
from flask_cors import CORS, cross_origin
import pandas as pd
from werkzeug.utils import secure_filename
import pypyodbc
from datetime import datetime
import controller_token as tokenController
import controller_user as userController
import common as COMMON
UPLOAD_FOLDER = 'C:/Users/abc/repo/smash_or_pass/pop_hy_py_fl/POP_HY_PY/uploadedFiles'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask (__name__ , template_folder='templates')
cors = CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 64 * 4096 * 4096
app.config['CORS_HEADERS'] = 'Content-Type'
CUSTOM_CONFIG = {
    'tokenKey' : 'x-access-token',
    'badRequestTuple' : ({'message':'bad request (input format)'}, 401),
    'badRequestMissingTokenTuple' : ({'message':'bad request (Missing Token)'}, 401),
    'badRequestInvalidTokenTuple' : ({'message':'bad request (Invalid Token)'}, 401),
    'internalServerError' : ({'message':'something went wrong'}, 500),
    'insufficientPrivilages' : ({'message':'insufficient Privilages'}, 401),
    'conflict':({'message':'conflict Already Exists'}, 409),
}
def AppCustomConfig(key : str):
    return CUSTOM_CONFIG[key]

def Authorized(fn):
    @wraps(fn)
    def wrap ( * args):
        #print('args', *args)
        #print(request)
        token = None
        tokenKey = AppCustomConfig('tokenKey')
        print('inside Authorised')
        if tokenKey in request.headers :
            token = request.headers[tokenKey]
            try :

                data = tokenController.decodeToken(token)
                print( data, tokenController.isTokenExpired(data) )
                if not tokenController.isTokenExpired(data) :
                    print(data, 'fn addr', fn)
                    return fn(data, *args)
                else :
                    return formResponse( *AppCustomConfig( 'badRequestInvalidTokenTuple' ) )
            except :
                return formResponse( *AppCustomConfig( 'badRequestInvalidTokenTuple' ) )
        else :
            return formResponse( *AppCustomConfig( 'badRequestMissingTokenTuple' ) )
    return wrap

@app.route('/')
def index():
    return f""" This is index of the app . """

@app.route('/api/login', methods=['POST'])
def userLogin():
    #getToken
    if(request.method =='POST'):
        json = request.json
        cursor, conn = COMMON.getConnection()
        query_data_frame = userController.getUserByPhone(conn, json)
        if(len(query_data_frame.index)>0):
            query_role_frame = userController.getRolesByPhone( conn, json )
            roles = query_role_frame['ROLE'].tolist()
            #print( query_role_frame )
            parsed = parseQueryData(query_data_frame)
            #print(parsed[0])
            jwt = tokenController.encode_auth_token( {
                'phone_number' : parsed[0]['PHONE_NUMBER'],
                'roles' : roles
                } ).decode('utf-8')
            parsed[0]["token"] = jwt
            #print( query_role_frame['ROLE'] )
            parsed[0]["roles"] = roles
            #print(parsed)
            return formResponse(parsed[0])
        else:
            return formResponse({'message':'no user found'}, 404)
    else:
        return formResponse( *AppCustomConfig( 'badRequestTuple' ) )

@app.route('/api/refreshToken', methods=['POST'])
@Authorized
def getRefreshToken(tokenData):
    #getToken
    if(request.method =='POST'):
        userData = tokenData['sub']
        jwt = tokenController.encode_auth_token( {
            'phone_number' : tokenData['sub']['phone_number'],
            'roles' : tokenData['sub']['roles']
            } ).decode('utf-8')
        userData["token"] = jwt
        userData['PHONE_NUMBER'] = tokenData['sub']['phone_number']
        return formResponse(userData)
    else:
        return formResponse( *AppCustomConfig( 'badRequestTuple' ) )


@app.route('/api/showusers', methods = ['POST'])
@Authorized
def showitems( tokenData ):
    print('tokenData', tokenData)
    roles = tokenData['sub']['roles']
    if(request.method =='POST' ):
        if ('ADMIN' in roles or 'UPDATE' in roles) :
            cursor, conn = COMMON.getConnection()
            df = userController.getRolesByAllPhones(conn)
            #df_json = df.groupby('PHONE_NUMBER').apply(lambda x: JSON.loads( x.to_json(orient='records') ))
            m = COMMON.mapByKeyData( parseQueryData( df ) , 'PHONE_NUMBER')
            return formResponse(
                {
                    'message':'success',
                    'data': m
                }, 200
            )
        else :
            return formResponse( *AppCustomConfig( 'insufficientPrivilages' ) )
    else:
        return formResponse( *AppCustomConfig( 'badRequestTuple' ) )

@app.route('/api/showroles', methods = ['POST'])
@Authorized
def showroles( tokenData ):
    print('tokenData', tokenData)
    if(request.method =='POST'):
        cursor, conn = COMMON.getConnection()
        df = userController.getRoles(conn)
        print('inside showroles')
        #df_json = df.groupby('PHONE_NUMBER').apply(lambda x: JSON.loads( x.to_json(orient='records') ))
        m = parseQueryData( df )
        return formResponse(
            {
                'message':'success',
                'data': m
            }, 200
        )
    else:
        print('showRoles')
        return formResponse( *AppCustomConfig( 'badRequestTuple' ) )

@app.route('/api/addusers' , methods = ['POST'])
@Authorized
def addusers( tokenData ):
    print('inside add users')
    print(request)
    if(request.method =='POST'):
        json = request.json
        cursor, conn = COMMON.getConnection()
        print('inside add users')
        print(json)
        try:
            query_data_frame = userController.insertUser(cursor, conn, json)
            code=400 if query_data_frame['id']=="NA" else 200
            #parsed = parseQueryData(query_data_frame)
            return  formResponse(query_data_frame, code)
        except:
            return formResponse( * AppCustomConfig('conflict'))
    else:
        return formResponse( *AppCustomConfig( 'badRequestTuple' ) )

@app.route('/api/addroles', methods = ['POST'])
@Authorized
def addrole( tokenData ):
    print('inside add users')
    print(request)
    if(request.method =='POST'):
        json = request.json
        cursor, conn = COMMON.getConnection()
        print('inside add users')
        print(json)
        try:
            query_data_frame = userController.insertRole(cursor, conn, json)
            code=400 if query_data_frame['id']=="NA" else 200
            #parsed = parseQueryData(query_data_frame)
            return  formResponse(query_data_frame, code)
        except:
            return formResponse( * AppCustomConfig('conflict'))
    else:
        return formResponse( *AppCustomConfig( 'badRequestTuple' ) )



def parseQueryData(query_data_frame):
    #print(query_data_frame)
    result = query_data_frame.to_json(orient="records")
    #print(result)
    parsed = JSON.loads(result)
    return parsed

def formResponse(data, statusCode=200):
	return app.response_class(
        response= JSON.dumps(data),
        status=statusCode,
        mimetype='application/json'
    )


if(__name__ == '__main__'):
  app.run(debug=True)