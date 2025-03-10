from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page():
    return 'Главная страница'


@app.get("/user/admin")
async def get_admin_page():
    return 'Вы вошли как админ'


@app.get("/user/{user_id}")
async def get_user_number(user_id: int = Path(ge=1, le=100, description='Enter User ID', examples=1)):
    return f'Вы вошли как пользователь №{user_id}'


@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')], age: int = Path(ge=18, le=100, description='Enter age', example=24)):
    return f'Информация о пользователе. Имя: {username},  Возраст: {age}'
