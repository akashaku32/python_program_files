from abc import ABC,abstractmethod
class ide:
    @abstractmethod
    def debug(self):
        pass
class pycharm(ide):
    def debug(self):
        print("pycharm ide")
class eclipse(ide):
    def debug(self):
        print("eclipse ide")
obj=pycharm()
obj.debug()
