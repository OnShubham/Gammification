Absolutely — here is a polished **`README.md`** ready for your repo 👇
You can copy-paste directly into GitHub.

---

````markdown
# Daily Streak System (Check-in & Usage Streaks)

A backend workflow for tracking daily activity streaks (similar to Snapchat).  
Supports multiple streak types:
- **Daily Check-in** (explicit user action)
- **Daily Usage** (app usage counts as streak)

---

## 🧠 Core Concept

Each streak is defined **per user, per streak type**:
- Tracks **current streak**
- Tracks **longest streak**
- Saves **last active date**

Streak increments only if:
- The user completes an event **on a new day**
- The last event was **exactly 1 day ago**

If the user misses a day → **streak resets**.

---

## 📊 Data Model

### `users`
| Field | Type | Notes |
|------|------|------|
| id | UUID / number | Primary Key |
| timezone | string | Convert timestamps before streak logic |

### `streaks`
| Field | Type | Notes |
|------|------|------|
| id | UUID / number | Primary Key |
| user_id | FK | user reference |
| type | enum | CHECKIN / USAGE |
| current_streak | int | active count |
| longest_streak | int | record count |
| last_event_date | date | YYYY-MM-DD (no time) |
| created_at | datetime | |
| updated_at | datetime | |

### `streak_events` (optional)
For analytics/history — not required for basic logic.

---

## 🔁 Streak Workflow Diagram

```mermaid
flowchart LR
    U[User / App Client] -->|Open app or tap 'Check-in'| A[Send Event to Backend]

    A --> B[Auth Service\nVerify Token]
    B --> C[Streak Service]

    C --> D[Fetch Streak Record]
    D --> E[Compare last_event_date with today]

    E --> F{Day difference?}

    F -->|0 days| G[Already counted today\nReturn streak]
    F -->|1 day| H[Increment streak]
    F -->|>1 day| I[Reset streak to 1]

    H --> J[Update DB & longest streak]
    I --> J

    G --> K[Return streak response]
    J --> K

    K --> U
````

---

## ⚙️ Streak Update Flowchart (Core Algorithm)

```mermaid
flowchart TD
    A[Event received] --> B[Convert timestamp to\nuser_local_date]
    B --> C[Load streak record]
    C --> D{Exists?}

    D -->|No| E[Create record\ncurrent_streak = 1\nlongest_streak = 1]
    E --> Z[Return streak]

    D -->|Yes| F[Calculate day_diff]

    F --> G{day_diff == 0?}
    G -->|Yes| Z[Return existing streak]

    G -->|No| H{day_diff == 1?}
    H -->|Yes| I[Increment streak\nUpdate record]
    I --> Z[Return streak]

    H -->|No| J[Reset current_streak = 1]
    J --> K[Update record]
    K --> Z[Return streak]
```

---

## 📡 API Example (REST)

### Trigger streak update

```http
POST /api/streaks/event
```

#### Request Body

```json
{
  "user_id": "12345",
  "streak_type": "CHECKIN",
  "source": "MOBILE"
}
```

#### Response

```json
{
  "current_streak": 4,
  "longest_streak": 12,
  "last_event_date": "2025-12-03",
  "updated": true
}
```

---

## ⛔ Edge Cases

| Case                                   | Action                                  |
| -------------------------------------- | --------------------------------------- |
| Multiple actions in one day            | Return same streak (don’t increment)    |
| Missed more than 1 day                 | Reset streak to 1                       |
| Timestamp earlier than last_event_date | Ignore or clamp to current date         |
| Timezone difference                    | Always calculate by **user-local date** |

---

## 🎯 Features You Can Add Later

* Streak freeze / Save My Streak (coins / reward system)
* Push notifications for missed streaks
* Badges or reward unlocks at milestones
* Weekly or monthly progress graphs
* Social sharing (“🔥 15-day streak!”)

---

## 📌 Summary

This system provides:
✔ Reliable streak tracking
✔ Timezone-safe date handling
✔ Lightweight & scalable design
✔ Works for any type of streak event (check-in, usage, learning, etc.)

---

Feel free to modify the schema and diagrams as needed.
If you want, I can also provide:

✨ SQL schema
✨ Backend code (Node, Firebase, Django, etc.)
✨ Example UI widgets

Would you like me to generate a **Streak Service class implementation** for your tech stack?
