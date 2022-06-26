class parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class child(parent):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
a=child("Rim",5)
a.display()