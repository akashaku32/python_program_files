from db_connect import*
db="animal"
db=db_connect(db)
cursor=db.cursor()
query="select * from pets"
cursor.execute(query)
records=cursor.fetchall()
for i in records:
    print(i)
db.close()