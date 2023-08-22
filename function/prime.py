def prime(num1):
    f=0
    for i in range(2,num1):
        if(num1%i == 0):
            f=1
            break
    return f
num1=int(input("number:"))
p=prime(num1)
if(p==1):
    print("not prime")
else:
    print("prime")

        