from fastapi import FastAPI
from app.routes import login_routes, profile_routes, hello

app = FastAPI()

app.include_router(login_routes.router)
app.include_router(profile_routes.router)
app.include_router(hello.router)

