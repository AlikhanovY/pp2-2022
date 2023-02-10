class Shape():
    def __init__(self, length):
        self.length=length
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def area(self):
        print(self.length ** 2 )
p1=Shape(0)
p2=Square(9)
p1.area()
p2.area()
        