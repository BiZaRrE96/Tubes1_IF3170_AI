from magicube import Magicube
from random import random
from random import choice
import traversal as t
from magicube_adder import fitness
from typing import Callable
from math import exp
from math import log
from math import e as euler

#testing purposes only
from random import randint

from hilltest import generate_vector

class wheel_spinner:
    def __init__(self, value_list: list[float], flip : bool = False) -> None:
        self.total_value = sum(value_list,0)
        modifier = 0
        if flip:
            self.total_value *= (-1)
            modifier = self.total_value
        self.floor_values : list[float] = [(sum([value_list[i] + modifier for i in range(j)]) + value_list[j] + modifier) for j in range(len(value_list))]

        pass
    
    def spin(self) -> int:
        target : float = random() * self.total_value
        i = 0
        #print("TARGET :",target)
        while (target >= self.floor_values[i]):
            i += 1
        return i

#fixes the given cube
def fix_cube(cube : Magicube) -> None:    
    duplicate_exists : bool = False
    #List out numbers that have duplicates
    dupe_check : list[int] = [0 for i in range(cube.size ** 3)]
    for layer in cube.numbers:
        for column in layer:
            for x in column:
                assert(x <= cube.size ** 3)
                dupe_check[x-1] += 1
                if dupe_check[x-1] > 1:
                    duplicate_exists = True
    if duplicate_exists:
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

#mutate
def mutate(cube : Magicube, severity : float) -> None:
    maxint = cube.size**3
    mutate_ammount = round(severity * (maxint))
    for i in range(mutate_ammount):
        a = 0 
        b = 0
        while (a == b):
            a = randint(1,maxint)
            b = randint(1,maxint)
        cube.swap_num(a,b)
        

#2 strategies : disintegrate and cut, fix cube gets called by breed
#DONT FORGET TO COPY
def disintegrate(m1 : Magicube, m2 : Magicube) -> Magicube:
    #semakin bagus cube, semakin tinggi kemungkinan nilainya diambil
    f1 = fitness(m1)
    f2 = fitness(m2)
    picker = wheel_spinner([f1,f2],True)
    maxpos = m1.size**3
    numberlist : list[int] = []
    
    #begin splicing
    pick = [m1,m2]
    for i in range(maxpos):
        pos : t.Vector3 = generate_vector(i,m1.size)
        numberlist += [pick[picker.spin()].get(pos.x,pos.y,pos.z)]
    
    return Magicube(m1.size,custom=numberlist)
    pass

def splice(m1 : Magicube, m2 : Magicube) -> Magicube:
    pass

#mutation isnt necesarilly needed seeing how fix_cube has some kind of randomness
#though when the scenario of two same cubes get picked, it is necesarry
def breed(candidates : list[Magicube], splice_method: Callable[[Magicube,Magicube],Magicube], max_itter : int = None) -> list[Magicube]: #😭😭😭😭😭😭
    #init variables
    if (max_itter != None):
        pass
    else:
        max_itter = len(candidates)
        
    #define fitness value for pick
    fitness_values : list[float] = []
    for cube in candidates:
        fitness_values += [fitness(cube)]
    wheel : wheel_spinner = wheel_spinner(fitness_values,True)
    
    retval : list[Magicube] = []
    #splice until have same ammount as supplied candidates or speciffied times
    #candidate numbers :
    c1 = wheel.spin()
    c2 = wheel.spin()
    for i in range(max_itter):
        if (c1 != c2): #skip splicing if its the same
            child = splice_method(candidates[c1],candidates[c2])
        else:
            child = candidates[c1].copy()
        fix_cube(child)

        #SEMAKIN JELEK NILAI CUBE, SEMAKIN TINGGI TINGKAT MUTASI
        #FOR THE TIME BEING IM NOT IMPLEMENTING THE COMPLEX MUTATION DECISIONS
        
        #correction : The better the cube is compared to its parrent, the less mutation it will recieve
        #factors : distance from 0, distance from parent
        
        #THIS VERSION : PURELY BY DISTANCE FROM 0
        # y = exp(-x*loge(2)/125)-1
        f = fitness(child)
        mutation_factor = exp(-f*log(2,euler)/(child.size**3))-1
        mutation_factor = mutation_factor * mutation_factor
        #mutation only swaps two positions so no need to refix
        mutate(child,mutation_factor)
        
        retval += [child]
    #start breeding lmao
    return retval
    pass

#testing artifacts
'''
n = 5
cube_a = Magicube(n)
cube_b = Magicube(n)

print("A :",fitness(cube_a))
# cube_a.print()
print("B :",fitness(cube_b))
# cube_b.print()

test_value : list[float] = []
for i in range(5):
    test_value += [fitness(breed([cube_a,cube_b],disintegrate, 1)[0])]
print(sum(test_value)/len(test_value))
'''

listc = [Magicube(3),Magicube(3),Magicube(3),Magicube(3)]
for i in range(64):
    listc = breed(listc,disintegrate)
for cube in listc:
    print(fitness(cube))