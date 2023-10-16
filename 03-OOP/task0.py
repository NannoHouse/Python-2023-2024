from math import sqrt, sin, cos, atan  # you will need these
from math import pi, isclose
class PolarCoordinate:
    def __init__(self,r,fi):
        self.r = r
        self.fi = fi
    def get_r(self):
        return self.r
    def get_fi(self):
        return self.fi
    def to_cartesian(self):
        x=self.get_r() * cos(self.get_fi())
        y=self.get_r() * sin(self.get_fi())
        return (x,y)
    @classmethod
    def from_cartesian(cls,x,y):
        r=sqrt(x**2 + y**2)
        fi = atan(y/x)
        return cls(r,fi)
    
    def __repr__(self):
        return f"PolarCoordinate({self.get_r()}, {self.get_fi()})"

    def __str__(self):
        return f"(r: {self.get_r()}, angle: {self.get_fi()})"
    # define hash
    def __hash__(self):
        return hash((self.get_r(), self.get_fi()))

    #define == and !=
    def __eq__(self,other):
        return self.r == other.r and self.fi == other.fi
    def __neq__(self,other):
        return self.r != other.r or self.fi != other.fi


p1 = PolarCoordinate(1, pi/6)

print(p1.r == 1)
print(p1.fi == pi/6)
p2 = PolarCoordinate.from_cartesian(3, 4)
print(isclose(p2.r, 5))

# false - 
print(isclose(p2.fi, atan(4/3)))
x, y = p2.to_cartesian()
print(isclose(x, 3))
print(isclose(y, 4))


p3 = PolarCoordinate(1, 0)
print(str(p3) == "(r: 1, angle: 0)")
print(repr(p3) == "PolarCoordinate(1, 0)")

pp1, pp2, pp3 = PolarCoordinate(1, pi/6), PolarCoordinate.from_cartesian(3, 4), PolarCoordinate(1, 0)
print(p1 == pp1)
print(p2 == pp2)
print(p3 == pp3)

d = {p1: "A", p2: "B", p3: "C"}
print(d[pp1] == "A")
print(d[pp2] == "B")
print(d[pp3] == "C")

s = {p1, p2, p3, pp1, pp2, pp3, p1, p2, p3}
print(len(s) == 3)
