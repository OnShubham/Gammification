from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class User(BaseModel):
    """User model for MongoDB"""
    username: str
    hashed_password: str
    last_checkin_date: Optional[date] = None
    current_streak: int = 1
    longest_streak: int = 1
    regular_streaks: dict = {}  # Track milestone achievements (e.g., {"7_day": 3, "30_day": 1})
    counting_streaks: int = 0  # Total count of all streak milestones achieved

    class Config:
        json_encoders = {date: lambda v: v.isoformat() if v else None}
