import datetime
class operations:
    num1:int
    num2:int
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def mul(self):
        return self.num1*self.num2
    @staticmethod
    def get_date():
        return datetime.date.today()
obj1=operations(20,30)
#instance method
print(obj1.add())
print(obj1.mul())
#static method
print(operations.get_date())
    