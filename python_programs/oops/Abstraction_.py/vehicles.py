class parent:
    def vehicles(self):
        self.context=["passionpro","swift"]
        return self.context
class child(parent):
    def vehicles(self):
        super().vehicles()
        self.context.append("hunter")
        return self.context
obj1=child()
print(obj1.vehicles())