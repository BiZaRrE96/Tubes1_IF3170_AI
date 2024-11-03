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


cubes : list[Magicube] = [Magicube(5) for i in range(8)]

avg = 0
avg_count = 0
for cube in cubes:
    print(cube.get_fitness())
    avg += cube.get_fitness()
    avg_count += 1
print("AVERAGE :",avg/avg_count)

for i in range(128):
    cubes = ge2.breed(cubes,ge2.disintegrate)
    # print("=====")
    # for cube in cubes:
    #     print(cube.get_fitness())

print("=====")
avg = 0
avg_count = 0
for cube in cubes:
    print(cube.get_fitness())
    avg += cube.get_fitness()
    avg_count += 1
print("AVERAGE :",avg/avg_count)