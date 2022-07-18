from typing import List
from uuid import UUID

from fastapi import FastAPI
from models import User, Gender, Roles

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("1b9fa92e-9187-4632-95ab-b4ca3c1fa378"),
        first_name='Jane',
        last_name='Doe',
        gender=Gender.female,
        roles=[Roles.user]
    ),
    User(
        id=UUID("48707420-00ed-4853-8dec-2aaad93f3cc1"),
        first_name='Alex',
        last_name='Jones',
        gender=Gender.male,
        roles=[Roles.user, Roles.admin]
    )
]


@app.get('/')
async def root():
    return {"hello": "world"}


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}