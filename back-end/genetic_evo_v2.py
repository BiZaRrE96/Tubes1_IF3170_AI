from Magicubev2 import Magicube2 as Magicube
from random import random
from random import choice
import traversal as t
from typing import Callable
from math import exp
from math import log
from math import e as euler
from math import sin as sin
from math import pi as pi
#testing purposes only
from random import randint

from hilltest import generate_vector

class wheel_spinner:
    def __init__(self, value_list: list[float], flip : bool = False) -> None:
        self.floor_values : list[float] = []
        self.total_value = sum(value_list,0)
        
        if (flip):    
            value_list = [value - self.total_value for value in value_list]
            self.total_value = sum(value_list,0)
        
        chances = []
        for j in range(len(value_list)):
            chances += [value_list[j] / self.total_value]
            self.floor_values += [(sum([value_list[i] for i in range(j)]) + value_list[j])/self.total_value]
    
        pass
    
    def spin(self) -> int:
        target : float = random()
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
    f1 = m1.get_fitness()
    f2 = m2.get_fitness()
    picker = wheel_spinner([f1,f2],True)
    maxpos = m1.size**3
    numberlist : list[int] = []
    
    #begin splicing
    pick = [m1,m2]
    ###pickrate = [0,0]
    for i in range(maxpos):
        pos : t.Vector3 = generate_vector(i,m1.size)
        pickno = picker.spin()
        numberlist += [pick[pickno].get(pos.x,pos.y,pos.z)]
        ###pickrate[pickno] += 1
    
    ###print(f1,f2)
    ###print("PICKRATE :",pickrate)
    return Magicube(m1.size,custom=numberlist)
    pass

###ERROR HERE
def split(m1: Magicube, m2: Magicube) -> Magicube:
    pos : int = round(sin(random()*pi) * (m1.size**3))
    custom : list[int] = []
    print("zzz",pos)
    for i in range(pos):
        x = i % m1.size
        y = i // (m1.size) % m1.size 
        z = i // (m1.size**2)
        print(x,y,z)
        custom += [m1.get(x,y,z)]
    for i in range(pos,(m1.size**3-pos-1)):
        x = i % m1.size
        y = i // (m1.size**2) % m1.size
        z = i // (m1.size**2)
        custom += [m2.get(x,y,z)]
    
    return Magicube(m1.size,custom=custom)
        
    

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
        fitness_values += [cube.get_fitness()]
    wheel : wheel_spinner = wheel_spinner(fitness_values,True)
    
    retval : list[Magicube] = []
    #splice until have same ammount as supplied candidates or speciffied times
    #candidate numbers :
    for i in range(max_itter):
        c1 = wheel.spin()
        c2 = wheel.spin()
        #print("SPEEN :",c1,c2)
        if (c1 != c2): #skip splicing if its the same
            child = splice_method(candidates[c1],candidates[c2])
        else:
            child = candidates[c1].copy()
        fix_cube(child)

        csize = candidates[c1].size
        mv = -(csize ** 3)
        p = (candidates[c1].get_fitness() + candidates[c2].get_fitness())/2
        f = child.get_fitness()
        #PARENT modification
        
        #NO MUTATION IF CHILD IS BETTER
                    
                    # if (f>p): #if child is better, lessen mutation
                    #     mutation_factor = 0
                    # else:
                    #     mutation_factor = ((-f + p) * 0.5 * euler / (csize**3)) + 0.25
        mutation_factor = 0
                         
        #mutation only swaps two positions so no need to refix
        mutate(child,mutation_factor)
        retval += [child]
    #start breeding lmao
    return retval
    pass

#testing artifacts
