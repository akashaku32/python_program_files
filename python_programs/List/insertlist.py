# lst=[1,2,3,4,5]
# lst.insert(0,0)
# print(lst)
lst=[]

# num=int(input("enter the limit:"))
# for i in range(num):
#     val=int(input(f"enter the {i+1}th element:"))
#     lst.append(val)
# ma=max(lst)+10
# lst.insert(2,ma)
# print(lst)
num=int(input("enter the limit:"))
for i in range(num):
    
    val=int(input(f"enter the {i+1}th element:"))
    lst.append(val)
    ma=lst[0]
    if(ma<lst[i]):
        ma=lst[i]
ma+=10
lst.insert(2,ma)
print(lst)