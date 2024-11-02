from . import magicube_adder as ma
from . import magicube as m
import traversal as t

n: int = 5
MAX_ITERATION: int = 10

cube: m.Magicube = m.Magicube(n)

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size, n // (size**2)])

try:
    for i in range(MAX_ITERATION):
        current_fitness = ma.fitness(cube)
        
        print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")
        
        # Check if the current cube is optimal
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
                
                # Swap positions
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
                
                # Calculate fitness after swap
                new_fitness = ma.fitness(cube)
                
                # If the new configuration is better, save it
                if new_fitness > best_fitness:
                    best_fitness = new_fitness
                    found_better = True
                    best_cube = cube.copy()
                    print(f"NEW: {best_fitness} >> Current fitness after swap: {ma.fitness(cube)}")
                
                # Revert swap
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
        
        # Update the cube if a better configuration was found
        if found_better:
            cube = best_cube
            print(f"End of iteration {i + 1} - New best fitness: {best_fitness}")
        else:
            print(f"End of iteration {i + 1} - No better solution found.")

        print(f"Current fitness after iteration {i + 1}: {ma.fitness(cube)}\n")

    # Print the final cube configuration after last iteration
    print("Final cube configuration:")
    cube.print()

except Exception as e:
    print("An error occurred:", e)
    cube.print()
