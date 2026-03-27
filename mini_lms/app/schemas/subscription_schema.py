from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class SubscriptionBase(BaseModel):
    student_id: int
    package_name: str = Field(..., min_length=2)
    total_sessions: int = Field(..., gt=0)
    end_date: date

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionResponse(SubscriptionBase):
    id: int
    used_sessions: int

    class Config:
        from_attributes = True