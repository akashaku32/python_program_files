fread=open("C:\\Users\\idk18\\OneDrive\\Desktop\\python_programs\\fileinputoutput\\users\\data.txt","r")
users=[]
for i in fread:
    text=i.rstrip("\n")
    name,followers,following=text.split(",")
    dic={}
    dic["name"]=name
    dic["followers"]=int(followers)
    dic["following"]=int(following)
    users.append(dic)
max_followers=max(users,key=lambda l:l.get("followers"))
max_following=max(users,key=lambda l:l.get("following"))
print(max_followers)
print(max_following)
fwrite=open("C:\\Users\\idk18\\OneDrive\\Desktop\\python_programs\\fileinputoutput\\users\\data.txt","w")
for i in users:
    fwrite.write(str(i)+"\n")
    
   
        


