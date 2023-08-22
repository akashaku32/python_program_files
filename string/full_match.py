from re import *
rule="[k-m][369][a-zA-Z0-9]*"
value="hello"
matching=fullmatch(rule,value)
if(matching!=None):
    print("valid")
else:
    print("not valid")
