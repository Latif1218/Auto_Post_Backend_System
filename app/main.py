from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import SESSION_SECRET_KEY
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "http://localhost:3001",
#         "http://127.0.0.1:8000",
#         "https://fafaseleto-frontend.vercel.app",
#         "http://192.168.7.56:3000",
#         "https://nonprinting-featherlight-leatrice.ngrok-free.dev",
#         "http://127.0.0.1:5500",
#     ], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# app.add_middleware(
#     SessionMiddleware,
#     secret_key = SESSION_SECRET_KEY,
#     https_only = True,
#     same_site="lax"
# )


@app.get('/health', status_code=status.HTTP_200_OK)
def health():
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail="API is healthy and running correctly.",
        headers={"POSTULAE Healthcheack": "healthy"}
    )

