from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserResponse(BaseModel):
    user_id: str
    last_checkin_date: Optional[date]
    current_streak: int
    longest_streak: int
    regular_streaks: dict = {}
    counting_streaks: int = 0

    class Config:
        from_attributes = True

class CheckInRequest(BaseModel):
    user_id: str
    local_date: date
