num1=12
num2=24
max=0
for i in range(1,num1+1):
    if(num1%i==0 and num2%i==0):
        if(max<i):
            max=i
lcm=(num1*num2)//max
print(lcm)