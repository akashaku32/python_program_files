lst=[1,2,3,3,5,1]
dict={}
for i in lst:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)