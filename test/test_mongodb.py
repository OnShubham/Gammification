"""
Test MongoDB connection
"""
from app.database import db, users_collection
from pymongo.errors import ConnectionFailure

def test_connection():
    try:
        # Test connection
        db.client.admin.command('ping')
        print("✓ Successfully connected to MongoDB!")
        print(f"✓ Database: {db.name}")
        print(f"✓ Collections: {db.list_collection_names()}")
        
        # Count users
        user_count = users_collection.count_documents({})
        print(f"✓ Total users in database: {user_count}")
        
        return True
    except ConnectionFailure as e:
        print(f"✗ Failed to connect to MongoDB: {e}")
        print("\nMake sure MongoDB is running on localhost:27017")
        print("You can start MongoDB with: mongod")
        return False

if __name__ == "__main__":
    test_connection()
