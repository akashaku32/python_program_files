k=int(input("num:"))
f=0
if k==1 or k==0:
    print("not prime")
else:
    for i in range(2,k):
        if(k%i==0):
            f=1
            break
    if(f==0):
        print(f"{k} is prime")
    else:
        print("not prime")


    
