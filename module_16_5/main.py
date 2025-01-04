#Переименовать файл в main.py

from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi.templating import Jinja2Templates


class User(BaseModel):
    id: Optional[int] = None
    username: str
    age: int


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

users: List[User] = []


class UserCreate(BaseModel):
    username: str = Field(min_length=4, max_length=10, description='Имя пользователя')
    age: int = Field(ge=18, le=120, description='Возраст пользователя')


@app.get('/', response_class=HTMLResponse)
async def get_all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{user_id}', response_class=HTMLResponse)
async def update_user(user_id: int, request: Request):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User  not found")


@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/user/', response_model=User)
async def create_user(user_create: UserCreate):
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=user_create.username, age=user_create.age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}', response_model=User)
async def update_user(user_id: int, user_update: UserCreate):
    for user in users:
        if user.id == user_id:
            user.username = user_update.username
            user.age = user_update.age
            return user
    raise HTTPException(status_code=404, detail="User  not found")


@app.delete('/user/{user_id}', response_model=dict)
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": f"Deleted user {user_id}"}
    raise HTTPException(status_code=404, detail="User  not found")

#для запуска uvicorn main:app --reload
