class parent:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
class child(parent):
    def __init__(self,name,age):
        parent.__init__(self,name)
        self.age=age
    def getage(self):
        return self.age
class grandchild(child):
    def __init__(self,name,age,location):
        child.__init__(self,name,age)
        self.location=location
    def getlocation(self):
        return self.location
gc=grandchild("Doremon",15,"Japan")
print(gc.getName(), gc.getage(),gc.getlocation())