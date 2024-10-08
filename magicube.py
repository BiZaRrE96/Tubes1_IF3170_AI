import random
import exceptions as ex

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

#XYZ
judgement_vectors : list[list[int]] = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,0,1],[0,1,1],[1,-1,0],[1,0,-1],[0,-1,1],[1,1,1][-1,1,1][1,-1,1][-1,-1,1]]

#X < > (Kiri kanan); Y /\ \/ (atas bawah); Z (+) (-) (depan belakang)
#therefore Magicube.numbers[Z][Y][X]

#X 0 -> +; Y /\ +; Z ke arah kita positif

class Magicube:
    def __init__(self, cube_size : int = 5, straight = False) -> None:
        #define cube size (n^3)
        self.size : int = cube_size
        
        #generate random state
        self.numbers : list[list[list[int]]] = []
        
        #populate cube
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
                raise ex.IllegalInputException(i)

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
            
# test
test : Magicube = Magicube(5, True)
try:
    test.print()
    test.swap_num(2,125)
    print("SWAP")
    test.print()
    pass
except ex.IllegalInputException as e:
    print(e.description)