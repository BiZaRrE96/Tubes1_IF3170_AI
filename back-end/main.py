from fastapi import FastAPI
from typing import List, Optional
import random

from .algorithm.magicube import generate_n_stack

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate-cube")
async def generate_cube(n: int, straight: Optional[bool] = False):
    result = generate_n_stack(n, straight)
    return {"numbers": result}