
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
    print(vector.list(),"*",factor)
    return Vector3([vector.x * factor, vector.y * factor, vector.z * factor])
    
def add_v(va : Vector3, vb : Vector3) -> Vector3:
    print(va.list(),"+",vb.list())
    return Vector3([va.x + vb.x,va.y + vb.y,va.z + vb.z])

#given an X,Y,Z vector generate a "path"
class Path:
    def __init__(self, pos: Vector3, dirr: Vector3) -> None:
        self.position = pos
        self.direction = dirr
    
    def list(self, length: int) -> list[Vector3]:
        retval : list[Vector3] = []
        for i in range(length):
            tempv: Vector3 = add_v(self.position,mult_v(self.direction,1+i))
            retval = retval + [tempv]
        return retval
            

#ASUME SIZE IS 3
#alt, legal pos finder
def traversal(vector : list[int], length : int) -> list[Vector3]:
    assert(len(vector) == 3)
    zeroes : list[bool] = [False, False, False] #menandakan 0 dimana aja
    retval: list[Vector3] = []
    
    if (vector.count(0) <= 2):
        #populate zeroes
        for i in range(3):
            if vector[i] == 0:
                zeroes[i] = True
        
        #begin
            
        pass
    else:
        pass
    