class p1:
    def m1(self):
        print("p1 method")
class p2:
    def m1(self):
        print("p2 method")
class c1(p1,p2):
    pass
obj=c1()
obj.m1()