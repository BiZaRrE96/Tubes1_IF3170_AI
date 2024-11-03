import random
import math
from magicube import Magicube
from magicube_adder import fitness, deviation

def generate_neighbor(cube : Magicube):
    new_cube = cube.copy()
    size = cube.size
    x1 = random.randint(0, size - 1)
    y1 = random.randint(0, size - 1)
    z1 = random.randint(0, size - 1)
    x2 = random.randint(0, size - 1)
    y2 = random.randint(0, size - 1)
    z2 = random.randint(0, size - 1)
    Magicube.swap_spot(new_cube, x1, y1, z1, x2, y2, z2)
    return new_cube

def simulated_annealing(cube : Magicube, initial_temp=1000, cooling_rate=0.999995):
    initial_state = cube
    current_cube = cube
    current_fitness = fitness(cube)
    current_deviation = deviation(cube)
    best_fitness = current_fitness
    best_deviation = current_deviation
    temp = initial_temp
    iteration = 0
    max_fitness_list = []
    avg_fitness_list = []
    
    while temp > 1:
        neighbor_cube = generate_neighbor(current_cube)
        neighbor_fitness = fitness(neighbor_cube)
        neighbor_deviation = deviation(neighbor_cube)
        deltaEF = neighbor_fitness - current_fitness
        deltaED = neighbor_deviation - current_deviation
        exp_term = math.exp(-deltaED / temp)
        
        if neighbor_deviation < current_deviation:
            current_cube = neighbor_cube
            current_fitness = neighbor_fitness
            current_deviation = neighbor_deviation
            if current_deviation < best_deviation:
                best_fitness = current_fitness
                best_deviation = current_deviation
                
        else:
            if exp_term > random.random():
                current_cube = neighbor_cube
                current_fitness = neighbor_fitness
                current_deviation = neighbor_deviation
                if current_deviation < best_deviation:
                    best_fitness = current_fitness
                    best_deviation = current_deviation

        
        max_fitness_list.append(max(current_fitness, neighbor_fitness))
        avg_fitness_list.append((current_fitness + neighbor_fitness) / 2)

        temp *= cooling_rate
        iteration += 1

        print(f"Iteration: {iteration}, Temperature: {temp}, Fitness: {best_fitness}, Deviation: {best_deviation}")

    final_state = current_cube
    final_fitness = best_fitness
    iterations = iteration

    # print("Initial Cube State:")
    # initial_state.print()
    # print("\nFinal Cube State:")
    # final_state.print()
    # print(f"\nFinal Fitness Value: {final_fitness}")
    # print(f"Total Iterations: {iterations}")

true_example = [121,108,7,20,59,31,53,112,109,10,47,61,45,76,86,91,77,71,6,70,25,16,80,104,90,29,28,122,125,11,12,82,34,87,100,107,43,38,33,94,52,64,117,69,13,115,98,4,1,97,51,15,41,124,84,103,3,105,8,96,89,68,63,58,37,30,118,21,123,23,42,111,85,2,75,78,54,99,24,60,113,57,9,62,74,32,93,88,83,19,26,39,92,44,114,66,72,27,102,48,36,110,46,22,101,56,120,55,49,35,40,50,81,65,79,116,17,14,73,95,67,18,119,106,5]
cube = Magicube(5)
simulated_annealing(cube)