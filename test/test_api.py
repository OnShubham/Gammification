"""
Complete test of the gamification API with MongoDB
"""
import requests
from datetime import date
import json

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("🧪 Testing Gamification API with MongoDB\n")
    
    # Test 1: Register a new user
    print("1️⃣ Testing user registration...")
    register_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/register", json=register_data)
        if response.status_code == 200:
            print("✓ User registered successfully!")
            print(f"   Response: {response.json()}\n")
        else:
            print(f"✗ Registration failed: {response.status_code}")
            print(f"   Error: {response.text}\n")
            if response.status_code == 400:
                print("   (User might already exist - continuing with login...)\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")
        return
    
    # Test 2: Login
    print("2️⃣ Testing user login...")
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/token",
            data=login_data,  # OAuth2 uses form data, not JSON
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data["access_token"]
            print("✓ Login successful!")
            print(f"   Token: {access_token[:20]}...\n")
        else:
            print(f"✗ Login failed: {response.status_code}")
            print(f"   Error: {response.text}\n")
            return
    except Exception as e:
        print(f"✗ Error: {e}\n")
        return
    
    # Test 3: Get current user
    print("3️⃣ Testing get current user...")
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/api/user/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print("✓ User data retrieved!")
            print(f"   Username: {user_data['username']}")
            print(f"   Current Streak: {user_data['current_streak']}")
            print(f"   Longest Streak: {user_data['longest_streak']}\n")
        else:
            print(f"✗ Failed: {response.status_code}")
            print(f"   Error: {response.text}\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")
    
    # Test 4: Check-in
    print("4️⃣ Testing check-in...")
    checkin_data = {
        "local_date": str(date.today())
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/checkin",
            json=checkin_data,
            headers=headers
        )
        if response.status_code == 200:
            user_data = response.json()
            print("✓ Check-in successful!")
            print(f"   Current Streak: {user_data['current_streak']}")
            print(f"   Longest Streak: {user_data['longest_streak']}")
            print(f"   Last Check-in: {user_data['last_checkin_date']}\n")
        else:
            print(f"✗ Check-in failed: {response.status_code}")
            print(f"   Error: {response.text}\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")
    
    print("=" * 50)
    print("✅ All tests completed!")
    print("=" * 50)

if __name__ == "__main__":
    test_api()
