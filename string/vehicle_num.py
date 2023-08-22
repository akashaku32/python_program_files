from re import *
# rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
# num="KL-09-bn-6789"
# matcher=fullmatch(rule,num)
# if matcher!=None:
#     print("valid")
# else:
#     print("not valid")
rule="[A-Z][A-Z][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
num="KL-09-bn-6789"
matcher=fullmatch(rule,num)
if matcher!=None:
    print("valid")
else:
    print("not valid")