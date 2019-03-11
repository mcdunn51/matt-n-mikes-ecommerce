# import sqlite3, csv

import mysql.connector, csv, pypyodbc

def create_mssql_connection():
    connection = pypyodbc.connect(r'Driver={SQL Server};'
                                'Server=navsqlat\RKWL1;'
                                'Database=SVGL1;'
                                'uid=MICHAELM;pwd=michael91448')
    return connection

def create_mysql_connection():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0000",
    database='django-test',
    auth_plugin='caching_sha2_password'
    )
    return conn

mysql_conn = create_mysql_connection()
mysql_cur = mysql_conn.cursor()
mssql_conn = create_mssql_connection()
mssql_cur = mssql_conn.cursor()

sql = 'DELETE FROM `django-test`.`api_product`'
mysql_cur.execute(sql)
mysql_conn.commit()

sql = "SELECT No_, Description, [Description 2], [Unit Price], [Primary Colour], [Manufacturer Code] from SVG$Item WHERE [Manufacturer Code] in ('MORPHY', 'SWAN', 'SMEG') and [Unit Price] > 0"
res = mssql_cur.execute(sql)
for row in res:
    try:
        sql = "insert into api_product (itemno, description, description2, price, colour, manufacturerCode) values ('%s', '%s', '%s', %s, '%s', '%s')" % (row[0], row[1], row[2], row[3], row[4], row[5])
        print(sql)
        mysql_cur.execute(sql)
        mysql_conn.commit()
    except:
        print('fail')