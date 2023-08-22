from mysql.connector import *
def db_connect(db):
    
    db=connect(
        host="localhost",
        user="root",
        password="Password@123",
    
        database=db)
    return db