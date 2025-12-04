# Streak Tracking System Documentation

## Overview
The gamification app now tracks four types of streaks for each user:

## Streak Fields

### 1. **current_streak** (int)
- Tracks the user's current consecutive check-in streak
- Increments by 1 when user checks in on consecutive days
- Resets to 1 if the user misses a day

### 2. **longest_streak** (int)
- Stores the maximum streak the user has ever achieved
- Updates automatically when `current_streak` exceeds the previous record

### 3. **regular_streaks** (dict)
- Tracks how many times a user has reached specific milestone streaks
- Format: `{"7_day": 2, "30_day": 1, "90_day": 1}`
- Milestones tracked: 3, 7, 14, 30, 60, 90, 180, 365 days
- Each time a user reaches a milestone, the counter for that milestone increments

### 4. **counting_streaks** (int)
- Total count of ALL milestone achievements
- Increments by 1 each time any milestone is reached
- Useful for gamification badges and rewards

## Example Scenario

**User Journey:**
1. User checks in for 7 consecutive days
   - `current_streak`: 7
   - `longest_streak`: 7
   - `regular_streaks`: `{"7_day": 1}`
   - `counting_streaks`: 1

2. User continues to 30 days
   - `current_streak`: 30
   - `longest_streak`: 30
   - `regular_streaks`: `{"7_day": 1, "14_day": 1, "30_day": 1}`
   - `counting_streaks`: 3

3. User misses a day, then starts a new streak and reaches 7 days again
   - `current_streak`: 7
   - `longest_streak`: 30 (unchanged)
   - `regular_streaks`: `{"7_day": 2, "14_day": 1, "30_day": 1}`
   - `counting_streaks`: 4

## API Response Example

```json
{
  "username": "john_doe",
  "last_checkin_date": "2025-12-04",
  "current_streak": 15,
  "longest_streak": 45,
  "regular_streaks": {
    "3_day": 5,
    "7_day": 3,
    "14_day": 2
  },
  "counting_streaks": 10
}
```

## Database Migration

If you have existing users, run the migration script:
```bash
python migrate_streaks.py
```

This will add the new fields to all existing users with default values:
- `regular_streaks`: `{}`
- `counting_streaks`: `0`
