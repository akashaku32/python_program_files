class books:
    name:str
    author:str
    price:int
    pages:int
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.author=kwargs.get("author")
        self.price=kwargs.get("price")
        self.pages=kwargs.get("pages")
    def get(self):
        print(self.name,self.author,self.price,self.pages)
    def __str__(self):
        return self.name
    

obj=books(name="inferno",author="deschamps",price=500,pages=1000)
print(obj)
obj.get()