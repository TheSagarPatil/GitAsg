
import mysql.connector as sql

def getConnection():
    connection = sql.connect(host='localhost', database='app1', user='root')
    #print(connection)
    cursor = connection.cursor()
    return cursor, connection

def mapByKeyData(objArray, key):
    mapDict = dict()
    for obj in objArray :
        print(obj)
        dataAsKey = obj[key]
        print(dataAsKey)
        if dataAsKey in mapDict :
            print('inside t')
            mapDict [ dataAsKey ] .append( obj )
        else :
            print('inside f')
            mapDict [ dataAsKey ] = []
            mapDict [ dataAsKey ] .append( obj )
    return mapDict