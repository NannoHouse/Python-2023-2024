# haha zadacha za skeleta

class Counter:
    def __init__(self):
        self._initial=0
        self.__steps__ = 1
    def increment(self):
        self._initial += self._steps
    def get_total(self):
        return self._initial
    def get_step(self):
        return self.__steps__

class TwowayCounter(Counter):
    def decrement(self):
        self._initial -= self.get_step()

class LimitedCOunter:
    def __init__(self,mex,initial=0,step=1):
        self._max = max
        self._initial = initial
        self._step = step
    def increment(self):
        if self._initial + self._step <= self._max:
            self._initial += self._step
    def get_max(self):
        return self._max
    def get_total(self):
        return self._initial
    def get_step(self):
        return self._step
class LimitedTwowayCounter:
    def __init__(self, _min, max, initial=0, step=1):
        self._min = min
        self._max = max
        self._initial = initial
        self._step = step
    def increment(self):
        if self._initial + self._step <= self._max : self._initial += self. _step
    def decrement(self):
        if self._initial - self._step >= self._min : self._initial -= self._step
    def get_min(self):
        return self._min
    def get__max(self):
        return self._max
    def get_total(self):
        return self. _initial
    def get_step(self):
        return self. _step
class Semaphore:
    def __inti__(self, is_available = False):
        self._is_available = is_available
        if is_available : self.__counter__ = 0 
        else : self.__counter__ = 1 
    def is_available(self):
        return True if self._is_available else  False
    def wait(self):
        if self.__counter__ > 0 : self.__counter__ -=1
    def signal(self):
        if self.__counter__ == 0 : self.__counter__ +=1


