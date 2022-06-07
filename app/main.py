from fastapi import FastAPI

from app.api.solve import solve_router


def start_app() -> FastAPI:
    app = FastAPI(
        title="The Quadratic Equation",
        version="0.1",
        description="A service that solves quadratic equations."
    )
    app.include_router(solve_router)
    return app
    
app = start_app()