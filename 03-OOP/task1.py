from math import log2
from random import seed, randint
from enum import Enum

# HOW TF DO I USE THIS ---??????
class Food(Enum):
    BERRY = 1
    COW = 2
    BANANA=3

class Player:
    def __init__(self, name,hp=10,xp=0):
        self.__name = name
        self.__hp = hp  if hp >= 0 else 0 
        self.__xp = xp
        self.__level = 1 if self.__xp < 300 else 2+int(log2(int(xp/300)))
    @property
    def name(self):
        return self.__name
    @property
    def xp(self):
        return self.__xp
    @property 
    def hp(self):
        return self.__hp
    @property
    def level(self):
        return self.__level
    def __repr__(self):
        return f"{self.name} , hp:{self.hp} , xp:{self.xp} , level: {self.level}"
    def __str__(self):
        return f"{self.name} , hp:{self.hp} , xp:{self.xp} , level: {self.level}"



    def change_level(self):
     if self.xp < 300: self.__level = 1 
     else:  self.__level = 2+int(log2(int(self.xp/300)))
    def increase_xp(self,value):
        self.__xp += value
        self.change_level()
    def increase_hp(self,value):
        self.__hp += value
    
    
    # fix death 
    def decrease_hp(self,value):
        if self.hp - value <= 0:
            print(f"Player {self.name} died")
            return
        else:
            self.__hp -= value
    def fight(self,other):
        seed(3)
        winPl1=0
        print("--------------------------------")
        print("Numbers ")
        for round in range(3):
            value = randint(0,10)
            print(f"Numbers {value}")
            if value % 2 == 0 : winPl1 += 1 
            else : winPl1 -=1

        if winPl1 > 0:
            self.increase_xp(int(other.xp * 0.3))
            other.decrease_hp(3)
        else :
            other.increase_xp(int(self.xp * 0.3))
            self.decrease_hp(3)

    def feed(self,value):
        match value:
            case "BERRY" : self.increase_hp(3)
            case "BEEF" : self.increase_hp(4)
            case "BANANA" : self.increase_hp(5)




p1=Player("Cecka",10,300)
p2=Player("Stoyan",4,1000)
p3=Player("Kaloyan",-5,1100)

print(p1)
print(p2)
print(p3)

p1.fight(p2)
print(p1)
print(p2)
print(p3)
p2.fight(p3)
p3.fight(p1)