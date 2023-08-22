lst=[2,3,4,5]
sum=8
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if(lst[i]+lst[j]==sum and i!=j):
#             print(lst[i],end=" ")
low=0
upp=len(lst)-1
while(low<upp):
    curr_sum=lst[low]+lst[upp]
    if(curr_sum==sum):
        print("pairs:",lst[low],lst[upp])
        break
    elif(curr_sum<sum):
        low+=1
    elif(curr_sum>sum):
        upp-=1
            