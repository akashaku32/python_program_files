from json import load

with open("C:\\Users\\idk18\\OneDrive\\Desktop\\python_programs\\jsonprocess\\data.json","r") as f:
    data=load(f)

names=[u.get("name") for u in data]    
# print(names)

#student with highest mark
candidate=max(data,key=lambda s:s.get("total"))
# print(candidate)

#sort all students with respect to order by desc
out=sorted(data,reverse=True,key=lambda s:s.get("total"))
# print(out)                                                                                                     

#print all bca students
bca_s=[u.get("name") for u in data if u.get("course")=="bca"]
print(bca_s)