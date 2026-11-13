from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import hashlib
import uuid

app = FastAPI()
users_db = {}

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    if any(u["email"] == user.email for u in users_db.values()):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = str(uuid.uuid4())
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    
    new_user = {
        "id": user_id,
        "username": user.username,
        "email": user.email,
        "password_hash": hashed_password
    }
    users_db[user_id] = new_user
    
    return {"id": user_id, "username": user.username, "email": user.email}
