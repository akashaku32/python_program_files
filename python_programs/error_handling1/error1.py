num1=int(input("num1:"))
num2=int(input("num2:"))
try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)

print("db commit1")
print("db commit2")
