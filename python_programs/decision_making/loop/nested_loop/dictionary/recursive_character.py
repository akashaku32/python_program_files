text="AABBCCCDE"
dic={}
for i in text:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
print(max(dic,key=lambda l:dic.get(l)))
# ma=max(dic.values())
# for k,v in dic.items():
#     if ma==v:
#         print(k,v)



