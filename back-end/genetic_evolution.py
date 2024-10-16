from magicube import Magicube
from random import random
from random import choice
import traversal as t
from magicube_adder import fitness

#testing purposes only
from random import randint

from hilltest import generate_vector

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

#fixes the given cube
def fix_cube(cube : Magicube) -> None:    
    #List out numbers that have duplicates
    dupe_check : list[int] = [0 for i in range(cube.size ** 3)]
    for layer in cube.numbers:
        for column in layer:
            for x in column:
                assert(x <= cube.size ** 3)
                dupe_check[x-1] += 1
    
    blanks = [i+1 for i in range(0,cube.size ** 3) if dupe_check[i] == 0]
    dupes = [[i+1,dupe_check[i]] for i in range(cube.size ** 3) if dupe_check[i] > 1]
    
    #begin repair : assign randomly on dupes
    for i in range(len(dupes)):
        grabbag = [dupes[i][0]]
        for j in range(dupes[i][1]-1):
            pick = choice(blanks)
            grabbag += [pick]
            blanks.remove(pick)
        
        #patch cube
        for j in range(len(grabbag)):
            #getpos : tpos = targetpos
            tpos = cube.find_number(dupes[i][0]) #x,y,z
            pick = choice(grabbag)
            cube.numbers[tpos[2]][tpos[1]][tpos[0]] = pick
            grabbag.remove(pick)
    pass

def breed(candidates : list[Magicube]) -> list[Magicube]: #😭😭😭😭😭😭
    #define fitness value for pick
    fitness_values : list[float] = []
    for cube in candidates:
        fitness_values += [fitness(cube)]
    wheel : wheel_spinner = wheel_spinner(fitness_values)
    
    #start breeding lmao
    pass

#testing artifacts
'''
n = 2
testcube = Magicube(n,False,[randint(1,n**3) for i in range(n**3)])
testcube.print()
print("INTO")
fix_cube(testcube)
testcube.print()
'''