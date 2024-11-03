import magicube_adder as ma
import magicube as m
import traversal as t
import random
import time

n: int = 5

x = int(input("Enter the maximum number of iterations per restart: "))
y = int(input("Enter the maximum number of restarts: "))
MAX_ITERATION: int = x
MAX_RESTARTS: int = y

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size, n // (size**2)])

# Function to randomize the cube
def randomize_cube(cube: m.Magicube):
    for _ in range(n**3 * 2):  # Arbitrary number of swaps for shuffling
        j = random.randint(0, n**3 - 1)
        k = random.randint(0, n**3 - 1)
        
        if j != k:
            start = generate_vector(j, n)
            target = generate_vector(k, n)
            cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)

cube: m.Magicube = m.Magicube(n)
best_fitness_overall = float('-inf')
best_cube_overall = cube.copy()
restart_count = 0 
total_iterations = 0  

start_time = time.time()
try:
    for restart in range(MAX_RESTARTS):
        restart_count += 1
        randomize_cube(cube)
        current_fitness = ma.fitness(cube)
        print(f"Restart {restart_count} - Starting fitness: {current_fitness}")

        found_optimal = False
        for i in range(MAX_ITERATION):
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

                    new_fitness = ma.fitness(cube)

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

        print(f"Total restarts completed: {restart_count}")
        print(f"Total iterations across all restarts: {total_iterations}")

        if found_optimal:
            break

    end_time = time.time()
    execution_time = end_time - start_time

    print("Final cube configuration with best fitness across all restarts:")
    best_cube_overall.print()
    print(f"Total restarts: {restart_count}")
    print(f"Total iterations: {total_iterations}")
    print(f"Execution time: {execution_time:.2f} seconds") 

except Exception as e:
    print("An error occurred:", e)
    cube.print()
