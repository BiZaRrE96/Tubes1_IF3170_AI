from Magicubev2 import Magicube2 as Magicube
from magicube import true_example
import genetic_evo_v2 as ge2
from copy import deepcopy

def report_avg_cubes(cl : list[Magicube]) -> dict:
    avg = 0
    avg_count = 0
        
    for cube in cl:
        avg += cube.get_fitness()
        avg_count += 1
    
    retval = {"AVG" : avg/avg_count, "BEST" : max_fitness(cl)}
    return retval
    
def max_list(l : list[float]):
    mpos = 0
    max = l[0]
    for i in range(1,len(l)):
        if l[i] > max:
            max = l[i]
            mpos = i
    return mpos

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

def run(cl : list[Magicube], itterations : int ,method, report : list = None):
    cubes : list[Magicube] = cl.copy()

    for i in range(itterations):
        cubes = ge2.breed(cubes,method)
        # print("=====")
        # for cube in cubes:
        #     print(cube.get_fitness())

    if report != None:
        report += [report_avg_cubes(cubes)]
    print("=====")


def test_wrapper():
    ###START
    report : dict = {"Experiment 1" : {"Disintegrate" : {8 : [],64 : [],512 : []},"Split" : {8 : [],64 : [],512 : []}},"Experiment 2" : {"Disintegrate" : {4 : [],8 : [],16 : []},"Split" : {4 : [],8 : [],16 : []}}}
    cubes : list[Magicube] = [Magicube(5) for i in range(8)]

    report["Reference"] = report_avg_cubes(cubes)
    
    templ = []
    print("\n\n==|| EXPERIMEN BAGIAN 1 ||==")
    print("\n\n==START== DISINTEGRATE")
    print("\nEksperimen 1 : Itteration 8")
    run(cubes[:8],8,ge2.disintegrate, templ)
    run(cubes[:8],8,ge2.disintegrate, templ)
    run(cubes[:8],8,ge2.disintegrate, templ)
    report["Experiment 1"]["Disintegrate"][8] = templ

    templ = []
    print("\nEksperimen 1 : Itteration 64")
    run(cubes[:8],64,ge2.disintegrate, templ)
    run(cubes[:8],64,ge2.disintegrate, templ)
    run(cubes[:8],64,ge2.disintegrate, templ)
    report["Experiment 1"]["Disintegrate"][64] = templ

    templ = []
    print("\nEksperimen 1 : Itteration 512")
    run(cubes[:8],512,ge2.disintegrate, templ)
    run(cubes[:8],512,ge2.disintegrate, templ)
    run(cubes[:8],512,ge2.disintegrate, templ)
    report["Experiment 1"]["Disintegrate"][512] = templ

    templ = []
    print("\n\n==START== SPLIT")
    print("\nEksperimen 1 : Itteration 8")
    run(cubes[:8],8,ge2.split, templ)
    run(cubes[:8],8,ge2.split, templ)
    run(cubes[:8],8,ge2.split, templ)
    report["Experiment 1"]["Split"][8] = templ

    templ = []
    print("\nEksperimen 1 : Itteration 64")
    run(cubes[:8],64,ge2.split, templ)
    run(cubes[:8],64,ge2.split, templ)
    run(cubes[:8],64,ge2.split, templ)
    report["Experiment 1"]["Split"][64] = templ

    templ = []
    print("\nEksperimen 1 : Itteration 512")
    run(cubes[:8],512,ge2.split, templ)
    run(cubes[:8],512,ge2.split, templ)
    run(cubes[:8],512,ge2.split, templ)
    report["Experiment 1"]["Split"][512] = templ


    templ = []
    print("\n\n==|| EXPERIMEN BAGIAN 2 ||==")
    print("\n\n==START== DISINTEGRATE")
    print("\nEksperimen 2 : Sample 4")
    run(cubes[:4],64,ge2.disintegrate, templ)
    run(cubes[:4],64,ge2.disintegrate, templ)
    run(cubes[:4],64,ge2.disintegrate, templ)
    report["Experiment 2"]["Disintegrate"][4] = templ

    templ = []
    print("\nEksperimen 2 : Sample 8")
    run(cubes[:8],64,ge2.disintegrate, templ)
    run(cubes[:8],64,ge2.disintegrate, templ)
    run(cubes[:8],64,ge2.disintegrate, templ)
    report["Experiment 2"]["Disintegrate"][8] = templ

    templ = []
    print("\nEksperimen 2 : Sample 16")
    run(cubes[:16],64,ge2.disintegrate, templ)
    run(cubes[:16],64,ge2.disintegrate, templ)
    run(cubes[:16],64,ge2.disintegrate, templ)
    report["Experiment 2"]["Disintegrate"][16] = templ

    print("\n\n==START== SPLIT")
    
    templ = []
    print("\nEksperimen 2 : Sample 4")
    run(cubes[:4],64,ge2.split, templ)
    run(cubes[:4],64,ge2.split, templ)
    run(cubes[:4],64,ge2.split, templ)
    report["Experiment 2"]["Split"][4] = templ

    templ = []
    print("\nEksperimen 2 : Sample 8")
    run(cubes[:8],64,ge2.split, templ)
    run(cubes[:8],64,ge2.split, templ)
    run(cubes[:8],64,ge2.split, templ)
    report["Experiment 2"]["Split"][8] = templ

    templ = []
    print("\nEksperimen 2 : Sample 16")
    run(cubes[:16],64,ge2.split, templ)
    run(cubes[:16],64,ge2.split, templ)
    run(cubes[:16],64,ge2.split, templ)
    report["Experiment 2"]["Split"][16] = templ
    
    return report
