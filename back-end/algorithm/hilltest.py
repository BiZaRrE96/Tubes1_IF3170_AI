from .utils import magicube_adder as ma
from .utils import magicube as m
from .utils import traversal as t
import time

n : int = 5

MAX_ITTERATION : int = 10

cube : m.Magicube = m.Magicube(n)

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size , n // (size**2)])

'''
try:
    for i in range(MAX_ITTERATION):
        if ma.fitness(cube) >= -0.0:
            break
        found_better : bool = False
        temp_cube : m.Magicube # = cube.copy()
        for j in range(n**3-1):
            start : t.Vector3 = generate_vector(j,n)
            bestval : float = ma.fitness(cube)
            for k in range(n**3-1-j):
                target : t.Vector3 = generate_vector(k+j,n)
                cube.swap_spot(start.x,start.y,start.z,target.x,target.y,target.z)
                if ma.fitness(cube) > bestval:
                    bestval = ma.fitness(cube)
                    found_better = True
                    print("NEW :",bestval, end = "")
                    print(" >>",ma.fitness(cube))
                    temp_cube = cube.copy()
                #revert swap
                cube.swap_spot(start.x,start.y,start.z,target.x,target.y,target.z)
        if found_better:
            cube = temp_cube.copy()
        print("Curval :",ma.fitness(cube))
except e:
    cube.print()
'''