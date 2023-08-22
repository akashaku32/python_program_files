from re import *
# text="luminar technolab luminar technohub"
# k=finditer("luminar",text)
# count=0
# for i in k:
#     print(i.start())
#     print(i.group())
#     count+=1
# print(count)

text="aabdxyZER*"
# k=finditer("[a-zA-Z0-9]",text)
k=finditer("[a-zA-Z0-9]",text)
for i in k:
    print(i.group())


# [a-zA-Z] -> /w
# ^[A-Za-z] -> /W
# [0-9] -> /d
# ^[0-9] -> /D
