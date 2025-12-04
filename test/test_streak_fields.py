"""
Test script to verify the new streak tracking fields
"""
import requests
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8000"

def test_streak_tracking():
    """Test the new regular_streaks and counting_streaks fields"""
    
    # 1. Register a test user
    print("1. Registering test user...")
    register_data = {
        "username": "streak_tester",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/register", json=register_data)
        if response.status_code == 200:
            print("[OK] User registered successfully")
            user_data = response.json()
            print(f"  Initial data: {user_data}")
        elif response.status_code == 400:
            print("[WARN] User already exists, continuing with login...")
        else:
            print(f"[ERROR] Registration failed: {response.text}")
            return
    except Exception as e:
        print(f"[ERROR] Error during registration: {e}")
        return
    
    # 2. Login to get token
    print("\n2. Logging in...")
    login_data = {
        "username": "streak_tester",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/token",
            data=login_data
        )
        if response.status_code == 200:
            token = response.json()["access_token"]
            print("[OK] Login successful")
        else:
            print(f"[ERROR] Login failed: {response.text}")
            return
    except Exception as e:
        print(f"[ERROR] Error during login: {e}")
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Get current user data
    print("\n3. Fetching user data...")
    try:
        response = requests.get(f"{BASE_URL}/api/user/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print("[OK] User data retrieved:")
            print(f"  Username: {user_data['username']}")
            print(f"  Current Streak: {user_data['current_streak']}")
            print(f"  Longest Streak: {user_data['longest_streak']}")
            print(f"  Regular Streaks: {user_data.get('regular_streaks', 'NOT FOUND')}")
            print(f"  Counting Streaks: {user_data.get('counting_streaks', 'NOT FOUND')}")
        else:
            print(f"[ERROR] Failed to get user data: {response.text}")
            return
    except Exception as e:
        print(f"[ERROR] Error fetching user data: {e}")
        return
    
    # 4. Simulate check-ins to reach milestones
    print("\n4. Simulating check-ins to test milestone tracking...")
    today = date.today()
    
    for i in range(8):  # Check in for 8 days to hit 3-day and 7-day milestones
        checkin_date = today - timedelta(days=7-i)
        checkin_data = {"local_date": checkin_date.isoformat()}
        
        try:
            response = requests.post(
                f"{BASE_URL}/api/checkin",
                json=checkin_data,
                headers=headers
            )
            if response.status_code == 200:
                user_data = response.json()
                print(f"  Day {i+1} check-in: Streak = {user_data['current_streak']}")
                if user_data.get('regular_streaks'):
                    print(f"    Milestones: {user_data['regular_streaks']}")
                    print(f"    Total milestone count: {user_data.get('counting_streaks', 0)}")
            else:
                print(f"  [ERROR] Check-in failed: {response.text}")
        except Exception as e:
            print(f"  [ERROR] Error during check-in: {e}")
    
    # 5. Final user data
    print("\n5. Final user data after check-ins:")
    try:
        response = requests.get(f"{BASE_URL}/api/user/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print("[OK] Final stats:")
            print(f"  Current Streak: {user_data['current_streak']}")
            print(f"  Longest Streak: {user_data['longest_streak']}")
            print(f"  Regular Streaks: {user_data.get('regular_streaks', {})}")
            print(f"  Counting Streaks: {user_data.get('counting_streaks', 0)}")
            
            # Verify the new fields exist
            if 'regular_streaks' in user_data and 'counting_streaks' in user_data:
                print("\n[SUCCESS] New streak tracking fields are working correctly!")
            else:
                print("\n[FAILED] New fields are missing from the response!")
        else:
            print(f"[ERROR] Failed to get final user data: {response.text}")
    except Exception as e:
        print(f"[ERROR] Error fetching final user data: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("Testing New Streak Tracking Fields")
    print("=" * 60)
    test_streak_tracking()
    print("\n" + "=" * 60)
