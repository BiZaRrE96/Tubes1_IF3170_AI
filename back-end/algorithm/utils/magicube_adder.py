from statistics import stdev
import time
import magicube as m
import traversal as t
import threading

def fitness(cube: m.Magicube) -> float:
    paths : list[t.Path] = []
    value : list[int] = []
    for direction in t.judgement_vectors:
        paths = paths + t.traversal(direction,cube.size)
    for path in paths:
        temp : int = 0
        for vector in path.list():
            temp += cube.get(vector.x,vector.y,vector.z)
        value += [temp]
    return -stdev(value)

def deviation(cube: m.Magicube) -> float:
    total_deviation: float = 0
    magic_number: float = 315

    # Menghitung penyimpangan untuk setiap baris
    for x in range(cube.size):
        for y in range(cube.size):
            sum_row = sum(cube.get(x, y, z) for z in range(cube.size))
            deviation = abs(sum_row - magic_number)
            total_deviation += deviation

    # Menghitung penyimpangan untuk setiap kolom
    for y in range(cube.size):
        for z in range(cube.size):
            sum_column = sum(cube.get(x, y, z) for x in range(cube.size))
            deviation = abs(sum_column - magic_number)
            total_deviation += deviation

    # Menghitung penyimpangan untuk setiap tiang
    for x in range(cube.size):
        for z in range(cube.size):
            sum_pillar = sum(cube.get(x, y, z) for y in range(cube.size))
            deviation = abs(sum_pillar - magic_number)
            total_deviation += deviation

    # Menghitung penyimpangan untuk setiap diagonal
    # Diagonal dari sudut kiri atas ke kanan bawah
    sum_diag1 = sum(cube.get(i, i, i) for i in range(cube.size))
    deviation1 = abs(sum_diag1 - magic_number)
    total_deviation += deviation1

    # Diagonal dari sudut kiri bawah ke kanan atas
    sum_diag2 = sum(cube.get(i, i, cube.size - i - 1) for i in range(cube.size))
    deviation2 = abs(sum_diag2 - magic_number)
    total_deviation += deviation2

    return total_deviation

finish : bool = False

def bogo_search(size : int) -> None:
    global finish
    
    cube: m.Magicube
    #test
    if size == 69:
        cube = m.Magicube(custom=m.true_example)
    else:
        cube = m.Magicube(size)
        
    if fitness(cube) >= -50:
        if not finish:
            cube.print()
            print("FINISH!")
            print(fitness(cube))
            finish = True
    return

def bogo_supersearch(n : int):
    ix : int = 0
    clock : float = 0
    while not finish:
        t1 = threading.Thread(target=bogo_search,args=(n,))
        t2 = threading.Thread(target=bogo_search,args=(n,))
        t3 = threading.Thread(target=bogo_search,args=(n,))
        t4 = threading.Thread(target=bogo_search,args=(n,))
        
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        
        clock += time.process_time()
        ix += 1
        
        if (clock // 1000 > 0):
            print("loop",ix)
            clock = clock % 1000

#bogo_supersearch(5)