from db_connect import *

    
class mobiles:
    def connect(self):
        db=db_connect("mobilesdb")
        return db
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="select * from mobiles"
        cursor.execute(query)
        mobiles=cursor.fetchall()
        for i in mobiles:
             print(i)
        
    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="insert into mobiles(name,spec) values(%s,%s)"
        data=tuple(v for v in kwargs.values())
        cursor.execute(query,data)
        db.commit()
    def retrieve(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"select * from mobiles where id={id}"
        cursor.execute(query)
        mobile=cursor.fetchone()
        print(mobile)
    def update(self,id,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        data=list(v for v in kwargs.values())
        data.append(id)
        
        query="update mobiles set name=%s spec=%s where id=%d"
        
        
        cursor.execute(query,data)
        db.commit()
    def destroy(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"delete mobiles where id={id}"
        cursor.execute(query)
        db.commit()
        return "record deleted"


obj=mobiles()
# obj.destroy(7)
obj.update(6,name="pixel",spec="oled")
# obj.post(name='oneplus nord',spec='snapdragon888')
# obj.update(name='rog',id=6)