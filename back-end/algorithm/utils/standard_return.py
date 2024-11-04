from .Magicubev2 import Magicube2 as Magicube

def standard_return(first_cube : Magicube, end_cube : Magicube, value_graph : list[float], log : str, exec_time : float):
    return {"first" :   {
                        "cube" : first_cube.to_list(),
                        "value" : first_cube.get_fitness()
                        },
            "end" :     {
                        "cube" : end_cube.to_list(),
                        "value" : end_cube.get_fitness()
                        },
            "graph" : value_graph,
            "log" : log,
            "time" : exec_time}