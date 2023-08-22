def factorial(num1):
    fact=1
    for i in range(1,num1+1):
        fact*=i
    return fact
num1=int(input("number:"))
print(factorial(num1))