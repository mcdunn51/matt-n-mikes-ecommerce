# import sqlite3, csv

# def create_connection(db_file):
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
 
#     return None

# conn = create_connection('db.sqlite3')
# cur = conn.cursor()

# with open ('data.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         # print(row[0], row[1], row[2], row[3], row[4])
#         sql = "insert into api_product (itemno, description, description2, price, colour, manufacturerCode) values ('%s', '%s', '%s', %s, '%s', '%s')" % (row[0], row[1], row[1], row[2], row[3], row[4])
#         print(sql)
#         cur.execute(sql)
#         conn.commit()

import mysql.connector, csv

def create_mysql_connection():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0000",
    database='django-test',
    auth_plugin='caching_sha2_password'
    )
    return conn

conn = create_mysql_connection()
cur = conn.cursor()

with open (r'C:\Users\michael.mountford\OneDrive\Programming\matt-mikes-practice\backEnd\src\unused\data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row[0], row[1], row[2], row[3], row[4])
        sql = "insert into api_product (itemno, description, description2, price, colour, manufacturerCode) values ('%s', '%s', '%s', %s, '%s', '%s')" % (row[0], row[1], row[1], row[2], row[3], row[4])
        print(sql)
        cur.execute(sql)
        conn.commit()