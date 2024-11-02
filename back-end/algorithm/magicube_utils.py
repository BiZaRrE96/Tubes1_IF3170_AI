from .magicube import Magicube

    # x = i % m1.size
    # y = i // (m1.size) % m1.size 
    # z = i // (m1.size**2)

def into_list(m : Magicube) -> list[int]:
    return [m.get(i % m.size, i // m.size % m.size, i // (m.size ** 2)) for i in range(m.size ** 3)]