class mobile():
    name:str
    price:int
    display:str
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")
    def __str__(self):
        return self.name
    @property
    def get_price(self):
        return self.price
    
obj=mobile(name="oneplus",price=20000,display="oled")
print(obj)
print(obj.get_price)