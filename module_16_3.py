#Переименуйте файл на main.py

from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя:Exaple, возраст:18'}


@app.get('/users')
def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
def create_user(username: str = Path(min_length=4, max_length=10, description='Имя пользователя', example='Ivan')
                , age: int = Path(ge=18, le=120, description='Возраст пользователя', example=18)) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя:{username}, возраст:{age}'
    return f"User {current_index} is regitered"


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int = Path(ge=1, le=100, description='Идентификатор пользователя', example=1)
                , username: str = Path(min_length=4, max_length=10, description='Имя пользователя', example='Ivan')
                , age: int = Path(ge=18, le=120, description='Возраст пользователя', example=18)) -> str:
    users[user_id] = f'Имя:{username}, возраст:{age}'
    return f"User {user_id} is updated"


@app.delete('/user/{user_id}')
def delete_user(user_id: int) -> str:
    users.pop(str(user_id))
    return f"User {user_id} is deleted"
