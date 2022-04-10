import pandas as pd
def getUserByPhone(conn, json):
    #print(json)
    #returns pd dataframe
    queryString = """
    Select
        `PHONE_NUMBER`
    from `tbl_user`
    where
        `PHONE_NUMBER` = '{phone_number}'
        and `password` = PASSWORD('{password}') ;
    """.format(phone_number=json['phone_number'], password=json['password'])
    #print(queryString)
    sql_query = pd.read_sql_query(queryString, conn)
    return sql_query

def getRolesByPhone( conn, json):
    queryString = """
    select
        `PHONE_NUMBER`,
        `ROLE`
    from `tbl_user_userroles`
    where `PHONE_NUMBER` = '{phone_number}'
    """.format( phone_number=json['phone_number'] )
    sql_query = pd.read_sql_query(queryString, conn)
    return sql_query

def getRolesByAllPhones( conn ):
    queryString = """
    select
        `PHONE_NUMBER`,
        `ROLE`
    from `tbl_user_userroles`
    """
    sql_query = pd.read_sql_query(queryString, conn)
    return sql_query

def getRoles( conn ):
    queryString = """
    select
        `ROLE`
    from `tbl_user_roles`
    """
    sql_query = pd.read_sql_query(queryString, conn)
    return sql_query


def getUsers(conn, json):
    queryString = """
    Select
        `PHONE_NUMBER`
    from `tbl_user`;
    """
    #print(queryString)
    sql_query = pd.read_sql_query(queryString, conn)
    return sql_query

def insertUser(cursor, conn, json):
    print('inside insert user', json)
    queryString = """
    insert into `TBL_USER`
    (`PHONE_NUMBER`, `PASSWORD`)
    values
    ('{phone_number}', PASSWORD('{password}'))
    """.format(phone_number=json['phone_number'], password=json['password'])
    cursor.execute(queryString)
    #insertId = cursor.fetchone()[0]
    print ( queryString)
    conn.commit()
    return {'id':json['phone_number'], 'message':'success'}

def insertRole(cursor, conn, json):
    queryString = """
    insert into `tbl_user_roles`
    (`ROLE`)
    values
    ('{new_role}')
    """.format(new_role=json['role_name'].upper())
    cursor.execute(queryString)
    #insertId = cursor.fetchone()[0]
    conn.commit()
    return {'id':json['role_name'].upper(), 'message':'success'}
