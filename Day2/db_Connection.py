import mysql.connector

def db_Connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@143",
        database="HDFCBank"
    )
print("db connected successfully.....")
