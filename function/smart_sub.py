def smart_sub(num1,num2):
    return num1-num2 if num1>num2 else num2-num1
num1=int(input("number 1:"))
num2=int(input("number 2:"))
print(smart_sub(num1,num2))