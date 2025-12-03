# Streak Gamification App Documentation

## Project Overview
The Streak Gamification App is a web-based application designed to help users build habits by tracking daily check-ins. It features a streak system where users are rewarded for consecutive daily check-ins. The application includes user authentication, real-time streak updates, and a responsive user interface.

## Features
- **User Authentication**: Secure registration and login system using JWT (JSON Web Tokens).
- **Daily Check-in**: Users can check in once every day to maintain their streak.
- **Streak Tracking**:
  - **Current Streak**: Counts the number of consecutive days checked in.
  - **Longest Streak**: Tracks the highest streak achieved by the user.
  - **Streak Reset**: Automatically resets the streak to 1 if a day is missed.
- **Responsive UI**: A clean, dark-themed interface built with HTML, CSS, and Vanilla JavaScript.
- **Persistent Data**: User data and streaks are stored in a SQLite database.

## Technology Stack

### Backend
- **Language**: Python 3.x
- **Framework**: FastAPI (High-performance web framework)
- **Server**: Uvicorn (ASGI server)
- **Database**: SQLite (with SQLAlchemy ORM)
- **Authentication**: Python-Jose (JWT handling), Passlib (Password hashing)
- **Validation**: Pydantic

### Frontend
- **Structure**: HTML5 (Jinja2 Templates)
- **Styling**: Vanilla CSS3 (Dark mode, responsive design)
- **Logic**: Vanilla JavaScript (Fetch API for backend communication)

## Project Structure
```
c:/Shubham/Office/Gammification/
├── .env                 # Environment variables (Secret keys, etc.)
├── .venv/               # Python Virtual Environment
├── gammification.db     # SQLite Database file
├── requirements.txt     # Python dependencies
└── app/                 # Main Application Directory
    ├── main.py          # App entry point & API routes
    ├── models.py        # SQLAlchemy Database Models
    ├── schemas.py       # Pydantic Data Schemas
    ├── crud.py          # Database CRUD operations
    ├── auth.py          # Authentication logic & utilities
    ├── database.py      # Database connection setup
    ├── templates/       # HTML Templates
    │   └── index.html   # Main application page
    └── static/          # Static Assets
        ├── style.css    # CSS Styles
        └── script.js    # Frontend JavaScript logic
```

## Installation & Setup

1.  **Prerequisites**: Ensure Python 3.8+ is installed on your system.

2.  **Clone/Navigate**: Open the project directory.
    ```bash
    cd c:/Shubham/Office/Gammification
    ```

3.  **Virtual Environment**:
    It is recommended to use the existing virtual environment (`.venv`).
    ```bash
    # Windows
    .venv\Scripts\activate
    ```

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application**:
    Start the development server using Uvicorn.
    ```bash
    uvicorn app.main:app --reload
    ```

6.  **Access the App**:
    Open your browser and navigate to: `http://127.0.0.1:8000`

## API Endpoints

### Authentication
-   `POST /token`: Login and retrieve an access token.
    -   **Body**: `username`, `password` (OAuth2PasswordRequestForm)
-   `POST /api/register`: Register a new user.
    -   **Body**: `{"username": "...", "password": "..."}`

### User Operations
-   `GET /api/user/me`: Get current logged-in user details.
    -   **Headers**: `Authorization: Bearer <token>`
-   `POST /api/checkin`: Perform a daily check-in.
    -   **Headers**: `Authorization: Bearer <token>`
    -   **Body**: `{"local_date": "YYYY-MM-DD"}`

## Database Model (`User`)
-   `id`: Integer, Primary Key
-   `username`: String, Unique
-   `hashed_password`: String
-   `last_checkin_date`: Date
-   `current_streak`: Integer
-   `longest_streak`: Integer

## Development Notes
-   The database is initialized automatically on startup (`models.Base.metadata.create_all`).
-   The frontend uses `localStorage` to persist the JWT token across sessions.
-   Timezone handling relies on the client sending the `local_date` to ensure streaks are calculated based on the user's local time.
