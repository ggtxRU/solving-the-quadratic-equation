import math

from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_418_IM_A_TEAPOT

from app.models.pydantic import RequestSolveModel


solve_router = APIRouter()


@solve_router.post("/solve/", status_code=201, tags=["Solve"], description="Solving the quadratic equation..." )
async def solve(coefficients: RequestSolveModel):
    """Get discriminant."""
    dis = coefficients.b * coefficients.b - 4 * coefficients.a * coefficients.c
    sqrt_val = math.sqrt(abs(dis)) 
    if coefficients.a == 0:
        return JSONResponse(status_code=HTTP_418_IM_A_TEAPOT,
        content="Coefficient 'a' cannot be zero!")
    """Checking condition for discriminant."""
    if dis > 0: 

        response_object = {
            "x1": ((-coefficients.b + sqrt_val) / (2 * coefficients.a)) ,
            "x2": ((-coefficients.b - sqrt_val) / (2 * coefficients.a))
            }
        return response_object
    elif dis == 0: 
        response_object = {
            "x": (-coefficients.b / (2 * coefficients.a))  
        }
        return response_object
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
            content="The equation has no solutions")