# assign_tasks.py

import random
from datetime import date
from .Master_Activities import GROUP_1, GROUP_2, GROUP_3, GROUP_4, GROUP_5, ALL_ACTIVITIES, MASTER_ACTIVITY_DATA
from .database import DAILY_QUESTS # Import MongoDB collection

def get_full_quest_details(quest_doc: dict) -> list:
    """Transforms a list of task names into a list of detailed task objects."""
    detailed_tasks = []
    task_names = quest_doc.get("tasks_list", [])
    
    for name in task_names:
        details = MASTER_ACTIVITY_DATA.get(name, {})
        detailed_tasks.append({
            "name": name,
            "description": details.get("description", "Description not found.")
        })
    return detailed_tasks

def assign_tasks(user_id: int):
    """
    Randomly assigns 5 tasks to the user and saves them to the Daily_Quests collection.
    """
    
    today = date.today().isoformat()
    
    # 1. Check if tasks are already assigned for today
    existing_quest = DAILY_QUESTS.find_one({
        "user_id": user_id, 
        "quest_date": today
    })
    
    if existing_quest:
        # **FIX for ObjectId Issue**: Convert _id to string for existing quest
        existing_quest['_id'] = str(existing_quest['_id'])
        return {
            "message": "Quest already assigned for today.",
            "user_id": user_id,
            "quest_date": today,
            "tasks": get_full_quest_details(existing_quest),
            "status": existing_quest["status"]
        }

    # --- Task Selection Logic ---
    assigned_tasks = []
    
    # 1xG1, 1xG4, 1xG3, 1x(G2 or G5), 1xWildcard
    
    # Slot 1: Group 1 (Logging)
    assigned_tasks.append(random.choice(GROUP_1))
    
    # Slot 2: Group 4 (Planning)
    while True:
        task = random.choice(GROUP_4)
        if task not in assigned_tasks:
            assigned_tasks.append(task)
            break
            
    # Slot 3: Group 3 (Review/View)
    while True:
        task = random.choice(GROUP_3)
        if task not in assigned_tasks:
            assigned_tasks.append(task)
            break

    # Slot 4: Group 2 or 5 (Core Focus/AI)
    G2_or_G5 = GROUP_2 + GROUP_5
    while True:
        task = random.choice(G2_or_G5)
        if task not in assigned_tasks:
            assigned_tasks.append(task)
            break
            
    # Slot 5: Wildcard 
    wildcard_pool = [t for t in ALL_ACTIVITIES if t not in assigned_tasks]
    if wildcard_pool:
        assigned_tasks.append(random.choice(wildcard_pool))
    
    # 2. Create the quest document
    quest_document = {
        "user_id": user_id,
        "quest_date": today,
        "tasks_list": assigned_tasks, 
        "status": "Pending",
        "quest_reward_lp": 10,  # Fixed reward for the batch
        "reward_claimed": False
    }
    
    # 3. Insert and retrieve the document to get the ObjectId
    insert_result = DAILY_QUESTS.insert_one(quest_document)
    
    # 4. Prepare the response
    print(f"Assigned tasks for User {user_id}: {assigned_tasks}")
    
    return {
        "message": "New daily quest assigned.",
        "user_id": user_id,
        "quest_date": today,
        # Fetch the details using the names
        "tasks": get_full_quest_details(quest_document), 
        "status": quest_document["status"]
    }