class bank:
    accno:int
    balance:int
    ac_type:str
    p_name:str
    def create_account(self,accno,balance,ac_type,p_name):
        self.accno=accno
        self.balance=balance
        self.ac_type=ac_type
        self.p_name=p_name
    def deposit(self,amount):
        self.balance+=amount
        print(f"your account {self.accno} is credited with {amount} and balance is {self.balance}")
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"your bank account:{self.accno} have been debited with amount:{amount} and balance is {self.balance}")
        else:
            print("transaction unsuccessful insufficient balance")
    def display(self):
        print(self.accno,self.balance,self.ac_type,self.p_name)
obj1=bank()
obj1.create_account(23424141,2000,"current","athithya")
obj1.deposit(20000)
obj1.withdraw(2000)
