# Gamification App - No Authentication Version

## Overview
This is a simplified version of the gamification app with **authentication removed**. Users can now track their streaks using just a simple User ID - no passwords, no login required!

## What Changed?

### Backend Changes
1. **Removed Authentication System**
   - No more JWT tokens
   - No more OAuth2
   - No more password hashing
   - Removed `auth.py` dependency

2. **Simplified User Model**
   - Changed from `username` + `hashed_password` to just `user_id`
   - Users are identified by a simple string ID

3. **Updated API Endpoints**
   - `POST /api/user/create?user_id=<id>` - Create or get a user
   - `GET /api/user/{user_id}` - Get user data
   - `POST /api/checkin` - Check in (now requires `user_id` in request body)

### Frontend Changes
1. **Removed Login/Register Forms**
   - Simple "Enter User ID" input instead
   - No password fields

2. **Simplified User Flow**
   - Enter any User ID → Start tracking streaks
   - User ID stored in localStorage
   - Auto check-in on page load

## API Usage

### Create or Get User
```bash
curl -X POST "http://127.0.0.1:8000/api/user/create?user_id=john123"
```

Response:
```json
{
  "user_id": "john123",
  "last_checkin_date": null,
  "current_streak": 0,
  "longest_streak": 0,
  "regular_streaks": {},
  "counting_streaks": 0
}
```

### Get User Data
```bash
curl "http://127.0.0.1:8000/api/user/john123"
```

### Check In
```bash
curl -X POST "http://127.0.0.1:8000/api/checkin" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "john123",
    "local_date": "2025-12-08"
  }'
```

## Running the App

1. **Start the server:**
   ```bash
   cd c:\Shubham\Office\Gammification
   .venv\Scripts\activate
   uvicorn app.main:app --reload
   ```

2. **Open in browser:**
   ```
   http://127.0.0.1:8000
   ```

3. **Enter any User ID and start tracking!**

## Testing

Run the test script to verify everything works:
```bash
python test_no_auth.py
```

## Integration with Other Apps

Since there's no authentication, other apps can easily integrate by:

1. **Creating/Getting a user:**
   ```python
   import requests
   
   response = requests.post(
       "http://127.0.0.1:8000/api/user/create?user_id=user123"
   )
   user = response.json()
   ```

2. **Triggering a check-in:**
   ```python
   from datetime import date
   
   response = requests.post(
       "http://127.0.0.1:8000/api/checkin",
       json={
           "user_id": "user123",
           "local_date": date.today().isoformat()
       }
   )
   updated_user = response.json()
   ```

## Features Retained
- ✅ Streak tracking (current & longest)
- ✅ Milestone achievements (3, 7, 14, 30, 60, 90, 180, 365 days)
- ✅ Total milestone counter
- ✅ Beautiful UI with glassmorphism
- ✅ Auto check-in on page load
- ✅ MongoDB persistence

## Security Note
⚠️ **This version has NO authentication!** Anyone with a user_id can:
- View that user's data
- Update that user's streaks

This is intentional for easy integration with other apps. If you need security, consider:
- Adding API keys
- Implementing proper authentication
- Using the original authenticated version

## Files Modified
- `app/main.py` - Removed auth, simplified endpoints
- `app/models.py` - Changed to user_id
- `app/schemas.py` - Removed auth schemas
- `app/crud.py` - Updated to use user_id
- `app/templates/index.html` - Removed login/register forms
- `app/static/script.js` - Removed auth logic

## Migration from Authenticated Version

If you have existing users in the database with `username` and `hashed_password`, you'll need to migrate them:

```python
# Migration script (run once)
from app.database import users_collection

# Update all existing users
users_collection.update_many(
    {},
    {
        "$rename": {"username": "user_id"},
        "$unset": {"hashed_password": ""}
    }
)
```

Or start fresh with a new database collection.
