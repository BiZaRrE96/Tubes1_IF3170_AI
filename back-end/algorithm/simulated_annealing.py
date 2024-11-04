import random
import math
from .utils.Magicubev2 import Magicube2 as Magicube
from .utils.magicube_adder import fitness, deviation
from .utils.standard_return import standard_return
import matplotlib.pyplot as plt
import time

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

n : int = 5

def simulated_annealing(cubelist : list[int]=None, initial_temp=None, cooling_rate=None) -> dict:
    
    #return values
    start_time = time.time()
    log : str = ""
    
    if cubelist != None:
        cube: Magicube = Magicube(n,custom=cubelist)
    else:
        cube: Magicube = Magicube(n)
        print("Cube unset, randomizing...")
        log += "CUBE UNSET\n"
        
    if initial_temp != None:
        pass
    else:
        initial_temp = 1000
        print("Initial temp unset! setting to 1000...")
        log += "INITIAL TEMP UNSET\n"
        
    if cooling_rate != None:
        pass
    else:
        cooling_rate = 0.99995
        print("cooling rate unset! setting to 0.99995...")
        log += "INITIAL TEMP UNSET\n"

    #return values
    first_cube = cube.copy()
    best_cube : Magicube = None
    graph : list[float] = [cube.get_fitness()]
    
    current_cube = cube
    current_fitness = cube.get_fitness()
    current_deviation = deviation(cube)
    best_fitness = current_fitness
    best_deviation = current_deviation
    temp = initial_temp
    iteration = 0
    max_fitness_list = []
    avg_fitness_list = []
    exp_term_list = []

    stuck_counter = 0
    stuck_frequency = 0
    
    start_time = time.time()
    while temp > 1:
        neighbor_cube = generate_neighbor(current_cube)
        neighbor_fitness = neighbor_cube.get_fitness()
        neighbor_deviation = deviation(neighbor_cube)
        deltaEF = neighbor_fitness - current_fitness
        deltaED = neighbor_deviation - current_deviation
        exp_term = math.exp(-deltaED / temp)
        
        if neighbor_deviation < current_deviation:
            current_cube = neighbor_cube.copy()
            current_fitness = neighbor_fitness
            current_deviation = neighbor_deviation
            if current_deviation < best_deviation:
                best_cube = current_cube.copy()
                best_fitness = current_fitness
                best_deviation = current_deviation
            stuck_counter = 0
                
        else:
            if exp_term > random.random():
                current_cube = neighbor_cube.copy()
                current_fitness = neighbor_fitness
                current_deviation = neighbor_deviation
                if current_deviation < best_deviation:
                    best_cube = current_cube.copy()
                    best_fitness = current_fitness
                    best_deviation = current_deviation
            stuck_counter += 1

        if stuck_counter > 1:
            stuck_frequency += 1
            stuck_counter = 0

        
        max_fitness_list.append(max(current_fitness, neighbor_fitness))
        avg_fitness_list.append((current_fitness + neighbor_fitness) / 2)
        exp_term_list.append(exp_term)

        temp *= cooling_rate
        iteration += 1

        print(f"Iteration: {iteration}, Temperature: {temp}, Fitness: {best_fitness}, Deviation: {best_deviation}")
        log += (f"Iteration: {iteration}, Temperature: {temp}, Fitness: {best_fitness}, Deviation: {best_deviation}") + "\n"
    end_time = time.time()


    # plt.figure(figsize=(10, 6))
    # plt.plot(max_fitness_list, label='Max Fitness', color='blue')
    # plt.plot(avg_fitness_list, label='Average Fitness', color='orange')
    # plt.xlabel('Iterations')
    # plt.ylabel('Objective Function Value')
    # plt.title('Objective Function Value vs Iterations')
    # plt.legend()
    # plt.show()

    time_exec = end_time - start_time

    print("RESULT")
    print(f"Best Fitness: {best_fitness}, Best Deviation: {best_deviation}, Iteration: {iteration}, Time: {time_exec}, Stuck Frequency: {stuck_frequency}")
    log =(f"Best Fitness: {best_fitness}\nBest Deviation: {best_deviation}\nIteration: {iteration}\nTime: {time_exec}\nStuck Frequency: {stuck_frequency}") + log
    log = f"Itterations : {iteration} |\n" + log
    return standard_return(first_cube,best_cube,max_fitness_list,time_exec,log,{"avg_graph":avg_fitness_list,"exp_graph":exp_term_list,"stuck_freq":stuck_frequency})
    ##return best_fitness, max_fitness_list, avg_fitness_list, exp_term_list, iteration, time_exec, stuck_frequency

