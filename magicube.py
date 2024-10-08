import random

# Generate a list of numbers from 1 to n, and randomized into a list
def generate_n_stack(n: int):
    numbers : list[int] = [i+1 for i in range(n)]
    retval : list[int] = []
    for i in range(n):
        get : int = random.randint(0,n-1-i)
        retval = retval + [numbers[get]]
        numbers = numbers[:get] + numbers[get+1:]
    return retval
    pass    

class magicube:
    def __init__(self, cube_size : int = 5) -> None:
        #define cube size (n^3)
        self.size : int = cube_size
        
        #generate random state
        self.numbers : list[list[list[int]]] = []
        
        #populate cube
        randstack = generate_n_stack(self.size * self.size * self.size)
        for i in range(self.size):
            temp_j : list[list[int]] = []
            for j in range(self.size):
                temp_k : list[int] = []
                for k in range(self.size):
                    temp_k = temp_k + [randstack[(i * self.size * self.size) + (j * self.size) + k]]
                temp_j = temp_j + [temp_k]
            self.numbers = self.numbers + [temp_j]