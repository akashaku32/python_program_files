lst=[1,3,5,7]
val=int(input("enter the key:"))
f=0

for i in lst:
    if(val==i):
        print("element found")
        f=1
        break
    

if(f==0):
    print("element not found")


