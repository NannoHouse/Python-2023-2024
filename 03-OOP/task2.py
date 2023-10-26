from math import sqrt
class Vector3:
    def __init__(self, x,y,z):
        self._x = x
        self._y=y
        self._z = z
    def __repr__(self):
        return f"({self._x}, {self._y}, {self._z}"
    def __str__(self):
        return f"({self._x}, {self._y}, {self._z}"
    def __add__(self,other):
        if isinstance(other,Vector3): 
            return Vector3(self._x + other._x, self._y + other._y, self._z + other._z)
        else :
             return Vector3(self._x + other, self._y + other, self._z + other)
    def __radd__(self,other):
         return other + self
    def __iadd__(self,other):
         self._x += other._x
         self._y += other._y
         self._z += other._z
         return self 
    def __mull__(self,other):
        if isinstance(other,Vector3): 
            return Vector3(self._x * other._x, self._y * other._y, self._z * other._z)
        else :
             return Vector3(self._x * other, self._y * other, self._z * other)
    def __rmul__(self,other):
        return Vector3(self._x * other, self._y * other, self._z * other)
    def __imul__(self,other):
        self._x += other._x
        self._z += other._z
        self._y += other._y
        return self
    def __eq__(self,other):
        return self._x == other._x and self._y == other._y and self._z == other._z
    def __ne__(self,other):
        return not self == other
    def __abs__(self):
        return  sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2)
    def __getattr__(self,name):
        match name:
            case 'X': return self._x
            case 'Y ': return self._y
            case 'Z' : return self._z
    def __setattr__(self,name, value):
        pass
    def __iter__(self):
        return iter(self._x, self._y, self._z)