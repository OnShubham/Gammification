"""
Script to fix the database by dropping the old username index
and creating a proper unique index on user_id
"""
from pymongo import MongoClient
import os

# MongoDB Configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "gammification_db")

# Connect to MongoDB
client = MongoClient(MONGODB_URL)
db = client[DATABASE_NAME]
users_collection = db["users"]

print("=" * 60)
print("DATABASE INDEX FIX SCRIPT")
print("=" * 60)

print("\n1. Current indexes:")
indexes = list(users_collection.list_indexes())
for idx in indexes:
    index_name = idx.get('name', 'unknown')
    index_key = idx.get('key', {})
    unique = idx.get('unique', False)
    print(f"   - Name: {index_name}")
    print(f"     Keys: {dict(index_key)}")
    print(f"     Unique: {unique}")

print("\n2. Dropping 'username_1' index...")
try:
    users_collection.drop_index("username_1")
    print("   ✓ Successfully dropped 'username_1' index")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n3. Creating unique index on 'user_id'...")
try:
    users_collection.create_index("user_id", unique=True)
    print("   ✓ Successfully created unique index on 'user_id'")
except Exception as e:
    print(f"   ✗ Error: {e}")
    if "already exists" in str(e).lower():
        print("   (Index already exists - this is OK)")

print("\n4. Final indexes:")
indexes = list(users_collection.list_indexes())
for idx in indexes:
    index_name = idx.get('name', 'unknown')
    index_key = idx.get('key', {})
    unique = idx.get('unique', False)
    print(f"   - Name: {index_name}")
    print(f"     Keys: {dict(index_key)}")
    print(f"     Unique: {unique}")

print("\n" + "=" * 60)
print("DATABASE FIX COMPLETE!")
print("=" * 60)
