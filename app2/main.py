# main.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
import os

# Import core logic and data
from app2.database import ACTIVITY_LOG, DAILY_QUESTS
from app2.assign_tasks import assign_tasks, get_full_quest_details
from app2.Master_Activities import MASTER_ACTIVITY_DATA
from app2.xp_system import process_user_activity_xp


app = FastAPI(title="Bobo Gamification API")

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount static files and templates
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Pydantic Model for incoming activity logs
class ActivityLog(BaseModel):
    user_id: int
    activity_name: str

# --- Core Task Check Logic (Simulates DB Trigger) ---
def check_daily_tasks(user_id: int) -> Optional[dict]:
    """
    Checks the Activity_Log against the assigned Daily_Quests and updates status.
    """
    today = date.today().isoformat()
    
    quest_filter = {"user_id": user_id, "quest_date": today, "status": "Pending"}
    current_quest = DAILY_QUESTS.find_one(quest_filter)
    
    if not current_quest:
        # Quest either completed or not yet assigned.
        return {"status": "NO_ACTIVE_QUEST", "completed": 0, "remaining": 0}

    assigned_tasks = current_quest.get("tasks_list", [])
    
    # Query the Activity_Log for today's completed tasks
    log_filter = {
        "user_id": user_id,
        "activity_name": {"$in": assigned_tasks}, 
        "log_date": today
    }
    
    completed_tasks = ACTIVITY_LOG.distinct("activity_name", log_filter)
    tasks_completed_count = len(completed_tasks)
    
    print(f"User {user_id} has completed {tasks_completed_count} unique tasks today.")

    # Check for completion and update quest status
    if tasks_completed_count >= 5:
        reward_lp = current_quest.get("quest_reward_lp", 10) 
        
        # Update the quest status to 'Complete'
        DAILY_QUESTS.update_one(
            {"_id": current_quest["_id"]},
            {"$set": {"status": "Complete", "completion_time": datetime.utcnow()}}
        )
        
        return {
            "status": "QUEST_COMPLETE",
            "message": f"Congratulations! Quest complete, earned {reward_lp} LP!",
            "reward": reward_lp,
            "completed": 5,
            "remaining": 0
        }
    
    return {
        "status": "IN_PROGRESS",
        "completed": tasks_completed_count,
        "remaining": 5 - tasks_completed_count
    }


# --- API Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main frontend page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/activities")
def get_all_activities():
    """Get all available activities with descriptions"""
    return {"activities": MASTER_ACTIVITY_DATA}


@app.post("/quests/{user_id}/assign")
def handle_assign_quest(user_id: int):
    """Assigns the user a new 5-task quest for the day."""
    try:
        # assign_tasks returns a cleaned dictionary with task descriptions
        quest_data = assign_tasks(user_id) 
        return {"message": quest_data.pop("message", "Daily quest ready."), "quest": quest_data}
    except Exception as e:
        # You might want a more specific error here
        raise HTTPException(status_code=500, detail=f"Error assigning quest: {e}")


@app.post("/log_activity")
def handle_log_activity(log_data: ActivityLog):
    """
    Logs a completed activity and runs the task check (simulating the DB trigger).
    Now also calculates and updates XP.
    """
    user_id = log_data.user_id
    activity_name = log_data.activity_name
    
    # 1. Validation 
    if activity_name not in MASTER_ACTIVITY_DATA:
        raise HTTPException(status_code=400, detail=f"Unknown activity name: {activity_name}")

    # 2. Log the activity to MongoDB
    log_document = {
        "user_id": user_id,
        "activity_name": activity_name,
        "timestamp": datetime.utcnow(),
        "log_date": date.today().isoformat()
    }
    ACTIVITY_LOG.insert_one(log_document)
    
    # 3. XP & Level Update
    xp_result = process_user_activity_xp(user_id, activity_name)

    # 4. Simulate the DB Trigger: Execute the check function immediately
    check_result = check_daily_tasks(user_id)
    
    return {
        "status": "Activity logged successfully.",
        "quest_status": check_result,
        "logged_activity": activity_name,
        "xp_update": xp_result
    }

@app.get("/quests/{user_id}/status")
def view_quest_status(user_id: int):
    """Retrieves the user's current quest and progress for today."""
    today = date.today().isoformat()
    quest = DAILY_QUESTS.find_one({"user_id": user_id, "quest_date": today})
    
    if not quest:
        return {"message": "No quest found for today. Assign one first."}

    # **FIX for ObjectId Issue**: Convert _id to string 
    quest['_id'] = str(quest['_id'])
    
    # Fetch completed tasks to show progress
    check_result = check_daily_tasks(user_id)

    # Get detailed task list for the API response
    detailed_tasks = get_full_quest_details(quest) 
    
    return {
        "quest_details": {
            "tasks": detailed_tasks, # Shows name and description
            "status": quest.get("status"),
            "reward_lp": quest.get("quest_reward_lp")
        },
        "progress": check_result
    }