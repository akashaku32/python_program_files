names=["snehith","jishnu","jishnu","joe"]
val=input("enter the name to be searched:")
l=len(names)
f=0
for i in range(l):
    if(val==names[i]):
        
        names[i]="anamika"
        f=1
        
if(f==0):
    names.insert(1,"amal" )  
print(names)