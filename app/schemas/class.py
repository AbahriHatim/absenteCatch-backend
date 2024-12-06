from pydantic import BaseModel

class Class(BaseModel):
    id: int
    name: str
    teacher_id: int
