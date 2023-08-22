from re import *
# k=input("enter the num:")
# # i=re.search("^91",k)
# # if(i):
# #     print("indian num")
# # else:
# #     print("not indian")
rule="[+][9][1][0-9]{10}"

num="+917736970618"
# ind=search("[+][9][1][0-9]{1,10}",num)
matcher=fullmatch(rule,num)


if(matcher!=None):
    print("indian number")
else:
    print("not indian")

