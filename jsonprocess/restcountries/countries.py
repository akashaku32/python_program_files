from json import load
with open("C:\\Users\idk18\\OneDrive\\Desktop\python_programs\\jsonprocess\\restcountries\\rest.json","r",encoding="UTF-8") as f:
    data=load(f)
print("no of countries is:",len(data))
# country=input("enter the name of the country")
# for i in data:
#     if i.get("name")==country:
#print name of all countries
# all_country=[i.get("country") for i in data]
# print the region name and the list of countries of the region 
# all_regions={i.get("region") for i in data}
# print all countries of region asia
# asian_country=[i.get("name") for i in data if i.get("region")=="Asia"]
# print(asian_country)    
# print all region and no of countries in it
# dic={}
# for i in data:
#     if i.get("region") in dic:
#         dic[i.get("region")].append(i.get("name"))
#     else:
#         dic[i.get("region")]=[]
#         dic[i.get("region")].append(i.get("name"))
# print(dic)
# print india borders
indian_borders=[i.get("borders") for i in data if i.get("name")=="India"]
border=[i.get("name") for i in data if i.get("alpha3Code") in indian_borders[0]]
# print(border)


ma=max(data,key=lambda l:l.get("population"))
print(ma.get("name"))
