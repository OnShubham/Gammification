# API Reference - App2 Gamification

## Base URL
```
http://localhost:8001
```

## Endpoints

### 1. Frontend (HTML)
```http
GET /
```
**Description**: Serves the main frontend HTML page

**Response**: HTML page with full gamification interface

---

### 2. Get All Activities
```http
GET /api/activities
```
**Description**: Returns all available activities with descriptions

**Response**:
```json
{
  "activities": {
    "Hydration Hit": {
      "description": "Log a glass of water (Goal: 8/day)."
    },
    "AI Food Scan": {
      "description": "Snap a photo of your lunch to auto-calculate macros."
    },
    ...
  }
}
```

---

### 3. Assign Daily Quest
```http
POST /quests/{user_id}/assign
```
**Description**: Assigns 5 random tasks to the user for the day

**Parameters**:
- `user_id` (path): Integer - User identifier

**Response** (New Quest):
```json
{
  "message": "New daily quest assigned.",
  "quest": {
    "user_id": 1,
    "quest_date": "2024-12-08",
    "tasks": [
      {
        "name": "Hydration Hit",
        "description": "Log a glass of water (Goal: 8/day)."
      },
      ...
    ],
    "status": "Pending"
  }
}
```

**Response** (Quest Already Exists):
```json
{
  "message": "Quest already assigned for today.",
  "quest": {
    "user_id": 1,
    "quest_date": "2024-12-08",
    "tasks": [...],
    "status": "Pending"
  }
}
```

---

### 4. Get Quest Status
```http
GET /quests/{user_id}/status
```
**Description**: Retrieves current quest and progress for today

**Parameters**:
- `user_id` (path): Integer - User identifier

**Response** (Quest Found):
```json
{
  "quest_details": {
    "tasks": [
      {
        "name": "Hydration Hit",
        "description": "Log a glass of water (Goal: 8/day)."
      },
      ...
    ],
    "status": "Pending",
    "reward_lp": 10
  },
  "progress": {
    "status": "IN_PROGRESS",
    "completed": 3,
    "remaining": 2
  }
}
```

**Response** (Quest Complete):
```json
{
  "quest_details": {
    "tasks": [...],
    "status": "Complete",
    "reward_lp": 10
  },
  "progress": {
    "status": "QUEST_COMPLETE",
    "message": "Congratulations! Quest complete, earned 10 LP!",
    "reward": 10,
    "completed": 5,
    "remaining": 0
  }
}
```

**Response** (No Quest):
```json
{
  "message": "No quest found for today. Assign one first."
}
```

---

### 5. Log Activity
```http
POST /log_activity
```
**Description**: Logs a completed activity and updates XP, level, and quest progress

**Request Body**:
```json
{
  "user_id": 1,
  "activity_name": "Hydration Hit"
}
```

**Response** (Activity Logged):
```json
{
  "status": "Activity logged successfully.",
  "quest_status": {
    "status": "IN_PROGRESS",
    "completed": 1,
    "remaining": 4
  },
  "logged_activity": "Hydration Hit",
  "xp_update": {
    "xp_gained": 10,
    "new_total_xp": 10,
    "new_level": 1,
    "stats": {
      "current_level": 1,
      "xp_in_current_level": 10,
      "xp_target_next_level": 100,
      "xp_progress_percent": 10.0
    }
  }
}
```

**Response** (Quest Complete):
```json
{
  "status": "Activity logged successfully.",
  "quest_status": {
    "status": "QUEST_COMPLETE",
    "message": "Congratulations! Quest complete, earned 10 LP!",
    "reward": 10,
    "completed": 5,
    "remaining": 0
  },
  "logged_activity": "Doubt Buster",
  "xp_update": {
    "xp_gained": 10,
    "new_total_xp": 50,
    "new_level": 1,
    "stats": {
      "current_level": 1,
      "xp_in_current_level": 50,
      "xp_target_next_level": 100,
      "xp_progress_percent": 50.0
    }
  }
}
```

**Response** (Daily Cap Reached):
```json
{
  "status": "Activity logged successfully.",
  "quest_status": {...},
  "logged_activity": "Hydration Hit",
  "xp_update": {
    "xp_gained": 0,
    "reason": "daily_cap_reached"
  }
}
```

**Error Response** (Invalid Activity):
```json
{
  "detail": "Unknown activity name: Invalid Activity"
}
```

---

## Data Models

### ActivityLog (Request)
```typescript
{
  user_id: number;        // User identifier
  activity_name: string;  // Must match a key in MASTER_ACTIVITY_DATA
}
```

### Quest Assignment Logic
Each quest contains 5 tasks selected as follows:
1. **Slot 1**: Random from Group 1 (Daily Tracker)
2. **Slot 2**: Random from Group 4 (Action Taker)
3. **Slot 3**: Random from Group 3 (Quick View)
4. **Slot 4**: Random from Group 2 or 5 (Smart Scan or Core Focus)
5. **Slot 5**: Wildcard - Random from any remaining activity

### XP System
- **Fixed XP per activity**: 10 XP
- **Daily cap per activity**: 10 times
- **Level calculation**: Linear (100 XP per level)
  - Level = (Total XP / 100) + 1
  - Level 1: 0-99 XP
  - Level 2: 100-199 XP
  - Level 3: 200-299 XP

### Quest Completion
- **Requirement**: Complete 5 unique tasks in one day
- **Reward**: 10 LP (Loyalty Points)
- **Status**: Automatically updates from "Pending" to "Complete"

---

## Error Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 400 | Bad Request (invalid activity name) |
| 404 | Not Found (no quest found) |
| 500 | Internal Server Error |

---

## Usage Examples

### cURL Examples

**Assign Quest**:
```bash
curl -X POST http://localhost:8001/quests/1/assign
```

**Get Quest Status**:
```bash
curl http://localhost:8001/quests/1/status
```

**Log Activity**:
```bash
curl -X POST http://localhost:8001/log_activity \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "activity_name": "Hydration Hit"}'
```

**Get All Activities**:
```bash
curl http://localhost:8001/api/activities
```

### JavaScript Examples

**Assign Quest**:
```javascript
const response = await fetch('/quests/1/assign', {
  method: 'POST'
});
const data = await response.json();
console.log(data);
```

**Log Activity**:
```javascript
const response = await fetch('/log_activity', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    user_id: 1,
    activity_name: 'Hydration Hit'
  })
});
const data = await response.json();
console.log(data);
```

---

## Notes

1. **No Authentication**: This API does not require authentication
2. **User Management**: Users are identified by integer IDs
3. **Date Handling**: All dates use ISO format (YYYY-MM-DD)
4. **Timezone**: Server uses UTC for timestamps
5. **Quest Reset**: New quests can only be assigned once per day per user
6. **Activity Validation**: Activity names must exactly match keys in MASTER_ACTIVITY_DATA
7. **XP Cap**: Each activity can only grant XP 10 times per day per user

---

**Last Updated**: 2024-12-08
