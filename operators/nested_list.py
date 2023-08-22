lst=[[1,2],[5,50],[50,45]]
num=[j+1 or j-1  for i in lst for j in i if j>5 or j<5 ]
print(num)