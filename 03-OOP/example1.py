import math

class Rectangle:
    def __init__(self, x=0,y=0):
        self._x=x
        self._y=y
    def __getX__(self):
        return self._x
    def __getY__(self):
        return self._y
    def area(self):
        return self._x * self._y
    def __repr__(self):
        return f"({self._x}, {self._y})"

class Circle:
    def __init__(self,r=0,color="grey"):
        self._r = r
        self._color = color
    def __getRad__(self):
        return self._r
    def __getColor__(self):
        return self._color
    def __repr__(self):
        return f"({self._r}, {self._color})"
    def area(self):
        return math.pi * self._r**2


class Shapes(Rectangle, Circle):
    def __init__(self):
        self._collection=list()

    def addCircle(self,circle):
        self._collection.append(circle)
    
    def addRectangle(self, rectangle):
        self._collection.append(rectangle)
    def sumAllRect(self):
        sum=0
        for elem in self._collection:
            if type(elem) == Rectangle:
                sum += elem.area()
        return sum
    
    def sumAllCircle(self):
        sum=0
        for elem in self._collection:
            if type(elem) == Circle:
                sum += elem.area()
        return sum
    def __getElAt__(self,index):
        elem = self._collection[index]
        return None if elem is None else elem
    
c1 = Circle(3,"brown")
c2 = Circle(5,"baby")
c3 = Circle(10000,"queer")
c4 = Circle(3.2,"red bell")

r1 = Rectangle(12,15)
r2 = Rectangle(11,0)
r3 = Rectangle(7,3)
r4 = Rectangle(3,3)

pp = Shapes()
pp.addCircle(c1)
pp.addCircle(c4)
pp.addCircle(c3)
pp.addCircle(c2)

pp.addRectangle(r1)
pp.addRectangle(r2)
pp.addRectangle(r3)
pp.addRectangle(r4)


print(pp.sumAllCircle())
print(pp.sumAllRect())


leng = pp._collection.__len__()

for i in range(leng):
    print(pp.__getElAt__(i))

# add iterator