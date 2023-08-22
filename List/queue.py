queue=[]
limit=int(input("enter the limit:"))
for i in range(limit):
    val=int(input(f"enter the {i}th element:"))
    queue.append(val)
print(queue)
lim=int(input("enter the no of elements to be popped:"))
for i in range(lim):
    queue.pop(0)
print(queue)
