mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],  
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]
# for i in mobiles:
#     if(i[3]=="4g"):
#         print(i[1])
# mob=[i[1] for i in mobiles if i[3]=="4g"]
# print(mob)
# mob=[i[1] for i in mobiles if i[2]<30000]
# print(mob)
# mob=[i[1] for i in mobiles if i[2]>30000 and i[2]<50000]
# print(mob)
mob=[i[1] for i in mobiles if i[2]<25000 and i[3]=="5g"]
print(mob)
 