from re import *
f=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\email\data.txt","r")
rule="[a-zA-Z0-9][a-zA-Z0-9$#_]*[@]gmail[.]com"
valid_email=set()
for i in f:
    i=i.rstrip("\n")
    k=fullmatch(rule,i)
    if(k!=None):
        valid_email.add(i)
print(valid_email)



