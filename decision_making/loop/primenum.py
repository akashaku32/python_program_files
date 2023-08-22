num=2
f=0
for i in range(2,num):
    if(num%i==0):
        f=1
        break
if(f==0):
    print(f"prime is {num}")
else:
    print(num,"not prime")
        
