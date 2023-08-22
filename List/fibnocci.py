# num=int(input("enter num:"))
# a=0
# b=1
# for i in range(num):
#     c=a+b
#     a=b
#     b=c
#     print(c)
l = [1, 2, 2, 1, 3, 4]
dup = {}

for i in l:
   if i in dup:
      dup[i]+=1
   else:
      dup[i]=1
print(dup)
