def simulated_annealing(self, initial_temp=100, cooling_rate=0.9999):
    """Implementasi Simulated Annealing"""
    time_start = time.time()
    current_fitness = self.fitness()
    temp = initial_temp

    while temp > 1:
        self.generate_neighbor()
        neighbor_fitness = self.fitness()

        if neighbor_fitness < current_fitness or random.random() < math.exp((current_fitness - neighbor_fitness) / temp):
            current_fitness = neighbor_fitness

        temp *= cooling_rate

    print(f"Final fitness after annealing: {current_fitness}")
    time_end = time.time()
    print(f"Time taken: {time_end - time_start} seconds")