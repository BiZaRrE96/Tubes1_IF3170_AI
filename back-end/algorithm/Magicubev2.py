import magicube as m
import traversal as t
import magicube_adder as a
import copy

class Magicube2(m.Magicube):
    def __init__(self, cube_size: int = 5, straight=False, custom: list[int] = None) -> None:
        super().__init__(cube_size, straight, custom)
        self.fitness_calculated : bool = False
        self.fitness : float = -9999
    
    def get_fitness(self):
        if not self.fitness_calculated:
            self.fitness = a.fitness(self)
            self.fitness_calculated = True
        return self.fitness
    
    def swap_spot(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> None:
        retval = super().swap_spot(x1, y1, z1, x2, y2, z2)
        self.fitness_calculated = False
        return retval

    def copy(self):
        new_cube : Magicube2 = Magicube2(self.size)
        new_cube.numbers = copy.deepcopy(self.numbers)
        new_cube.fitness_calculated = copy.copy(self.fitness_calculated)
        new_cube.fitness = copy.copy(self.fitness)
        return new_cube