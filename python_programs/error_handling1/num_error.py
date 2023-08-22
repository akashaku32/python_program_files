num=input("enter the num")
try:
    num=int(num)
    print(num**3)
except Exception as e:
    raise Exception("operand must be integer")

if num.isdigit():
