class employee:
    id=int
    name=str
    designation=str
    salary=int
    def set_emp(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.designation=desig
        self.salary=salary
    def display_emp(self):
        print(self.id,self.name,self.designation,self.salary)

emp1=employee()
emp1.set_emp(1,"nikhil","bpo",20000)
emp1.display_emp()