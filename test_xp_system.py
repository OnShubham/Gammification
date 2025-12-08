import requests
import json

BASE_URL = "http://localhost:8001"

def test_log_activity_and_xp():
    user_id = 999
    # Ensure user exists or is created by the system? 
    # My code creates a stub in USERS_COLLECTION if missing.
    
    activity = "Hydration Hit" # 10 XP
    
    payload = {
        "user_id": user_id,
        "activity_name": activity
    }
    
    print(f"Logging activity: {activity} for User {user_id}")
    response = requests.post(f"{BASE_URL}/log_activity", json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("Success!")
        print(json.dumps(data, indent=2))
        
        xp_update = data.get("xp_update")
        if xp_update:
            print(f"XP Gained: {xp_update.get('xp_gained')}")
            print(f"Total XP: {xp_update.get('new_total_xp')}")
            print(f"Level: {xp_update.get('new_level')}")
        else:
            print("XP Update info missing!")
            
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_log_activity_and_xp()
