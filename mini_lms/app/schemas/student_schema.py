from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from .parent_schema import ParentResponse # Tái sử dụng schema đã viết

class StudentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    dob: Optional[date] = None
    gender: Optional[str] = Field(None, max_length=10)
    current_grade: Optional[int] = Field(None, ge=1, le=12)
    parent_id: int

class StudentCreate(StudentBase):
    """Dữ liệu nhận vào khi tạo học sinh"""
    pass

class StudentResponse(BaseModel):
    """Dữ liệu trả về cho Client (có thông tin Parent)"""
    id: int
    name: str
    dob: Optional[date]
    gender: Optional[str]
    current_grade: Optional[int]
    parent: Optional[ParentResponse] = None # Nested object

    class Config:
        from_attributes = True