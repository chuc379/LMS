from pydantic import BaseModel
from datetime import datetime

class RegistrationCreate(BaseModel):
    student_id: int

class RegistrationResponse(BaseModel):
    id: int
    class_id: int
    student_id: int
    registration_date: datetime

    class Config:
        from_attributes = True