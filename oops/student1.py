class students:
    rollno:int
    name:str
    course:str

    def __init__(self,**kwargs):
        self.rollno=kwargs.get("rollno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")
    def get(self):
        print(self.rollno,self.name,self.course)
    def __str__(self):
        return self.name
ob1=students(rollno=1,name="snehith",course="python")
ob1.get()
print(ob1)