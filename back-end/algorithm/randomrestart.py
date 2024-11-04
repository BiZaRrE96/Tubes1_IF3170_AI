from .utils import magicube_adder as ma
from .utils.Magicubev2 import Magicube2 as Magicube
from .utils.magicube import generate_vector
from .utils.standard_return import standard_return
import random
import time

n: int = 5
def randomrestart(cubelist : list[int] = None, max_iteration : int = None, max_restarts : int = None) -> dict:

        #return values
    start_time = time.time()
    log : str = ""
    
    if cubelist != None:
        cube: Magicube = Magicube(n,custom=cubelist)
    else:
        cube: Magicube = Magicube(n)
        print("Cube unset, randomizing...")
        log += "CUBE UNSET\n"

    if max_iteration != None:
        pass
    else:
        max_iteration = 3
        print("Max itteration unset, setting to 8")
        log += "MAX ITTERATION UNSET\n"

    if max_restarts != None:
        pass
    else:
        max_restarts = 10
        print("Max restarts unset, setting to 10")
        log += "MAX RESTARTS UNSET\n"

    #return values
    first_cube = cube.copy()
    graph : list[float] = [cube.get_fitness()]

    # Function to randomize the cube
    def randomize_cube(cube: Magicube):
        for _ in range(n**3 * 2):  # Arbitrary number of swaps for shuffling
            j = random.randint(0, n**3 - 1)
            k = random.randint(0, n**3 - 1)
            
            if j != k:
                start = generate_vector(j, n)
                target = generate_vector(k, n)
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)

    best_fitness_overall = float('-inf')
    best_cube_overall = cube.copy()
    restart_count = 0 
    total_iterations = 0  

    start_time = time.time()
    try:
        for restart in range(max_restarts):
            restart_count += 1
            randomize_cube(cube)
            current_fitness = cube.get_fitness()
            print(f"Restart {restart_count} - Starting fitness: {current_fitness}")
            log += (f"Restart {restart_count} - Starting fitness: {current_fitness}") + "\n"

            found_optimal = False
            for i in range(max_iteration):
                total_iterations += 1  

                if current_fitness >= 0.0:
                    print("Optimal solution found.")
                    found_optimal = True
                    break
                
                found_better = False
                for _ in range(n**3): 
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
                            print(f"Iteration {i + 1} - Improved fitness: {new_fitness}")
                        else:
                            cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)

                if not found_better:
                    print(f"Iteration {i + 1} - No better solution found, moving to next restart.")
                    break

                print(f"End of iteration {i + 1} - Current fitness: {current_fitness}")

            if current_fitness > best_fitness_overall:
                best_fitness_overall = current_fitness
                best_cube_overall = cube.copy()
                print(f"New overall best fitness: {best_fitness_overall}")
                log += (f"New overall best fitness: {best_fitness_overall}") + "\n"
                
                graph += [best_fitness_overall]

            print(f"Total restarts completed: {restart_count}")
            print(f"Total iterations across all restarts: {total_iterations}")

            if found_optimal:
                break

        

        print("Final cube configuration with best fitness across all restarts:")
        best_cube_overall.print()
        print(f"Total restarts: {restart_count}")
        log = (f"Total restarts: {restart_count}") + "\n" + log
        print(f"Total iterations: {total_iterations}")
        log = (f"Total iterations: {total_iterations}") + "\n" + log
        
        

    except Exception as e:
        print("An error occurred:", e)
        cube.print()
        
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
    log = f"Itterations : {total_iterations} |\n" + log
    return standard_return(first_cube,cube,graph,execution_time,log)
