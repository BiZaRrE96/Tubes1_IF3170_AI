import random
from . import exceptions as ex
import copy
from .traversal import Vector3

# Generate a list of numbers from 1 to n, and randomized into a list
def generate_n_stack(n: int, straight: bool = False):
    numbers : list[int] = [i+1 for i in range(n)]
    if straight:
        return numbers
    retval : list[int] = []
    for i in range(n):
        get : int = random.randint(0,n-1-i)
        retval = retval + [numbers[get]]
        numbers = numbers[:get] + numbers[get+1:]
    return retval
    pass    

def generate_vector(n: int, size: int) -> Vector3:
    return Vector3([n % size, n // (size) % size, n // (size**2)])

#X < > (Kiri kanan); Y /\ \/ (atas bawah); Z (+) (-) (depan belakang)
#therefore Magicube.numbers[Z][Y][X]

#X 0 -> +; Y /\ +; Z ke arah kita positif

class Magicube:
    def __init__(self, cube_size : int = 5, straight = False, custom: list[int] = None) -> None:
        #define cube size (n^3)
        self.size : int = cube_size
        
        #generate random state
        self.numbers : list[list[list[int]]] = []
        
        randstack: list[int]
        #populate cube
        if custom != None:
            randstack = custom
        else:
            randstack = generate_n_stack(self.size ** 3, straight)
        
        for i in range(self.size):
            temp_j : list[list[int]] = []
            for j in range(self.size):
                temp_k : list[int] = []
                for k in range(self.size):
                    temp_k = temp_k + [randstack[(i * self.size ** 2) + (j * self.size) + k]]
                temp_j = temp_j + [temp_k]
            self.numbers = self.numbers + [temp_j]
    
    def find_number(self, number: int) -> list[int]: #xyz
        if (number > self.size ** 3):
            raise ex.IllegalInputException("Number too big!")
        for z in range(self.size):
            for y in range(self.size):
                for x in range(self.size):
                    # DEBUG : print(self.numbers[z][y][x])
                    if self.numbers[z][y][x] == number:
                        #DEBUG : print("x",x,"y",y,"z",z)
                        return [x,y,z]

    #note, mulai dari 0 ya    
    def swap_spot(self, x1:int ,y1:int ,z1:int, x2:int, y2:int, z2:int) -> None:
        check_input : list[int] = [x1,y1,z1,x2,y2,z2]
        for i in range(6):
            if check_input[i] < 0 or check_input[i] >= self.size:
                raise ex.IllegalInputException(f"{chr(ord('x') + (i % 3)).upper()}{i // 3 + 1}({check_input[i]})")

        #error check finished
        temp : int = self.numbers[z2][y2][x2]
        self.numbers[z2][y2][x2] = self.numbers[z1][y1][x1]
        self.numbers[z1][y1][x1] = temp
        
    
    def swap_num(self, n1: int, n2: int) -> None:
        if n1 < 0 or n1 > self.size ** 3:
            raise ex.IllegalInputException("n1")
        elif n2 < 0 or n2 > self.size ** 3:
            raise ex.IllegalInputException("n2")
        
        #error check finished
        v1 : int[3] = self.find_number(n1)
        v2 : int[3] = self.find_number(n2)
        self.swap_spot(v1[0],v1[1],v1[2],v2[0],v2[1],v2[2])
        
    def print(self) -> None:
        for y in range(self.size):
            for z in range(self.size):
                for x in range(self.size):
                    print(self.numbers[z][self.size - 1 - y][x],end = " ")
                print()
            print()
            
    def get(self,x:int,y:int,z:int) -> int:
        check_input : list[int] = [x,y,z]
        for i in range(3):
            if check_input[i] < 0 or check_input[i] >= self.size:
                raise ex.IllegalInputException(f"{chr(ord('x') + (i % 3)).upper()}")
        return self.numbers[z][y][x]
    
    def copy(self):
        new_cube : Magicube = Magicube(self.size)
        new_cube.numbers = copy.deepcopy(self.numbers)
        return new_cube
        #HERE
        
    def to_list(self):
        retval : list[int] = []
        for i in range(self.size**3):
            loc : Vector3 = generate_vector(i,self.size)
            retval += [self.get(loc.x,loc.y,loc.z)]
        return retval

def copy_cube(m1 : Magicube, m2 : Magicube):
    m1.size = m2.size
    m1.numbers = m2.numbers

true_example = [121,108,7,20,59,31,53,112,109,10,47,61,45,76,86,91,77,71,6,70,25,16,80,104,90,29,28,122,125,11,12,82,34,87,100,107,43,38,33,94,52,64,117,69,13,115,98,4,1,97,51,15,41,124,84,103,3,105,8,96,89,68,63,58,37,30,118,21,123,23,42,111,85,2,75,78,54,99,24,60,113,57,9,62,74,32,93,88,83,19,26,39,92,44,114,66,72,27,102,48,36,110,46,22,101,56,120,55,49,35,40,50,81,65,79,116,17,14,73,95,67,18,119,106,5]

#Magicube(custom=true_example).print()