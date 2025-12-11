from pymongo import MongoClient
from datetime import datetime

# --- MongoDB Setup ---
MONGO_URI = "mongodb://localhost:27017/" 
DB_NAME = "BoboGamificationDB"
CLIENT = MongoClient(MONGO_URI)
DB = CLIENT[DB_NAME]

# Define collections 
DAILY_QUESTS = DB["Daily_Quests"]
ACTIVITY_LOG = DB["Activity_Log"]
USER_STREAKS = DB["User_Streaks"]

# Connect to Users DB (shared with app 1)
# USERS_DB = CLIENT["gammification_db"]
# USERS_COLLECTION = USERS_DB["users"]