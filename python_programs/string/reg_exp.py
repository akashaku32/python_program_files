sen="joel is a good student in may batch"
sen2="joel is a good student in may batch  "
# # bol=sen.startswith("joel")
# # if bol==True:
# #     print("string starts with joel")

# words=sen.split()
# if words[0]=="joel":
#     print("string starts with joel")
import re
x=re.search("^joel.*batch$",sen)
y=re.search("^joel.*batch$",sen2)


print(x)
print(y)
