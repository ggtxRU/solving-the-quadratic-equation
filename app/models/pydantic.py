from typing import Optional
from pydantic import BaseModel


class RequestSolveModel(BaseModel):
    a: int
    b: int
    c: int