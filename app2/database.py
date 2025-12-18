from pymongo import MongoClient
from datetime import datetime

# --- MongoDB Setup ---
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- MongoDB Setup ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "BoboGamificationDB")
CLIENT = MongoClient(MONGO_URI)
DB = CLIENT[DB_NAME]

# Define collections 
DAILY_QUESTS = DB[os.getenv("DAILY_QUESTS_COLLECTION", "Daily_Quests")]
ACTIVITY_LOG = DB[os.getenv("ACTIVITY_LOG_COLLECTION", "Activity_Log")]
USER_STREAKS = DB[os.getenv("USER_STREAKS_COLLECTION", "User_Streaks")]

# Connect to Users DB (shared with app 1)
# USERS_DB = CLIENT["gammification_db"]
# USERS_COLLECTION = USERS_DB["users"]