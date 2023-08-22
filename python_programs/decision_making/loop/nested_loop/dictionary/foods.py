items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
    
]

# items_name=list(map(lambda n:n.get("name"),items))
# print(items_name)
# lst_names=[i.get("name") for i in items]
# print(lst_names)
# items_price=list(map(lambda n:n.get("price"),items))
# print(items_price)
# price=[i.get("price") for i in items]
# print(price)
# items_categ=list(filter(lambda n:n.get("category")=="veg",items))
# print(items_categ)
categ=[i for i in items if i.get("category")=="veg"]
print(categ)



