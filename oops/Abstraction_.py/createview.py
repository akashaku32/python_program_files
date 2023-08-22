from abc import ABC,abstractmethod
class createview(ABC):
    model:str
    template:str
    form_class:str
    def __init__(self,model,template,form_class):
        self.model=model
        self.template=template
        self.form_class=form_class
    @abstractmethod
    def create(self):
        pass
class emoloyeecreate(createview):
    def __init__(self, model, template, form_class):
        super().__init__(model, template, form_class)
    def create(self):
        print(f"{self.model} of template {self.template} in {self.form_class}")
obj=emoloyeecreate("employee","employee.html","employee.form")
obj.create()
