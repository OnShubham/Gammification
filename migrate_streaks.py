"""
Migration script to add regular_streaks and counting_streaks fields to existing users
"""
from app.database import users_collection

def migrate_users():
    """Add new streak tracking fields to existing users"""
    
    # Update all users that don't have the new fields
    result = users_collection.update_many(
        {
            "$or": [
                {"regular_streaks": {"$exists": False}},
                {"counting_streaks": {"$exists": False}}
            ]
        },
        {
            "$set": {
                "regular_streaks": {},
                "counting_streaks": 0
            }
        }
    )
    
    print(f"Migration completed!")
    print(f"Modified {result.modified_count} user(s)")
    print(f"Matched {result.matched_count} user(s)")

if __name__ == "__main__":
    migrate_users()
