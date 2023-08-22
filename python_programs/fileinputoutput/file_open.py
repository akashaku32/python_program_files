# k=open("C:\\Users\idk18\OneDrive\\Desktop\python_programs\\fileinputoutput\data.txt","r")
# words=[]
# for i in k:
#     l=i.rstrip("\n").split(" ")

    
#     for i in l:
#         words.append(i)
# print(set(words))
user_input=input("enter the user_input:")
fwrite=open("C:\\Users\idk18\OneDrive\\Desktop\python_programs\\fileinputoutput\data.txt","w")
fwrite.write(user_input)
fwrite.close()
fread=open("C:\\Users\idk18\OneDrive\\Desktop\python_programs\\fileinputoutput\data.txt","r")
words=[]
count_lines=1
count_space=0
count_alphabet=0
count_digit=0
count_special_char=0
for i in fread:
    if "\n" in i:
        count_lines+=1
    if " " in i:
        count_space+=1
    l=i.rstrip("\n").split(" ")
    for i in l:
        words.append(i)
for j in words:
        for g in j:
           if g.isalpha():
               count_alphabet+=1
           elif g.isdigit():
               count_digit+=1
           else:
               count_special_char+=1 
print("number of lines:",count_lines)
print("no of words:",len(words))
print("no of alphabets:",count_alphabet)
print("no of digits:",count_digit)
print("no of white space:",count_space)
print("no of special character:",count_special_char)
fread.close()



    
    
    

    

    

        
