# limit=25
# start=1
# even_sum=0
# odd_sum=0
# while(start<=limit):
#     if(start%2==0):
#         even_sum+=start
#     else:
#         odd_sum+=start
#     start+=1
# print(even_sum)
# print(odd_sum)
#using for loop

limit=25
start=1
even_sum=0
odd_sum=0
for i in range(start,limit+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum)
print(odd_sum)