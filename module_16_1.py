#Переименуйте файл на main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{username:str}/{age:int}")
async def user_page(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}. Возраст: {age}"


@app.get("/user/{user_id}")
async def user_page(user_id: int) -> str:
    return f"Вы вошли как пользователь №{user_id}"


@app.get("/")
async def general_page() -> str:
    return "Главная страница"
