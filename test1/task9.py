class Version:
    def __init(self,*args):
        pass
    @property
    def major(self):
        return self._major
    @property
    def minor(self):
        return self._minor
    @property
    def patch(self):
        return self._patch
    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"
    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"
    def __eq__(self,other):
        if isinstance(other,str):
            if "Version" in other:
                return True
            else: 
                lst = other.split('.')
                #think
        if isinstance(other,Version):
            return self.major == other.major and self.minor == other.minor and self.patch == other.patch
        return False
    def __ne__(self,other):
        return not self == other
    def __lt__(self,other):
        pass
    def __gt__(self,other):
        pass
# Tests:

assert Version(1, 2, 3).major == 1
assert Version(1, 2, 3).minor == 2
assert Version(1, 2, 3).patch == 3
assert Version("1.2.3").major == 1
assert Version("1.2.3").minor == 2
assert Version("1.2.3").patch == 3
assert Version("10.2.304").major == 10
assert Version("10.2.304").minor == 2
assert Version("10.2.304").patch == 304
assert str(Version(1, 2, 3)) == "1.2.3"
assert repr(Version(1, 2, 3)) == "Version(1, 2, 3)"
assert Version(1, 2, 3) == Version(1, 2, 3)
assert Version(1, 2, 3) == "1.2.3"
assert Version(1, 2, 3) != Version(1, 2, 4)
assert Version(1, 2, 3) != "1.2.4"
assert Version(1, 2, 3) < Version(2, 0, 0)
assert Version(1, 2, 3) < "2.0.0"
assert Version(1, 2, 3) < Version(1, 3, 0)
assert Version(1, 2, 3) < "1.3.0"
assert Version(1, 2, 3) < Version(1, 2, 4)
assert Version(1, 2, 3) < "1.2.4"
assert Version("1.2.3") < Version("1.12.0")
assert Version("1.2.3") < "1.12.0"
assert Version(1, 2, 3) > Version(0, 9, 0)
assert Version(1, 2, 3) > "0.9.0"
assert Version(1, 2, 3) > Version(1, 1, 0)
assert Version(1, 2, 3) > "1.1.0"
assert Version(1, 2, 3) > Version(1, 2, 2)
assert Version(1, 2, 3) > "1.2.2"
assert Version("1.1.13") > Version("1.1.3")
assert Version("1.1.13") > "1.1.3"