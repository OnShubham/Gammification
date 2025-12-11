# API Documentation

This document outlines the API endpoints available for the Gamification 

## Base URL
`http://127.0.0.1:8001`

---

## 1. Assign Daily Quest

**Endpoint:** `POST /quests/{user_id}/assign`

**Description:**
Generates and assigns a new set of daily tasks (a "quest") for the specified user. If a quest already exists for the day, it may return the existing one.

**Path Parameters:**
- `user_id` (integer): The ID of the user.

**Response Example:**

```json
{
    "message": "New daily quest assigned.",
    "quest": {
        "user_id": 999,
        "quest_date": "2025-12-11",
        "tasks": [
            {
                "name": "Fruit Snap",
                "description": "Log eating one piece of fruit."
            },
            {
                "name": "New Move",
                "description": "Try a new exercise suggested by the 'Athlete Workout' module."
            },
            {
                "name": "Allergy Check",
                "description": "Review or update your 'Suitability Profile' (allergies/conditions)."
            },
            {
                "name": "Sugar Watch",
                "description": "Stay below your recommended sugar limit for the day."
            },
            {
                "name": "Step Up",
                "description": "Log your daily step count (or sync it)."
            }
        ],
        "status": "Pending"
    }
}
```

---

## 2. Get Quest Status

**Endpoint:** `GET /quests/{user_id}/status`

**Description:**
Retrieves the detailed status of the user's current daily quest, including task lists, progress, and current streak information.

**Path Parameters:**
- `user_id` (integer): The ID of the user.

**Response Example:**

```json
{
    "quest_details": {
        "tasks": [
            {
                "name": "Fruit Snap",
                "description": "Log eating one piece of fruit."
            },
            {
                "name": "New Move",
                "description": "Try a new exercise suggested by the 'Athlete Workout' module."
            },
            {
                "name": "Allergy Check",
                "description": "Review or update your 'Suitability Profile' (allergies/conditions)."
            },
            {
                "name": "Sugar Watch",
                "description": "Stay below your recommended sugar limit for the day."
            },
            {
                "name": "Step Up",
                "description": "Log your daily step count (or sync it)."
            }
        ],
        "status": "Pending",
        "reward_lp": 10
    },
    "progress": {
        "status": "IN_PROGRESS",
        "completed": 0,
        "remaining": 5
    },
    "streak": 2
}
```

---

## 3. Log Activity

**Endpoint:** `POST /log_activity`

**Description:**
Logs a specific activity completion for a user. This updates the status of the corresponding task in the daily quest, calculates XP gained, and updates the user's level and streak if applicable.

**Request Body:**

```json
{
    "user_id": 999,
    "activity_name": "Fruit Snap"
}
```

**Response Example:**

```json
{
    "status": "Activity logged successfully.",
    "quest_status": {
        "status": "IN_PROGRESS",
        "completed": 3,
        "remaining": 2
    },
    "logged_activity": "Allergy Check",
    "xp_update": {
        "xp_gained": 10,
        "new_total_xp": 40,
        "new_level": 1,
        "stats": {
            "current_level": 1,
            "xp_in_current_level": 40,
            "xp_target_next_level": 100,
            "xp_progress_percent": 40.0
        }
    },
    "streak_update": {
        "status": "Already updated today",
        "current_streak": 1
    }
}
```
