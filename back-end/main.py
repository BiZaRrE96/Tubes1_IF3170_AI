from fastapi import FastAPI
from algorithm.magicube import Magicube
from algorithm.magicube_utils import into_list
from algorithm.steepestascent import steep_ascent
from time import sleep

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#contoh request : http://127.0.0.1:8000/run/ALGONAME?var_A=69&var_B=69
#as far as i understand, you dont need more than 2 variables
@app.get("/run/{algo_name}")
async def run_algo(algo_name : str):
    #some return values
    retval : dict = {"status" : "Error", "message" : "Undefined"}
    start_cube : Magicube = None
    end_cube : Magicube = None

    #no required inputs    
    #return value of dict {"cube","iteration","context"}
    if (algo_name == "steepest_accent"):
        pass
        start_cube = Magicube()
        result = steep_ascent(5,start_cube)
        end_cube = result["cube"]
        #on success
        if (retval != None):
            retval["status"] = "Success"
            retval["message"] = result["context"]
        else:
            retval["status"] = "Failure"
    
    #require ??? im not sure
    elif (algo_name == "simulated_annealing"):
        pass
    
    #require population_size and max_itteration
    # var_A = pop size
    # var_B = max_itteration
    elif (algo_name == "genetic_algprothm"):
        pass
        retval["status"] = "Success"
    
    #for simplicity reasons, magicube sebaiknya direturn sebagai satu list panjang urut dari x0y0z0 Hingga x4y4z4
    if (retval["status"] == "Success"):
        retval["start_cube"] = into_list(start_cube)
        retval["end_cube"] = into_list(end_cube)
    
    return retval

@app.get("/test")
async def testfunc():
    return {"message" : "balls"}

@app.get("/contoh_retval")
async def testfunc():
    return {"start_cube" : into_list(Magicube()), "status" : "test result"}