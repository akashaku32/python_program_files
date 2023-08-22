from db_connect import *
d="animal"
db=db_connect(d)
cursor=db.cursor()
query="select * from pets where id=2"
cursor.execute(query)
record=cursor.fetchone()
print(record)