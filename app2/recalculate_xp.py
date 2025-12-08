from app2.database import ACTIVITY_LOG, USERS_COLLECTION
from app2.xp_system import get_xp_value, calculate_level_stats, XP_VALUES
from datetime import datetime

def recalculate_all_xp():
    print("Starting XP Recalculation...")
    
    # 1. Reset (local aggregation)
    user_xp_totals = {}
    
    # 2. Iterate all logs
    cursor = ACTIVITY_LOG.find({})
    count = 0
    for log in cursor:
        user_id = str(log.get("user_id"))
        activity_name = log.get("activity_name")
        
        xp = get_xp_value(activity_name)
        
        if user_id not in user_xp_totals:
            user_xp_totals[user_id] = 0
        
        user_xp_totals[user_id] += xp
        count += 1
        
    print(f"Processed {count} logs.")
    
    # 3. Update Users
    for user_id, total_xp in user_xp_totals.items():
        stats = calculate_level_stats(total_xp)
        
        update_data = {
            "total_xp": total_xp,
            "current_level": stats["current_level"],
            "xp_to_next_level": stats["xp_target_next_level"],
            "xp_progress": stats["xp_in_current_level"],
            "updated_at": datetime.utcnow()
        }
        
        USERS_COLLECTION.update_one(
            {"user_id": user_id},
            {"$set": update_data},
            upsert=True
        )
        print(f"Updated User {user_id}: Level {stats['current_level']} ({total_xp} XP)")

    print("Recalculation Complete.")

if __name__ == "__main__":
    recalculate_all_xp()
