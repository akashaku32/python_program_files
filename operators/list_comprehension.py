# lst=[3,4,5,6,7]
# # odd=[i for i in lst if i%2!=0]
# # print(odd)
# # even=[i for i in lst if i%2==0]
# # print(even)
# # cubes=[i*i*i for i in lst]
# # print(cubes)
# num=[i for i in lst if i%3==0]
# print(num)
lst=[[1,2],[5,50],[50,45]]
num=[j+1 if j>5 else j-1 if j<5 else j for i in lst for j in i]

print(num)
