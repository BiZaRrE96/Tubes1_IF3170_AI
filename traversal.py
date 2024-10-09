
class Vector3:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.z = 0
    
    def __init__(self, vector: list[int]) -> None:
        length = len(vector)
        self.x = 0
        self.y = 0
        self.z = 0
        if length >= 1:
            self.x = vector[0]
        if length >= 2:
            self.y = vector[1]
        if length > 2:
            self.z = vector[2] 
    
    def list(self) -> list[int]:
        return [self.x,self.y,self.z]

def mult_v(vector: Vector3, factor: int) -> Vector3:
    #print(vector.list(),"*",factor)
    return Vector3([vector.x * factor, vector.y * factor, vector.z * factor])
    
def add_v(va : Vector3, vb : Vector3) -> Vector3:
    #print(va.list(),"+",vb.list())
    return Vector3([va.x + vb.x,va.y + vb.y,va.z + vb.z])


#given an X,Y,Z vector generate a "path"
class Path:
    def __init__(self, pos: Vector3, dirr: Vector3, length: int) -> None:
        self.position : Vector3 = pos
        self.direction : Vector3 = dirr
        self.length : int = length
    
    def list(self) -> list[Vector3]:
        retval : list[Vector3] = []
        for i in range(self.length):
            tempv: Vector3 = add_v(self.position,mult_v(self.direction,i))
            retval = retval + [tempv]
        return retval
            
#XYZ
judgement_vectors : list[list[int]] = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,0,1],[0,1,1],[1,-1,0],[1,0,-1],[0,-1,1],[1,1,1],[-1,1,1],[1,-1,1],[-1,-1,1]]

#ASUME SIZE IS 3
#alt, legal pos finder
def traversal(vector : list[int], length : int) -> list[Path]:
    assert(len(vector) == 3)
    zeroes : list[bool] = [False, False, False] #menandakan 0 dimana aja
    starts : list[list[int]]
    
    #Define starting area for pulling paths based on vector
    #In general, poisitve vectors need to start from near side, negative vector need to start from farside
    #ignore zeroes
    start_pos : list[int] = [0,0,0]
    for i in range(3):
        if vector[i] < 0:
            start_pos[i] = length-1
    
    starts = [start_pos]
    
    if (vector.count(0) <= 2):
        #populate zeroes
        for i in range(3):
            if vector[i] == 0:
                zeroes[i] = True
        #begin
        while (zeroes.count(True) > 0):
            temp: list[list[int]] = starts
            starts = []
            for value in temp:
                for i in range(length):
                    temp_insert = [value[0],value[1],value[2]]
                    temp_insert[zeroes.index(True)] += i
                    starts = starts + [temp_insert]
                pass
            zeroes[zeroes.index(True)] = False
        pass
    
    else:
        pass
    
    return [Path(Vector3(value),Vector3(vector),length) for value in starts]
    #return retval
    
