from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
import random

from algorithm.utils.magicube import generate_n_stack
from algorithm.steepestascent import steepestascent
from algorithm.stocastic import stocastic
from algorithm.sidewaysmove import sidewaysmove
from algorithm.randomrestart import randomrestart
from algorithm.simulated_annealing import simulated_annealing
from algorithm.genetic_evo_v2 import genetic_algorithm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define models for the JSON body structure
class GeneralRequest(BaseModel):
    cube: List[int]
class SidewaysRequest(BaseModel):
    cube: List[int]
    max_iteration: Optional[int] = None
    max_sidewaysmove: Optional[int] = None
class RandomStartRequest(BaseModel):
    cube: List[int]
    max_iteration: Optional[int] = None
    max_restarts: Optional[int] = None
class GeneticRequest(BaseModel):
    populasi: Optional[int] = None
    iterasi: Optional[int] = None

lastResponse: dict = {}
processdone: bool = False

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate-cube")
async def generate_cube(n: int, straight: Optional[bool] = False):
    result = generate_n_stack(n, straight)
    return result

# Steepest Ascent Hill Climbing
@app.post("/steepest-ascent-hill-climbing")
async def steepest_ascent_hc(request: GeneralRequest):
    # global lastResponse
    # global processdone
    # processdone = False
    result = steepestascent(request.cube)
    return result
    # lastResponse = result
    # processdone = True

@app.get("/steepest-ascent-hill-climbing")
async def get_steepest_ascent_hc():
    return lastResponse if processdone == True else {"Fuck off" : True}


# 
@app.post("/stochastic-hill-climbing")
async def stochastic_hc(request: GeneralRequest):
    result = stocastic(request.cube)
    return result

@app.post("/hill-climbing-with-sideways-move")
async def hc_with_sideways(request: SidewaysRequest):
    result = sidewaysmove(request.cube, request.max_iteration, request.max_sidewaysmove)
    return result

@app.post("/random-start-hill-climbing")
async def random_start_hc(request: RandomStartRequest):
    result = randomrestart(request.cube, request.max_iteration, request.max_restarts)
    return result

@app.post("/simulated-annealing")
async def simulated_annealing_api(request: GeneralRequest):
    result = simulated_annealing(request.cube)
    return result

@app.post("/genetic-algorithm")
async def genetic_algorithm_api(request: GeneticRequest):
    result = genetic_algorithm(request.populasi, request.iterasi, None)
    return result