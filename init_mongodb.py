"""
MongoDB initialization script
Creates indexes for better query performance
"""
from app.database import users_collection

def init_db():
    """Initialize MongoDB indexes"""
    # Create unique index on username
    users_collection.create_index("username", unique=True)
    print("✓ Created unique index on username field")
    print("✓ MongoDB initialized successfully")

if __name__ == "__main__":
    init_db()
