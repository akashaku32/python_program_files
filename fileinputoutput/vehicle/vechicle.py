from re import *
f=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\vehicle\data.txt","r")
kerala=set()
tamil=set()
kerala_rule="[k][l][-][0-9]{1,2}[-][a-zA-Z]{1,2}[-][0-9]{1,4}"
tamil_rule="[t][n][-][0-9]{1,2}[-][a-zA-Z]{1,2}[-][0-9]{1,4}"
for i in f:
    i=i.strip("\n")
    kerala_match=fullmatch(kerala_rule,i)
    if(kerala_match!=None):
        kerala.add(i)
    tamil_match=fullmatch(tamil_rule,i)
    if(tamil_match!=None):
        tamil.add(i)
print(kerala)
print(tamil)
