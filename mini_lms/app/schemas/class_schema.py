from pydantic import BaseModel, Field, conint
from datetime import time
from typing import List, Optional

class ClassBase(BaseModel):
    name: str = Field(..., min_length=2)
    subject: str
    day_of_week: conint(ge=2, le=8)  # 2: Thứ 2, 8: Chủ nhật
    time_slot: time
    teacher_name: str
    max_students: int = Field(20, ge=1)

class ClassCreate(ClassBase):
    pass

class ClassResponse(ClassBase):
    id: int

    class Config:
        from_attributes = True