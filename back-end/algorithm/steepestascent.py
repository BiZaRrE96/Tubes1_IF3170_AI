import magicube_adder as ma
import magicube as m
import traversal as t

n: int = 5
MAX_ITERATION: int = 10000  # Set a high default to allow for extensive searching

cube: m.Magicube = m.Magicube(n)

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size, n // (size**2)])

try:
    for i in range(MAX_ITERATION):
        current_fitness = ma.fitness(cube)
        
        print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")
        
        # Break if optimal solution is found (based on a positive fitness threshold, if applicable)
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

                # Swap spots and evaluate fitness
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
                new_fitness = ma.fitness(cube)

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
        else:
            # Stop the loop if no better solution is found (local optimum reached)
            print(f"End of iteration {i + 1} - No better solution found, stopping.")
            break 

        print(f"Current fitness after iteration {i + 1}: {ma.fitness(cube)}\n")

    print("Final cube configuration:")
    cube.print()

except Exception as e:
    print("An error occurred:", e)
    cube.print()
