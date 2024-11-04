from .utils import magicube_adder as ma
from .utils.magicube import generate_vector
from .utils.Magicubev2 import Magicube2 as Magicube
from .utils import traversal as t
from random import randint
from .utils.standard_return import standard_return
import time

n: int = 5

# Menerima input dari pengguna untuk jumlah maksimum iterasi
#max_iteration: int = 10

def sidewaysmove(cubelist : list[int] = None, max_iteration : int = None, max_sidewaysmove : int = None) -> dict:
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

    if max_sidewaysmove != None:
        sideways_moves_limit = max_sidewaysmove
    else:
        sideways_moves_limit = 3
        print("Max sidewaysmove unset, setting to 10")
        log += "MAX SIDEWAYS MOVE UNSET\n"

    #return values
    first_cube = cube.copy()
    graph : list[float] = [cube.get_fitness()]
    
    try:
        sideways_moves = 0 
        current_fitness = cube.get_fitness()

        for i in range(max_iteration):
            print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")

            # Memeriksa apakah kubus saat ini sudah optimal
            if current_fitness >= 0.0:
                print("Optimal solution found.")
                break
            
            found_better = False
            best_cube = cube.copy()
            best_fitness = current_fitness
            neighbor = []

            for j in range(n**3 - 1):
                start = generate_vector(j, n)

                for k in range(j + 1, n**3):
                    target = generate_vector(k, n)
                    
                    # Menukar posisi
                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
                    
                    # Menghitung fitness setelah swap
                    neighbor_fitness = cube.get_fitness()
                    
                    # Jika konfigurasi baru lebih baik, simpan
                    if neighbor_fitness > best_fitness:
                        found_better = True
                        best_fitness = neighbor_fitness
                        best_cube = cube.copy()
                        print(f"NEW: {best_fitness} >> Current fitness after swap: {cube.get_fitness()}")
                    elif neighbor_fitness == best_fitness:
                        neighbor += [[generate_vector(j,n),generate_vector(k,n)]]
                    
                    # Kembalikan swap
                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
            
            if found_better:
                cube = best_cube
                current_fitness = best_fitness  
                sideways_moves = 0  
                
                print(f"End of iteration {i + 1} - New best fitness: {best_fitness}")
                log += (f"End of iteration {i + 1} - New best fitness: {best_fitness}") + "\n"
                graph += [best_fitness]
            elif len(neighbor) > 0:
                sideways_moves += 1
                print(f"End of iteration {i + 1} - No better solution found. Sideways moves: {sideways_moves}")
                log += (f"End of iteration {i + 1} - No better solution found. Sideways moves: {sideways_moves}") + "\n"
                graph += [cube.get_fitness()]
                if sideways_moves >= sideways_moves_limit:
                    print("Stopped due to exceeding sideways move limit.")
                    break
                else:
                    #pick random neighbor
                    random_pick = randint(0, len(neighbor))
                    start = neighbor[random_pick][0]
                    target = neighbor[random_pick][1]
                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
            else:
                print(f"End of iteration {i + 1} - No better solution found & Local maxima.")
                log(f"End of iteration {i + 1} - No better solution found & Local maxima.")
                break

            print(f"Current fitness after iteration {i + 1}: {current_fitness}\n")

        print("Final cube configuration:")
        cube.print()

    except Exception as e:
        print("An error occurred:", e)
        cube.print()
        
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

    return standard_return(first_cube,cube,graph,execution_time,log)