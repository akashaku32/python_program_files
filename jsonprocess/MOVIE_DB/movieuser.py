from json import load

with open("C:\\Users\\idk18\\OneDrive\\Desktop\\python_programs\\jsonprocess\\MOVIE_DB\\mdb.json","r",encoding="UTF-8") as f:
    data=load(f)

#total number of movies    
print(len(data))

#print all movie names
m_title=[m.get("title") for m in data] 
# print(m_title)

#print movie with highest run time

movie=max(data,key=lambda m:int(m.get("runtime")))
# print(movie.get("title"))

#print all genres
# genres=[i.get("genres") for i in data]
# print(genres)
#print movie name with genres comedy
# movie_name=[i.get("title") for i in data if "Comedy" in i.get("genres")]
# print(movie_name)
#print movie name which contain geners comedy or fantasy
movie_name_2=[i.get("title") for i in data for g in i.get("genres") if g in ["Comedy","Fantasy"]]
print(movie_name_2)
#yearwise movie count  o/p={1988:4,1998:2}
dic={}
for i in data:
    if i.get("year") in dic:
        dic[i.get("year")]+=1
    else:
        dic[i.get("year")]=1
print(dic)
ma=max(dic,key=lambda l:dic.get(l))
print(ma)