from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
import random

from algorithm.utils.magicube import generate_n_stack
from algorithm.steepestascent import steepestascent
from algorithm.stocastic import stocastic
from algorithm.sidewaysmove import sidewaysmove
from algorithm.randomrestart import randomrestart

app = FastAPI()

# Define models for the JSON body structure
class SidewaysRequest(BaseModel):
    cube: List[int]
    max_iteration: Optional[int] = None
    max_sidewaysmove: Optional[int] = None

class RandomStartRequest(BaseModel):
    cube: List[int]
    max_iteration: Optional[int] = None
    max_restarts: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate-cube")
async def generate_cube(n: int, straight: Optional[bool] = False):
    result = generate_n_stack(n, straight)
    return result

@app.post("/steepest-ascent-hill-climbing")
async def steepest_ascent_hc(cube: List[int]):
    result = steepestascent(cube)
    return result

@app.post("/stochastic-hill-climbing")
async def stochastic_hc(cube: List[int]):
    result = stocastic(cube)
    return result

@app.post("/hill-climbing-with-sideways-move")
async def hc_with_sideways(request: SidewaysRequest):
    print("MAX SIDEWAYS MOVE:", request.max_sidewaysmove)
    result = sidewaysmove(request.cube, request.max_iteration, request.max_sidewaysmove)
    return result

@app.post("/random-start-hill-climbing")
async def random_start_hc(request: RandomStartRequest):
    print("MAX RESTARTS:", request.max_restarts)
    result = randomrestart(request.cube, request.max_iteration, request.max_restarts)
    return result









@app.get("/simulated-annealing")
async def simulated_annealing():
    return

@app.get("/genetic-algorithm")
async def genetic_algorithm():
    return