from .utils import magicube_adder as ma
from .utils import magicube as m
from .utils import traversal as t
import time

n: int = 5

# Menerima input dari pengguna untuk jumlah maksimum iterasi

MAX_ITERATION: int = 10
cube: m.Magicube = m.Magicube(n)

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size, n // (size**2)])

start_time = time.time()
try:
    sideways_moves_limit = int(input("Masukkan parameter maksimum sideways move : "))  #Parameter maximum sideways moves
    sideways_moves = 0 
    current_fitness = ma.fitness(cube)

    for i in range(MAX_ITERATION):
        print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")

        # Memeriksa apakah kubus saat ini sudah optimal
        if current_fitness >= 0.0:
            print("Optimal solution found.")
            break
        
        found_better = False
        best_cube = cube.copy()
        best_fitness = current_fitness

        for j in range(n**3 - 1):
            start = generate_vector(j, n)

            for k in range(j + 1, n**3):
                target = generate_vector(k, n)
                
                # Menukar posisi
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
                
                # Menghitung fitness setelah swap
                neighbor_fitness = ma.fitness(cube)
                
                # Jika konfigurasi baru lebih baik, simpan
                if neighbor_fitness >= best_fitness:
                    best_fitness = neighbor_fitness
                    found_better = True
                    best_cube = cube.copy()
                    print(f"NEW: {best_fitness} >> Current fitness after swap: {ma.fitness(cube)}")
                
                # Kembalikan swap
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
        
        if found_better:
            cube = best_cube
            current_fitness = best_fitness  
            sideways_moves = 0  
            print(f"End of iteration {i + 1} - New best fitness: {best_fitness}")
        else:
            sideways_moves += 1
            print(f"End of iteration {i + 1} - No better solution found. Sideways moves: {sideways_moves}")

            if sideways_moves >= sideways_moves_limit:
                print("Stopped due to exceeding sideways move limit.")
                break

        print(f"Current fitness after iteration {i + 1}: {current_fitness}\n")

    print("Final cube configuration:")
    cube.print()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

except Exception as e:
    print("An error occurred:", e)
    cube.print()
