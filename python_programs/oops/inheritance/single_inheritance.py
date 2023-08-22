class parent:
    def mobile(self):
        print("samsung")
    def bike(self):
        print("cb3")
    def car(self):
        print("lambo")

class child(parent):
    pass

obj=child()
obj.mobile()
obj.car()
obj.bike()
