from magicube import Magicube
from random import random
import traversal as t
from magicube_adder import fitness

class wheel_spinner:
    def __init__(self, value_list: list[float]) -> None:
        self.total_value = sum(value_list,0)
        self.floor_values : list[float] = [(sum([value_list[i] for i in range(j)]) + value_list[j]) for j in range(len(value_list))]
        pass
    
    def spin(self) -> int:
        target : float = random() * self.total_value
        i = 0
        print("TARGET :",target)
        while (target >= self.floor_values[i]):
            i += 1
        return i
        

def breed(candidates : list[Magicube]):
    #define fitness value for pick
    pass