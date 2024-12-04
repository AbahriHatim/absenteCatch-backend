from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    admin = 'admin'
    teacher = 'teacher'

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    role: UserRole