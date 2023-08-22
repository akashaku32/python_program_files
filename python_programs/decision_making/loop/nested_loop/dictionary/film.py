movies={"2018":5,"kerala story":3,"neymar":4,"kgf":5,"arm":4}
print(movies.keys())
print(max(movies,key=lambda l:movies.get(l)))
print(sorted(movies,key=lambda l:movies.get(l),reverse=True)) 
k=movies.items()
print(k)