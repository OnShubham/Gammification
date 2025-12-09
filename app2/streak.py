from datetime import date, timedelta, datetime
from app2.database import USERS_COLLECTION

def update_streak(user_id: int):
    """
    Updates the user's streak based on activity logging.
    Logic mirrors app/crud.py to maintain consistency.
    """
    # Find user
    # Note: user_id in app/crud.py is str, but app2 seems to use int or match type.
    # In app/main.py: check_in(request: schemas.CheckInRequest) -> user_id
    # In app2/main.py: ActivityLog.user_id: int
    # We should handle both or cast to the type stored in DB.
    # Let's check what type is stored. app/crud.py create_user takes user_id: str.
    # But app2 ActivityLog says int.
    # We will try strictly querying. If app2 treats it as int, we cast to str if needed or query both?
    # Let's assume the DB stores what app2 gives if app2 is the source, OR that app1 initialized it as string.
    # Given app1 is "Streak Gamification App" and might be the legacy one, it uses Strings.
    # We should probably convert int to str for query if the DB has strings.
    
    # Let's inspect one user if possible later. For now, we'll try to support the ID passed.
    
    # Query: Try to find user.
    user = USERS_COLLECTION.find_one({"user_id": str(user_id)})
    if not user:
        # Fallback if stored as int
        user = USERS_COLLECTION.find_one({"user_id": user_id})
    
    if not user:
        # If user doesn't exist in the Gamification DB, we might need to create them?
        # For now, let's assume existence or return.
        print(f"Streak Update: User {user_id} not found in users collection.")
        return

    # Parse last_checkin_date
    last_checkin_date = user.get("last_checkin_date")
    # Mongo stores datetime usually. Pydantic logic in app/crud expects date.
    
    local_date = date.today()
    
    if isinstance(last_checkin_date, datetime):
        last_checkin_date = last_checkin_date.date()
    
    # Prepare update values
    current_streak = user.get("current_streak", 0)
    longest_streak = user.get("longest_streak", 0)
    regular_streaks = user.get("regular_streaks", {})
    counting_streaks = user.get("counting_streaks", 0)
    
    # If already checked in today, do nothing
    if last_checkin_date == local_date:
        return {"status": "Already updated today", "current_streak": current_streak}

    # Streak Logic
    if last_checkin_date == local_date - timedelta(days=1):
        current_streak += 1
    else:
        # Missed a day (or more), or first time
        current_streak = 1
    
    longest_streak = max(longest_streak, current_streak)
    
    # Milestones
    milestones = [3, 7, 14, 30, 60, 90, 180, 365]
    milestone_hit = None
    
    for milestone in milestones:
        if current_streak == milestone:
            milestone_key = f"{milestone}_day"
            regular_streaks[milestone_key] = regular_streaks.get(milestone_key, 0) + 1
            counting_streaks += 1
            milestone_hit = milestone
            break
            
    # Update DB
    new_checkin_dt = datetime.combine(local_date, datetime.min.time())
    
    USERS_COLLECTION.update_one(
        {"_id": user["_id"]},
        {
            "$set": {
                "last_checkin_date": new_checkin_dt,
                "current_streak": current_streak,
                "longest_streak": longest_streak,
                "regular_streaks": regular_streaks,
                "counting_streaks": counting_streaks
            }
        }
    )
    
    print(f"Streak updated for {user_id}. Current: {current_streak}")
    return {
        "status": "Streak updated",
        "current_streak": current_streak,
        "milestone_hit": milestone_hit
    }
