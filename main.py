"""
"""
from fastapi import FastAPI

app = FastAPI()

# define root route
# (i.e. the home page, or "/")
@app.get("/")
async def root():
    return "Hello world!"