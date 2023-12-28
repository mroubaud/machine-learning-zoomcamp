from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello":"World"}

@app.get("/model/{my_name}")
def read_name(my_name: str, q: Optional[str]=None):
  return {"model description, sr": my_name, "q":q}