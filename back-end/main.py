from fastapi import FastAPI
from typing import List, Optional
import random

from algorithm.utils.magicube import generate_n_stack

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate-cube")
async def generate_cube(n: int, straight: Optional[bool] = False):
    result = generate_n_stack(n, straight)
    return result

@app.get("/steepest-ascent-hill-climbing")
async def steepest_ascent_hc():
    return

@app.get("/stochastic-hill-climbing")
async def stochastic_hc():
    return

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