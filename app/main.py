from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from .database import Base, engine, check_database_health
from .routers import register_user, login_user

# 1. Use lifespan for cleaner startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Run DB setup here
    print("Starting up: Creating database tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
        # Note: Depending on your needs, you might want to stop the app if DB fails
    yield
    # Shutdown logic (e.g., close connections)
    print("Shutting down...")

Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=lifespan)

@app.get('/health', status_code=status.HTTP_200_OK)
def health():
    # Return a dict, not an Exception
    is_db_ok = check_database_health()
    return {
        "status": "healthy" if is_db_ok else "degraded",
        "detail": "API is healthy and running."
    }


app.include_router(register_user.router)
app.include_router(login_user.router)