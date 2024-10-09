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
    return stdev(value)

finish : bool = False

def bogo_search(size : int) -> None:
    global finish
    
    cube: m.Magicube
    #test
    if size == 69:
        cube = m.Magicube(custom=m.true_example)
    else:
        cube = m.Magicube(size)
        
    if fitness(cube) == 0:
        cube.print()
        print("FINISH!")
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
        
#print(fitness(m.Magicube(custom=m.true_example)))
bogo_supersearch(3)