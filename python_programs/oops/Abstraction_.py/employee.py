from abc import ABC,abstractmethod
class employee(ABC):
    name:str
    salary:int
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @abstractmethod
    def cal_salary(self):
        pass
class manager(employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def cal_salary(self):
        print("salary of employee is",self.salary+1000)
class developer(employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def cal_salary(self):
        print("salary of developer is",self.salary+800)
obj1=manager("ashik",20000)
obj1.cal_salary()
obj2=developer("shri",25000)
obj2.cal_salary()