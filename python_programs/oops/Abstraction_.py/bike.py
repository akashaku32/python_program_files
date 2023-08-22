from abc import ABC,abstractmethod
class bike(ABC):
    name:str
    model:int
    fuel:str
    
    def __init__(self,name,model,fuel):
        self.name=name
        self.model=model
        self.fuel=fuel
    @abstractmethod
    def start(self):
        pass
class hunter(bike):
    def __init__(self,name,model,fuel):
        super().__init__(name,model,fuel)
    def start(self):
        print(f"{self.name} model {self.model} fuel type{self.fuel}")
obj=hunter("hunter",2023,"petrol")
obj.start()