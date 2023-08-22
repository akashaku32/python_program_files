f=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\attendence\data.txt","r")
f1=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\attendence\present.txt","r")
all_stud=set()
pres_stud=set()
for i in f:
    i=i.rstrip("\n")
    all_stud.add(i)
for i in f1:
    i=i.rstrip("\n")
    pres_stud.add(i)
absent_stud=all_stud.difference(pres_stud)
print(absent_stud)

f.close()
dir(str)