import math
class PolarCoordinate:
    def __init__(self,r,fi):
        self.__r = r
        self.__fi = fi
    def get_r(self):
        return self.__r
    def get_fi(self):
        return self.__fi
    def to_cartesian(self):
        x=self.get_fi * math.cos(self.get_fi)
        y=self.get_r * math.sin(self.get_fi)
        return (x,y)
    @classmethod
    def to_cartesian(self,x,y):
        r=math.sqrt(x**2 + y**2)
        fi = math.atan(x/y)
        return PolarCoordinate(r,fi)
    
    def __repr__(self):
        return f"PolarCoord: {self.__r} {self.__fi}"

    def __str__(self):
        return f"(r: {self.__r}, angle: {self.__fi})"
    # define hash
    def __hash__(self):
        return hash((self.__r, self.__fi))

    #define == and !=
    def __eq__(self,other):
        return self.__r == other.__r and self.__fi == other.__fi
    def __neq__(self,other):
        return self.__r != other.__r or self.__fi != other.__fi



