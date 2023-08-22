lst=[10,20,30,40]
loc=int(input("location:"))
try:
    print(lst[loc])
except Exception as e:
    loc=int(input("location"))
    print(lst[loc])
finally:
    print("db commit1")
    print("db commit2")