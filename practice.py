class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
emp1=Employee("Aisha",22)
emp2=Employee("Dora",23)
emp1.display()
emp2.display()
