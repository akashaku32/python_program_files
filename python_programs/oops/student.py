class student:
    rollno:int
    name:str
    course:str

    def __init__(self,rolno,name,course):
        self.rollno=rolno
        self.name=name
        self.course=course
    def show_data(self):
        print(self.rollno,self.name,self.course)
#reference name=class name()
obj1=student(1,"snehith","python")
obj2=student(2,"arun",".net")
obj1.show_data()
obj2.show_data()

#to initialise instance varibale we use constructor
#constructor name is __init__