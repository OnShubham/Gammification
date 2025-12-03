from . import models, schemas, auth
from .database import users_collection
from datetime import date, timedelta, datetime
from typing import Optional


def get_user_by_username(username: str) -> Optional[models.User]:
    """Get user by username from MongoDB"""
    user_data = users_collection.find_one({"username": username})
    if user_data:
        # Remove MongoDB's _id field before creating Pydantic model
        user_data.pop("_id", None)

        # Convert MongoDB datetime to date for the Pydantic model (if present)
        lcd = user_data.get("last_checkin_date")
        if lcd is not None:
            # lcd will be a datetime.datetime from Mongo
            user_data["last_checkin_date"] = lcd.date()

        return models.User(**user_data)
    return None


def create_user(user: schemas.UserCreate) -> models.User:
    """Create a new user in MongoDB"""
    hashed_password = auth.get_password_hash(user.password)
    user_data = {
        "username": user.username,
        "hashed_password": hashed_password,
        "last_checkin_date": None,  # stored as null initially
        "current_streak": 0,
        "longest_streak": 0,
    }

    # Insert into MongoDB
    users_collection.insert_one(user_data)

    # Remove _id for response (insert_one does not add _id to user_data, but safe)
    user_data.pop("_id", None)

    # Pydantic model expects last_checkin_date as date | None, so this is fine
    return models.User(**user_data)


def check_in(user: models.User, local_date: date) -> tuple[models.User, str]:
    """Handle user check-in and update streak"""

    # Check if already checked in today
    if user.last_checkin_date == local_date:
        return user, "Already checked in today!"

    # Update streak logic
    if user.last_checkin_date == local_date - timedelta(days=1):
        user.current_streak += 1
    else:
        user.current_streak = 1

    user.last_checkin_date = local_date
    user.longest_streak = max(user.longest_streak, user.current_streak)

    # Convert date -> datetime for MongoDB storage
    mongo_last_checkin = datetime.combine(local_date, datetime.min.time())

    # Update in MongoDB
    users_collection.update_one(
        {"username": user.username},
        {
            "$set": {
                "last_checkin_date": mongo_last_checkin,
                "current_streak": user.current_streak,
                "longest_streak": user.longest_streak,
            }
        },
    )

    return user, "Streak updated!"
