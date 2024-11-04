from .utils import magicube_adder as ma
from .utils.Magicubev2 import Magicube2 as Magicube
from .utils.magicube import generate_vector
from .utils import traversal as t
from .utils.standard_return import standard_return
import time

n: int = 5
MAX_ITERATION: int = 2

def steepestascent(cubelist : list[int] = None) -> dict:
    
    runs : int = 0
    
    if cubelist != None:
        cube: Magicube = Magicube(n,custom=cubelist)
    else:
        cube: Magicube = Magicube(n)

    first_cube = cube.copy()
    
    #return values
    start_time = time.time()
    graph : list[float] = [cube.get_fitness()]
    log : str = ""
    
    try:
        for i in range(MAX_ITERATION):
            current_fitness = cube.get_fitness()
            
            print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")
            log += (f"Iteration {i + 1} - Starting fitness: {current_fitness}") + "\n"
            
            # Break if optimal solution is found (based on a positive fitness threshold, if applicable)
            if current_fitness >= 0.0:
                print("Optimal solution found.")
                log += ("Optimal solution found.")
                break
            
            found_better = False
            best_cube = cube.copy()
            best_fitness = current_fitness

            for j in range(n**3 - 1):
                start = generate_vector(j, n)

                for k in range(j + 1, n**3):
                    target = generate_vector(k, n)

                    # Swap spots and evaluate fitness
                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
                    new_fitness = cube.get_fitness()

                    if new_fitness > best_fitness:
                        best_fitness = new_fitness
                        found_better = True
                        best_cube = cube.copy()
                        print(f"NEW: {best_fitness} >> Current fitness after swap: {new_fitness}")
                    
                    # Swap back to original configuration
                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
            
            # If a better solution was found, update the cube
            if found_better:
                cube = best_cube
                print(f"End of iteration {i + 1} - New best fitness: {best_fitness}")
                log += (f"End of iteration {i + 1} - New best fitness: {best_fitness}") + "\n"
            else:
                # Stop the loop if no better solution is found (local optimum reached)
                print(f"End of iteration {i + 1} - No better solution found, stopping.")
                log += (f"End of iteration {i + 1} - New best fitness: {best_fitness}") + "\n"
                runs = i + 1
                break 
            
            graph += [best_fitness]
            print(f"Current fitness after iteration {i + 1}: {cube.get_fitness()}\n")
            log += (f"Current fitness after iteration {i + 1}: {cube.get_fitness()}\n") + "\n"

        print("Final cube configuration:")
        cube.print()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.2f} seconds")
        
        

    except Exception as e:
        print("An error occurred:", e)
        cube.print()

    log = f"Itterations : {runs} |\n" + log
    return standard_return(first_cube, cube, graph, execution_time, log = log)
