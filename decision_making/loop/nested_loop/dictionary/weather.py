weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},

]
dic={}
for d in weather:
    for k,v in d.items():
        if k in dic:
            if(v>dic[k]):
               dic[k]=v 

        else:
            dic[k]=v
print(dic)

print(max(dic,key=lambda x:dic.get(x)))

