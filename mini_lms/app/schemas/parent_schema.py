from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

# Schema dùng cho Input (Khi tạo mới)
class ParentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., pattern=r"^\+?1?\d{9,15}$") # Regex kiểm tra số điện thoại
    email: Optional[EmailStr] = None

# Schema dùng cho Output (Khi trả về cho client)
class ParentResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: Optional[EmailStr]

    class Config:
        from_attributes = True # Cho phép chuyển từ SQLAlchemy model sang Pydantic