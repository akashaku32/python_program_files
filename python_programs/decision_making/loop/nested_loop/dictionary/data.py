data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }
d={}
for k,v in data.items():
    if v in d:
        d[v].append(k)
    else:
        d[v]=[k]
    
print(d)

        