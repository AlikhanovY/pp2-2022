class Shape():
    def __init__(self, length):
        self.length=length
    def area(self):
        print(0)
    
class Rectangle(Shape):
    def __init__(self,length, width):
        super().__init__(length)
        self.width=width
    def area(self):
        print(self.length * self.width)

p=Rectangle(1,2)
p.area()