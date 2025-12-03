from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import os

# MongoDB Configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "gammification_db")

# Synchronous MongoDB client (for non-async operations)
client = MongoClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Async MongoDB client (for async operations with FastAPI)
async_client = AsyncIOMotorClient(MONGODB_URL)
async_db = async_client[DATABASE_NAME]

# Collections
users_collection = db["users"]
async_users_collection = async_db["users"]

def get_db():
    """Get database instance for dependency injection"""
    return db

def get_async_db():
    """Get async database instance for dependency injection"""
    return async_db
