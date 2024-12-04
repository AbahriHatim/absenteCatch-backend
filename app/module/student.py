from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    photo_path = Column(String, nullable=True)  
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    classroom = relationship("Class", back_populates="students")
