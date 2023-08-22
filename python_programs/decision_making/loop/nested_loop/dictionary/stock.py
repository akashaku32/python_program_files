items = [
    {"sugar": 45},
    {"tea_powder": 28},
    {"coffee": 67},
    {"dairymilk": 170},
    {"kitkat": 70},
    {"bourborn": 50},
    {"munch": 30},
    {"milk": 80},
    {"pepsi": 99},

]

offers=[
    {"sugar":10},
    {"coffee":20},
    {"milk":5},
    {"pepsi":10}
]
dic={}
i=0

for i in offers:
        for k in items:
            key=list(i.keys())[0]
            if key in dic:
                 pass
            else:
                   if key in k:
                     dic[key]=k.get(key)-i.get(key)
print(dic)
    

           
        
                



# while(i<len(items)):
#     for k,v in items[i].items():
#         j=0
#         if(j<len(offers)):
#             for m,n in offers[j].items():
                
#                 if k==m:

#                     dic[k]=v-n
#                     break

#                 else:
#                     dic[k]=v
#                 j+=1
#     i+=1
    
# print(dic)
