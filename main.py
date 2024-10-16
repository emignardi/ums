from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import uvicorn
import models
from models import User
from database import engine, SessionLocal

app = FastAPI(
    title="User Management System",
    description="A web application to manage users.",
    version="1.0.0",
    openapi_url="/openapi.json")

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

# Pydantic Validation (IDE Type Hints, Data Validation, Serialization)
class UserBase(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str

class UserUpdateBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

# Database Connection/Session Object *
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Page Routes
@app.get("/", tags=["Template"], summary="Home Page", description="This route returns the home page template.")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# JSON Routes
@app.get("/users", status_code=status.HTTP_200_OK, response_model=list[UserBase], tags=["User"], summary="Read All Users", description="Retrieve a list of users.")
def readAll(db: Session = Depends(get_db)) -> list[UserBase]:
    users = db.query(User).all()
    if users is not None:
        return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND) 
    
@app.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=UserBase, tags=["User"], summary="Read Single User", description="Retrieve a single user.")
def readById(id: int, db: Session = Depends(get_db)) -> UserBase:
    user = db.query(User).filter(User.id == id).first()
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID:{id} - Invalid ID")

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserBase, tags=["User"], summary="Create User", description="Create a new user.")
def create(user: UserBase, db: Session = Depends(get_db)) -> UserBase:
    newUser = models.User(**user.model_dump())
    db.add(newUser)
    db.commit()
    return newUser

@app.put("/users/{id}", status_code=status.HTTP_200_OK, response_model=UserBase, tags=["User"], summary="Update User", description="Update an existing user.")
def update(id: int, user: UserUpdateBase, db: Session = Depends(get_db)) -> UserBase:
    updatedUser = db.query(User).filter(User.id == id).first()
    if updatedUser is not None:
        updatedUser.first_name = user.first_name
        updatedUser.last_name = user.last_name
        updatedUser.email = user.email
        updatedUser.phone = user.phone
        updatedUser.address = user.address
        db.add(updatedUser)
        db.commit()
        return updatedUser
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID:{id} - Invalid ID")

@app.delete("/users/{id}", status_code=status.HTTP_200_OK, response_model=UserBase, tags=["User"], summary="Delete User", description="Delete an existing user.")
def delete(id: int, db: Session = Depends(get_db)) -> UserBase:
    user = db.query(User).filter(User.id == id).first()
    if user is not None:
        db.delete(user)
        db.commit()
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID:{id} - Invalid ID")
    
if __name__ == "__main__":
    uvicorn.run(app)