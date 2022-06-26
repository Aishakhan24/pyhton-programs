class sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print(self.name,self.age)
class child1(sample):
    def __init__(self,marks,roll):
        self.marks=marks
        self.roll=roll
    def printname1(self):
        print(self.marks,self.roll)
a=child1(55,1)
a1=sample("Aisha",23)
a.printname()
a.printname1()




