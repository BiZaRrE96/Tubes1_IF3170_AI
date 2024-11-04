from fastapi import FastAPI
from typing import List, Optional
import random

from algorithm.utils.magicube import generate_n_stack
from algorithm.steepestascent import steepestascent
from algorithm.stocastic import stocastic

app = FastAPI()

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

@app.get("/hill-climbing-with-sideways-move")
async def hc_with_sideways():
    return

@app.get("/random-start-hill-climbing")
async def random_start_hc():
    return

@app.get("/simulated-annealing")
async def simulated_annealing():
    return

@app.get("/genetic-algorithm")
async def genetic_algorithm():
    return