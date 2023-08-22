fwrite=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\numbers.txt","w")
fread=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\numbers.txt","r")
for i in fread:
    j=int(i.rstrip("/n"))
    if j%100==0 and j%400==0:
        fwrite.write(str(j)+"/n")
    elif j%100!=0 and j%4==0:
        fwrite.write(str(j)+"\n")
print("executed")

# f=open("C:\\Users\idk18\OneDrive\Desktop\python_programs\\fileinputoutput\\numbers.txt","w")
# for i in range(1890,3001):
#     f.write(str(i)+"\n")
# print("executed")