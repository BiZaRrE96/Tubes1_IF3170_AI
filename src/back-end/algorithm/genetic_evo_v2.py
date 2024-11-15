from .utils.Magicubev2 import Magicube2 as Magicube
from .utils.magicube import generate_vector
from random import random
from random import choice
from .utils import traversal as t
from typing import Callable
from math import exp
from math import log
from math import e as euler
from math import sin as sin
from math import pi as pi
from random import randint
import time
from .utils.standard_return import standard_return

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
    #print("zzz",pos)
    for i in range(pos):
        x = i % m1.size
        y = i // (m1.size) % m1.size 
        z = i // (m1.size**2)
        #print(x,y,z)
        custom += [m1.get(x,y,z)]
    for i in range(pos,(m1.size**3)):
        x = i % m1.size
        y = i // (m1.size**2) % m1.size
        z = i // (m1.size**2)
        custom += [m2.get(x,y,z)]
    #print(len(custom))
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
        
        #print(c1,c2)

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
        mutation_factor = 0.01
                         
        #mutation only swaps two positions so no need to refix
        mutate(child,mutation_factor)
        retval += [child]
    #start breeding lmao
    return retval

'''=== === ==='''

def report_avg_cubes(cl : list[Magicube]) -> dict:
    avg = 0
    avg_count = 0
        
    for cube in cl:
        avg += cube.get_fitness()
        avg_count += 1
    
    retval = {"AVG" : avg/avg_count, "BEST" : max_fitness(cl)}
    return retval

def max_fitness(lc : list[Magicube]):
    mpos = 0
    max = -999999
    bestcube : Magicube = None
    for cube in lc:
        if cube.get_fitness() > max :
            bestcube = cube.copy()
            max = cube.get_fitness()
    return max

def best_cube(lc : list[Magicube]):
    mpos = 0
    max = -999999
    bestcube : Magicube = None
    for cube in lc:
        if cube.get_fitness() > max :
            bestcube = cube.copy()
            max = cube.get_fitness()
    return bestcube

#use samples if want to define samples, use sample count to tell how many to generate
def genetic_algorithm(sample_count : int = None, itterations : int = None, methodstr : str = None):
    #return values
    runs : int = 0
    start_time = time.time()
    log : str = ""

    if sample_count != None:
        pass
    else:
        sample_count = 4
        print("Sample count unset! setting to 4...")
        log += "SAMPLE COUNT UNSET\n"
        
    if itterations != None:
        pass
    else:
        itterations = 64
        print("Itterations unset! setting to 64...")
        log += "ITTERATIONS UNSET\n"
    
    if methodstr in ["disintegrate","split"]:
        pass
    else:
        methodstr = "disintegrate"
        print("Method unset! setting to disintegrate")
        log += "METHOD UNSET\n"
    
    method : Callable = None
    if (methodstr == "disintegrate"):
        method = disintegrate
    elif (methodstr == "split"):
        method = split

    cubes = [Magicube(5) for i in range(sample_count)]
    
    #return values
    first_cube = best_cube(cubes).copy()
    report = report_avg_cubes(cubes)
    graph : list[float] = [report["BEST"]]
    graph_avg : list[float] = [report["AVG"]]
    
    try:
        for i in range(itterations):
            runs += 1
            cubes = breed(cubes,method)
            
            report = report_avg_cubes(cubes)
            avg = report["AVG"]
            best = report["BEST"]
            print(f"Run-{i+1}) Average: {avg:.2f}, Best: {best:.2f}")
            log += f"Run-{i+1}) Average: {avg:.2f}, Best: {best:.2f}\n"
            
            graph += [report["BEST"]]
            graph_avg += [report["AVG"]]
            
        print("END")
            
    except Exception as e:
        print("Error :",e)
        log += "ERROR : " + e.__context__
        
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
    log = f"Itterations : {runs} |\n" + log
    
    return standard_return(first_cube,best_cube(cubes),graph,execution_time,log,{"graph_avg" : graph_avg})