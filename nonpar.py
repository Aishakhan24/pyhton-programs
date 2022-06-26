class demo:
    def __int__(self,age,country):
        self.age=age
        self.place=country
    def hello(self):
        print(f"Hello,I am a{self.age}yo from {self.place}")
d=demo(24,"Russia")
d.hello()