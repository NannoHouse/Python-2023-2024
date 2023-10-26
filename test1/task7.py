class Stack:
    def __init__(self,*args):
        self._size = len(args) 
        self._elements = list(args)
        self._top = None if self._size <= 0 else  self._elements[self._size - 1] 
    @property
    def top(self):
        print(self._elements)
        return  None if self._size <= 0 else  self._elements[self._size -1] 
    def push(self,elem):
        self._elements=self._elements.append(elem)
        self._size +=1
    def pop(self):
        self._size -=1
        self._elements.pop()
        print(f"{self._size}")
    def __len__(self):
        return self._size
    def __str__(self):
        return f"{self._elements}"
# Tests:


assert Stack().top is None
assert Stack("a").top == "a"
assert Stack(1, 2, 3, 4, 5).top == 5
assert Stack(*list(range(1000))).top == 999

# pop
s = Stack("a", "b", "c", "d")
s.pop()
print(s)
assert s.top == 'c'
s.pop()
print(s)

s.pop()
print(s)
assert s.top == "a"
s.pop()
assert s.top is None

# push
s.push("X")
assert s.top == "X"
s.push("X")
s.push("X")
assert s.top == "X"

# len
assert len(s) == 3
s.pop(); s.pop(); s.pop()
assert len(s) == 0