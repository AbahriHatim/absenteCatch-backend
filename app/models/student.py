from pydantic import BaseModel

class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    photo_path: str
    class_id: int