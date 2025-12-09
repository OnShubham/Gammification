import math
from datetime import datetime
from app2.Master_Activities import GROUP_1, GROUP_2, GROUP_3, GROUP_4, GROUP_5
from app2.database import USERS_COLLECTION


# 1 Activity = 10 XP.
FIXED_XP_PER_ACTIVITY = 10

def get_xp_value(activity_name: str) -> int:
    """Returns the XP value for a given activity (Fixed)."""
    return FIXED_XP_PER_ACTIVITY

def calculate_level_stats(total_xp: int):
    """
    Calculates level, xp in current level, and xp target for next level using a SIMPLE ARITHMETIC (Linear) formula.
    
    Formula: Level = (Total XP / 100) + 1
    Meaning: Every 100 XP (10 Activities) = 1 Level.
    """
    if total_xp < 0: total_xp = 0
    
    XP_PER_LEVEL = 100
    
    # Linear calculation
    # 0-99 XP -> Level 1
    # 100-199 XP -> Level 2
    level = (total_xp // XP_PER_LEVEL) + 1
    
    # XP required to reach the start of current level
    base_xp_current = (level - 1) * XP_PER_LEVEL
    
    # XP required to reach the next level
    target_xp_next = level * XP_PER_LEVEL
    
    xp_in_current_level = total_xp - base_xp_current
    
    return {
        "current_level": level,
        "xp_in_current_level": xp_in_current_level,
        "xp_target_next_level": target_xp_next,
        "xp_progress_percent": round((xp_in_current_level / XP_PER_LEVEL) * 100, 2)
    }

from datetime import date
from app2.database import USERS_COLLECTION, ACTIVITY_LOG

def process_user_activity_xp(user_id: int, activity_name: str):
    """
    Updates the user's XP based on the activity. 
    This should be called whenever an activity is logged.
    """
    # 0. Abuse Prevention / Cap
    # Check how many times this activity was logged today by this user
    today = date.today().isoformat()
    daily_count = ACTIVITY_LOG.count_documents({
        "user_id": user_id,
        "activity_name": activity_name,
        "log_date": today
    })
    
    # If this is the Nth time, and N > Limit, give 0 XP.
    # Note: simple cap. Better logic would use specific limits per activity.
    DAILY_LIMIT = 10 
    if daily_count > DAILY_LIMIT:
        print(f"User {user_id}: XP Cap reached for {activity_name} today.")
        return {
            "xp_gained": 0,
            "reason": "daily_cap_reached"
        }

    xp_gained = get_xp_value(activity_name)
    
    # 1. Fetch User (Assuming user_id is string in DB, but passed as int/str. Handle both)
    # The 'app' uses user_id as string usually. But 'app2' ActivityLog uses int?
    # app2 main.py: user_id: int.
    # app models.py: user_id: str.
    # We need to ensure type consistency. 'app' creates users.
    # Let's try to query with string version of user_id if int fails or just string.
    
    user = USERS_COLLECTION.find_one({"user_id": str(user_id)})
    if not user:
        # If user doesn't exist in USERS collection (maybe only tracked in app2?), 
        # we might need to create a stub or skip.
        # For now, let's assume existence or create if needed (or just error/log).
        print(f"User {user_id} not found in Gammification DB. Creating stub.")
        user = {
            "user_id": str(user_id),
            "total_xp": 0,
            "current_level": 1
        }
    
    current_total = user.get("total_xp", 0)
    new_total = current_total + xp_gained
    
    stats = calculate_level_stats(new_total)
    
    update_data = {
        "total_xp": new_total,
        "current_level": stats["current_level"],
        "xp_to_next_level": stats["xp_target_next_level"], # Mapping from model field name
        "xp_progress": stats["xp_in_current_level"],
        "updated_at": datetime.utcnow()
    }
    
    USERS_COLLECTION.update_one(
        {"user_id": str(user_id)},
        {"$set": update_data},
        upsert=True
    )
    
    print(f"User {user_id}: +{xp_gained} XP. Total: {new_total}. Level: {stats['current_level']}")
    
    return {
        "xp_gained": xp_gained,
        "new_total_xp": new_total,
        "new_level": stats["current_level"],
        "stats": stats
    }
