"""Simple verification that new fields exist in the database"""
from app.database import users_collection

print("Checking database for new streak fields...")
print("=" * 60)

# Get a sample user
user = users_collection.find_one()

if user:
    print(f"Sample user: {user.get('username', 'Unknown')}")
    print(f"  current_streak: {user.get('current_streak', 'MISSING')}")
    print(f"  longest_streak: {user.get('longest_streak', 'MISSING')}")
    print(f"  regular_streaks: {user.get('regular_streaks', 'MISSING')}")
    print(f"  counting_streaks: {user.get('counting_streaks', 'MISSING')}")
    
    if 'regular_streaks' in user and 'counting_streaks' in user:
        print("\n[SUCCESS] All streak fields are present in the database!")
    else:
        print("\n[ERROR] Some fields are missing!")
else:
    print("No users found in database")

print("=" * 60)
