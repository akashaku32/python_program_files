from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        pass
class rectangle(shape):
    def draw(self):
        print("rectangle")
obj=rectangle()
obj.draw()