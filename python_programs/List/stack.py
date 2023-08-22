lst=[]
limit=int(input("enter the limit:"))
for i in range(limit):
    val=int(input(f"enter the {i}th value:"))
    lst.append(val)
lim=int(input("enter the values to be popped:"))
for i in range(lim):
    lst.pop()
print(lst)