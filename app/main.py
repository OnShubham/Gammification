from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import models, schemas, crud


app = FastAPI(title="Streak Gamification App")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/user/create", response_model=schemas.UserResponse)
def create_or_get_user(user_id: str):
    """Create a new user or get existing user by user_id"""
    user = crud.get_user_by_id(user_id=user_id)
    if not user:
        user = crud.create_user(user_id=user_id)
    return user


@app.get("/api/user/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: str):
    """Get user data by user_id"""
    user = crud.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/api/checkin", response_model=schemas.UserResponse)
def check_in(request: schemas.CheckInRequest):
    """Check in for a user"""
    user = crud.get_user_by_id(user_id=request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user, message = crud.check_in(user, request.local_date)
    return user
