from .utils import magicube_adder as ma
from .utils.Magicubev2 import Magicube2 as Magicube
from .utils.magicube import generate_vector
from .utils import traversal as t
from .utils.standard_return import standard_return
import random
import time

n: int = 5

# x = int(input("Enter the maximum iteration: "))

def stocastic(cubelist : list[int] = None, max_iteration : int = None) -> dict:
    #return values
    start_time = time.time()
    log : str = ""
    runs : int = 0
    
    if cubelist != None:
        cube: Magicube = Magicube(n,custom=cubelist)
    else:
        cube: Magicube = Magicube(n)
        print("Cube unset, randomizing...")
        log += "CUBE UNSET\n"
        
    if max_iteration != None:
        pass
    else:
        max_iteration = 8
        print("Max itteration unset, setting to 8")
        log += "MAX ITTERATION UNSET\n"

    #return values
    first_cube = cube.copy()
    graph : list[float] = [cube.get_fitness()]

    try:
        for i in range(max_iteration):
            current_fitness = cube.get_fitness()
            
            print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")
            log += (f"Iteration {i + 1} - Starting fitness: {current_fitness}") + "\n"
            
            if current_fitness >= 0.0:
                print("Optimal solution found.")
                break
            
            found_better = False

            for _ in range(n**3):  #Fungsi untuk merandom penukaran
                j = random.randint(0, n**3 - 1)
                k = random.randint(0, n**3 - 1)

                if j != k:
                    start = generate_vector(j, n)
                    target = generate_vector(k, n)

                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)

                    new_fitness = cube.get_fitness()

                    if new_fitness > current_fitness:
                        current_fitness = new_fitness
                        found_better = True
                        print(f"NEW: {new_fitness} >> Current fitness after swap: {cube.get_fitness()}")
                    else:
                        cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)

            if not found_better:
                print(f"End of iteration {i + 1} - No better solution found, stopping.")
                log += (f"End of iteration {i + 1} - No better solution found, stopping.") + "\n"
                runs = i + 1
                break
            else:
                print(f"End of iteration {i + 1} - New fitness: {current_fitness}")
                log += (f"End of iteration {i + 1} - New fitness: {current_fitness}") + "\n"
                graph += [current_fitness]

            print(f"Current fitness after iteration {i + 1}: {current_fitness}\n")

        print("Final cube configuration:")
        cube.print()

    except Exception as e:
        print("An error occurred:", e)
        log += ("An error occurred:", e)
        cube.print()
        
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
    
    log = f"Itterations : {runs} |\n" + log

    return standard_return(first_cube, cube, graph, execution_time, log = log)