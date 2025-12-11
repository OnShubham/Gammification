# 🏗️ App2 Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                          │
│                     http://localhost:8001                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      FRONTEND LAYER                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  index.html  │  │  style.css   │  │   app.js     │      │
│  │              │  │              │  │              │      │
│  │ • Structure  │  │ • Glassmor-  │  │ • API calls  │      │
│  │ • Layout     │  │   phism      │  │ • State mgmt │      │
│  │ • Components │  │ • Animations │  │ • UI updates │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ HTTP/JSON
┌─────────────────────────────────────────────────────────────┐
│                      FASTAPI BACKEND                         │
├─────────────────────────────────────────────────────────────┤
│                         main.py                              │
│  ┌────────────────────────────────────────────────────┐     │
│  │  API Endpoints                                     │     │
│  │  • GET  /                → Serve HTML              │     │
│  │  • GET  /api/activities  → Get all activities      │     │
│  │  • POST /quests/{id}/assign → Assign quest         │     │
│  │  • GET  /quests/{id}/status → Get quest status     │     │
│  │  • POST /log_activity    → Log activity            │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      BUSINESS LOGIC                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │assign_tasks  │  │  xp_system   │  │check_daily   │      │
│  │              │  │              │  │   _tasks     │      │
│  │ • Select 5   │  │ • +10 XP     │  │ • Track      │      │
│  │   tasks      │  │ • Calculate  │  │   progress   │      │
│  │ • Group      │  │   level      │  │ • Complete   │      │
│  │   logic      │  │ • Daily cap  │  │   quest      │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  ┌──────────────────────────────────────────────────┐       │
│  │         Master_Activities.py                     │       │
│  │  • 67+ activity definitions                      │       │
│  │  • 5 groups (G1-G5)                              │       │
│  │  • Descriptions                                  │       │
│  └──────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATABASE LAYER                          │
├─────────────────────────────────────────────────────────────┤
│                    MongoDB (database.py)                     │
│  ┌────────────────────────────────────────────────────┐     │
│  │  Collections:                                      │     │
│  │  • ACTIVITY_LOG    → Activity records             │     │
│  │  • DAILY_QUESTS    → Quest assignments            │     │
│  │  • USERS_COLLECTION → User XP & levels            │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. Assign Quest Flow
```
User clicks "Assign Quest"
         │
         ▼
Frontend (app.js)
  fetch('/quests/1/assign', {method: 'POST'})
         │
         ▼
Backend (main.py)
  @app.post("/quests/{user_id}/assign")
         │
         ▼
Business Logic (assign_tasks.py)
  • Check if quest exists for today
  • Select 5 tasks (1×G1, 1×G4, 1×G3, 1×G2/G5, 1×Wildcard)
  • Prevent duplicates
         │
         ▼
Database (MongoDB)
  DAILY_QUESTS.insert_one({
    user_id, quest_date, tasks_list,
    status: "Pending", reward: 10
  })
         │
         ▼
Response to Frontend
  {quest: {tasks: [...], status: "Pending"}}
         │
         ▼
UI Update (app.js)
  • Display 5 tasks
  • Show progress bar (0/5)
  • Enable activity logging
```

### 2. Log Activity Flow
```
User selects activity & clicks "Log Activity"
         │
         ▼
Frontend (app.js)
  fetch('/log_activity', {
    method: 'POST',
    body: {user_id: 1, activity_name: "Hydration Hit"}
  })
         │
         ▼
Backend (main.py)
  @app.post("/log_activity")
  • Validate activity exists
         │
         ▼
Database Write (MongoDB)
  ACTIVITY_LOG.insert_one({
    user_id, activity_name, timestamp, log_date
  })
         │
         ▼
XP Calculation (xp_system.py)
  • Check daily cap (max 10 per activity)
  • Award 10 XP
  • Calculate new total XP
  • Calculate level (Total XP / 100 + 1)
  • Update user record
         │
         ▼
Database Update (MongoDB)
  USERS_COLLECTION.update_one({
    total_xp, current_level, xp_progress
  })
         │
         ▼
Quest Check (check_daily_tasks.py)
  • Query completed tasks for today
  • Count unique tasks
  • If count >= 5:
      - Update quest status to "Complete"
      - Award 10 LP
         │
         ▼
Response to Frontend
  {
    xp_update: {xp_gained: 10, new_level: 1, ...},
    quest_status: {completed: 1, remaining: 4}
  }
         │
         ▼
UI Update (app.js)
  • Update XP display
  • Update level display
  • Update progress bar
  • Show toast notification
  • If quest complete: Show celebration
```

## Component Interaction

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND COMPONENTS                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Header                                                      │
│  ├─ Logo                                                     │
│  └─ User ID Selector ──────────┐                            │
│                                 │                            │
│  Stats Dashboard               │                            │
│  ├─ Level Card                 │                            │
│  ├─ Total XP Card              │                            │
│  └─ Progress Card              │                            │
│                                 │                            │
│  XP Progress Bar               │                            │
│  └─ Animated gradient fill     │                            │
│                                 │                            │
│  Main Grid                     │                            │
│  ├─ Quest Panel                │                            │
│  │   ├─ Assign Button ─────────┼─→ POST /quests/{id}/assign│
│  │   ├─ Quest Status           │                            │
│  │   ├─ Progress Bar           │                            │
│  │   └─ Tasks List             │                            │
│  │                              │                            │
│  └─ Activity Panel             │                            │
│      ├─ Activity Dropdown ─────┼─→ GET /api/activities      │
│      ├─ Description            │                            │
│      └─ Log Button ────────────┼─→ POST /log_activity       │
│                                 │                            │
│  Activity Groups               │                            │
│  └─ 5 Category Cards           │                            │
│                                 │                            │
│  Toast Notification            │                            │
│  └─ Success/Error messages     │                            │
│                                 │                            │
└─────────────────────────────────┴────────────────────────────┘
```

## State Management

```javascript
// Frontend State (app.js)
{
  currentUserId: 1,              // Active user
  currentActivities: {...},      // All 67+ activities
  currentQuest: {...},           // Today's quest
  userStats: {                   // User progress
    current_level: 1,
    total_xp: 50,
    xp_progress: 50
  }
}

// Backend State (MongoDB)
{
  ACTIVITY_LOG: [                // Activity records
    {user_id, activity_name, timestamp, log_date}
  ],
  DAILY_QUESTS: [                // Quest assignments
    {user_id, quest_date, tasks_list, status, reward}
  ],
  USERS_COLLECTION: [            // User profiles
    {user_id, total_xp, current_level, xp_progress}
  ]
}
```

## Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                      TECHNOLOGY LAYERS                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Presentation Layer                                          │
│  ├─ HTML5          → Structure & semantics                  │
│  ├─ CSS3           → Styling & animations                   │
│  └─ JavaScript ES6 → Interactivity & logic                  │
│                                                              │
│  Application Layer                                           │
│  ├─ FastAPI        → Web framework                          │
│  ├─ Pydantic       → Data validation                        │
│  └─ Uvicorn        → ASGI server                            │
│                                                              │
│  Business Logic Layer                                        │
│  ├─ Python 3.x     → Core logic                             │
│  ├─ Custom modules → Quest/XP/Activity logic                │
│  └─ MongoDB driver → Database operations                    │
│                                                              │
│  Data Layer                                                  │
│  ├─ MongoDB        → NoSQL database                         │
│  ├─ Collections    → Activity_Log, Daily_Quests, Users      │
│  └─ Indexes        → user_id, quest_date                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Design Patterns

### Frontend
- **MVC Pattern**: Separation of concerns
- **Event-Driven**: User interactions trigger events
- **Async/Await**: Non-blocking API calls
- **State Management**: Centralized state object

### Backend
- **REST API**: Resource-based endpoints
- **Dependency Injection**: FastAPI's DI system
- **Repository Pattern**: Database abstraction
- **Service Layer**: Business logic separation

## Security & Performance

### Security
- ✅ Input validation (Pydantic models)
- ✅ Activity name validation
- ✅ Daily cap enforcement
- ✅ No SQL injection (MongoDB driver)

### Performance
- ✅ Async operations (FastAPI)
- ✅ Database indexing
- ✅ Minimal frontend dependencies
- ✅ Efficient queries
- ✅ Client-side caching

## Scalability

### Current Capacity
- Handles multiple concurrent users
- Efficient database queries
- Fast response times (<100ms)

### Future Scaling
- Add Redis caching
- Implement load balancing
- Database sharding
- CDN for static files

---

**Architecture designed for maintainability, scalability, and user experience**
