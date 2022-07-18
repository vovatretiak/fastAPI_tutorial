from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException
from models import User, Gender, Roles, UserUpdateRequest

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


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user_id} does not exist'
    )


@app.put('/api/v1/users/{user_id}')
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user_id == user.id:
            if user_update.first_name:
                user.first_name = user_update.first_name
            if user_update.first_name:
                user.last_name = user_update.last_name
            if user_update.first_name:
                user.middle_name = user_update.middle_name
            if user_update.first_name:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user_id} does not exist'
    )

