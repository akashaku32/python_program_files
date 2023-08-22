from db_connect import *
db="animal"
db=db_connect(db)
cursor=db.cursor()
query="""insert into pets(age,gender,breed,location,price) values(2,'female','breed4','palakkad',4500)"""
cursor.execute(query)
db.commit()