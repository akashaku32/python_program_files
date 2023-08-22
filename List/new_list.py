lst=[10,15,20,25,30]
new=[]
for i in lst:
    if(i%2!=0):
        if(i%5==0):
            new.append(i)
print(new)
