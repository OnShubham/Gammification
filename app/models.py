from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class User(BaseModel):
    """User model for MongoDB"""
    username: str
    hashed_password: str
    last_checkin_date: Optional[date] = None
    current_streak: int = 0
    longest_streak: int = 0

    class Config:
        json_encoders = {date: lambda v: v.isoformat() if v else None}
