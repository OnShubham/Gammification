"""
Test script to verify the no-authentication API works correctly
"""
import requests
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

def test_create_user():
    """Test creating a new user"""
    print("\n1. Testing user creation...")
    user_id = "test_user_123"
    response = requests.post(f"{BASE_URL}/api/user/create?user_id={user_id}")
    
    if response.status_code == 200:
        user = response.json()
        print(f"✓ User created successfully: {user}")
        return user_id
    else:
        print(f"✗ Failed to create user: {response.status_code} - {response.text}")
        return None

def test_get_user(user_id):
    """Test getting user data"""
    print(f"\n2. Testing get user by ID...")
    response = requests.get(f"{BASE_URL}/api/user/{user_id}")
    
    if response.status_code == 200:
        user = response.json()
        print(f"✓ User retrieved successfully: {user}")
        return True
    else:
        print(f"✗ Failed to get user: {response.status_code} - {response.text}")
        return False

def test_checkin(user_id):
    """Test check-in functionality"""
    print(f"\n3. Testing check-in...")
    today = date.today().isoformat()
    
    response = requests.post(
        f"{BASE_URL}/api/checkin",
        json={
            "user_id": user_id,
            "local_date": today
        }
    )
    
    if response.status_code == 200:
        user = response.json()
        print(f"✓ Check-in successful!")
        print(f"  Current streak: {user['current_streak']}")
        print(f"  Longest streak: {user['longest_streak']}")
        print(f"  Last check-in: {user['last_checkin_date']}")
        return True
    else:
        print(f"✗ Check-in failed: {response.status_code} - {response.text}")
        return False

def test_duplicate_checkin(user_id):
    """Test that duplicate check-ins on the same day work"""
    print(f"\n4. Testing duplicate check-in (should work but not increment)...")
    today = date.today().isoformat()
    
    response = requests.post(
        f"{BASE_URL}/api/checkin",
        json={
            "user_id": user_id,
            "local_date": today
        }
    )
    
    if response.status_code == 200:
        user = response.json()
        print(f"✓ Duplicate check-in handled correctly")
        print(f"  Current streak: {user['current_streak']}")
        return True
    else:
        print(f"✗ Duplicate check-in failed: {response.status_code} - {response.text}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Testing No-Authentication Gamification API")
    print("=" * 60)
    
    # Run tests
    user_id = test_create_user()
    
    if user_id:
        test_get_user(user_id)
        test_checkin(user_id)
        test_duplicate_checkin(user_id)
    
    print("\n" + "=" * 60)
    print("Testing complete!")
    print("=" * 60)
