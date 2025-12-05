# --- check_daily_tasks.py ---
from database import DAILY_QUESTS, ACTIVITY_LOG 
from datetime import date, datetime
from typing import Optional

def check_daily_tasks(user_id: int) -> Optional[dict]:
    """
    Simulates the DB Trigger function: checks the Activity_Log against the 
    assigned Daily_Quests for a user and updates the status if 5 tasks are found.
    """
    today = date.today().isoformat()
    
    # 1. Retrieve the user's active quest for today
    quest_filter = {"user_id": user_id, "quest_date": today, "status": "Pending"}
    current_quest = DAILY_QUESTS.find_one(quest_filter)
    
    if not current_quest:
        # User either has no quest or has already completed it.
        return None

    assigned_tasks = current_quest.get("tasks_list", [])
    
    # 2. Query the Activity_Log for today's completed tasks
    log_filter = {
        "user_id": user_id,
        "activity_name": {"$in": assigned_tasks}, # Check only tasks that were assigned
        "log_date": today
    }
    
    # Use aggregation/distinct to count how many *unique assigned tasks* have been logged
    # We only care if the name is present, not how many times it was logged.
    completed_tasks = ACTIVITY_LOG.distinct("activity_name", log_filter)
    
    tasks_completed_count = len(completed_tasks)
    
    print(f"User {user_id} has completed {tasks_completed_count} unique tasks today.")

    # 3. Check for completion and update quest status
    if tasks_completed_count >= 5:
        # A full quest is completed!
        reward_lp = current_quest.get("quest_reward_lp", 10) # Default to 10 LP
        
        # Update the quest status to 'Complete'
        DAILY_QUESTS.update_one(
            {"_id": current_quest["_id"]},
            {"$set": {"status": "Complete", "completion_time": datetime.utcnow()}}
        )
        
        return {
            "status": "QUEST_COMPLETE",
            "message": f"Congratulations! You completed the quest and earned {reward_lp} LP!",
            "reward": reward_lp
        }
    
    return {
        "status": "IN_PROGRESS",
        "completed": tasks_completed_count,
        "remaining": 5 - tasks_completed_count
    }