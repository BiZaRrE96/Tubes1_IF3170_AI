from Magicubev2 import Magicube2 as Magicube
from magicube import true_example
import genetic_evo_v2 as ge2
from copy import deepcopy


def max_list(l : list[float]):
    mpos = 0
    max = l[0]
    for i in range(1,len(l)):
        if l[i] > max:
            max = l[i]
            mpos = i
    return mpos


cubes : list[Magicube] = [Magicube(5) for i in range(4)]
for cube in cubes:
    print(cube.get_fitness())
print("=====")
for i in range(1024):
    cubes = ge2.breed(cubes,ge2.split)
    
for cube in cubes:
    print(cube.get_fitness())