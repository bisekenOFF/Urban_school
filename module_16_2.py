#Переименуйте файл на main.py

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def general_page() -> str:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> str:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{username:str}/{age:int}")
async def user_page(username: str = Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')
                    , age: int = Path(ge=18, le=120, description="Enter age", example='24')) -> str:
    return {"message": f"Информация о пользователе. Имя: {username}. Возраст: {age}"}


@app.get("/user/{user_id}")
async def user_page(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1')) -> str:
    return {"message": f"Вы вошли как пользователь №{user_id}"}

