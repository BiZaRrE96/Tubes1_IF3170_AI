import magicube_adder as ma
import magicube as m
import traversal as t
import random

n: int = 5

x = int(input("Enter the maximum iteration: "))
MAX_ITERATION: int = x

cube: m.Magicube = m.Magicube(n)

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size, n // (size**2)])

try:
    for i in range(MAX_ITERATION):
        current_fitness = ma.fitness(cube)
        
        print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")
        
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

                new_fitness = ma.fitness(cube)

                if new_fitness > current_fitness:
                    current_fitness = new_fitness
                    found_better = True
                    print(f"NEW: {new_fitness} >> Current fitness after swap: {ma.fitness(cube)}")
                else:
                    cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)

        if not found_better:
            print(f"End of iteration {i + 1} - No better solution found, stopping.")
            break
        else:
            print(f"End of iteration {i + 1} - New fitness: {current_fitness}")

        print(f"Current fitness after iteration {i + 1}: {current_fitness}\n")

    print("Final cube configuration:")
    cube.print()

except Exception as e:
    print("An error occurred:", e)
    cube.print()
