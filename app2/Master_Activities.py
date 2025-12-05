# MASTER_ACTIVITY_DATA.py

MASTER_ACTIVITY_DATA = {
    # --- Group 1: Logging & Manual Inputs (The "Daily Tracker") ---
    "Hydration Hit": {
        "description": "Log a glass of water (Goal: 8/day)."
    },
    "Supplement Tick": {
        "description": "Check off your daily vitamins/supplements."
    },
    "Fruit Snap": {
        "description": "Log eating one piece of fruit."
    },
    "Caffeine Log": {
        "description": "Log your coffee/tea intake."
    },
    "Step Up": {
        "description": "Log your daily step count (or sync it)."
    },
    "Mood Lift": {
        "description": "Log how you feel after a workout."
    },
    "Cardio King": {
        "description": "Log a 30-minute steady-state cardio session."
    },
    "Symptom Log": {
        "description": "Log a daily symptom check (e.g., Headache: None)."
    },
    "Meds Check": {
        "description": "Mark a scheduled medication as 'Taken'."
    },
    "Mood Meter": {
        "description": "Log your current stress/mood level."
    },
    "Sleep Log": {
        "description": "Confirm your sleep duration for last night."
    },

    # --- Group 2: AI Analysis & Media Uploads (The "Smart Scan") ---
    "AI Food Scan": {
        "description": "Snap a photo of your lunch to auto-calculate macros."
    },
    "Label Decoder": {
        "description": "Scan a barcode to see if a product matches your health profile (e.g., Diabetes safe)."
    },
    "Live Form Check": {
        "description": "Use the camera 'Live Analysis' for one set of Squats/Pushups."
    },
    "Video Review": {
        "description": "Upload a recorded video of your exercise for AI feedback."
    },
    "Rep Counter": {
        "description": "Use the AI to auto-count reps for one exercise."
    },
    "Doc Locker": {
        "description": "Upload a medical report/prescription file to 'Medical Records'."
    },

    # --- Group 3: Information Retrieval & Review (The "Quick View") ---
    "Meal Peek": {
        "description": "View your 'Smart Meal Plan' for today."
    },
    "Allergy Check": {
        "description": "Review or update your 'Suitability Profile' (allergies/conditions)."
    },
    "Plan View": {
        "description": "Open your 'General Workout Plan' for the week."
    },
    "Daily Fact": {
        "description": "Read one 'Micro-learning' card or fact."
    },
    "Course Browse": {
        "description": "View the syllabus of a generated course."
    },
    "Transcript Peek": {
        "description": "Use the search function to find a keyword in a class transcript."
    },
    "Whiteboard View": {
        "description": "Review a saved whiteboard snapshot from a previous class."
    },
    "Contact Update": {
        "description": "Verify your Emergency Contacts are up to date."
    },
    "Vitals View": {
        "description": "View the trend graph for BP or Glucose."
    },
    "Vaccine Tracker": {
        "description": "Update your vaccination status or view upcoming shots."
    },

    # --- Group 4: Planning, Building, & Completion (The "Action Taker") ---
    "Quick Swap": {
        "description": "Use the tool to find a healthy alternative to a junk food item."
    },
    "Grocery Run": {
        "description": "Generate a 'Smart Shopping List' for the week."
    },
    "Recipe Hunter": {
        "description": "Save 3 healthy recipes suggested by the AI."
    },
    "Cooking Mode": {
        "description": "Mark a meal as 'Prepared/Cooked' in the planner."
    },
    "Goal Set": {
        "description": "Input your fitness goal (e.g., Build Muscle/Lose Weight)."
    },
    "Gear Check": {
        "description": "Input available equipment (e.g., 'Home - Dumbbells')."
    },
    "Warm-up": {
        "description": "Mark the 'Warm-up' section of your plan as complete."
    },
    "Quick Stretch": {
        "description": "Complete a 5-minute suggested mobility routine."
    },
    "Full Session": {
        "description": "Mark a 'Main Workout' (approx. 20-40 mins) as complete."
    },
    "New Move": {
        "description": "Try a new exercise suggested by the 'Athlete Workout' module."
    },
    "Note Taker": {
        "description": "Save one note during a learning session."
    },
    "Reminder Set": {
        "description": "Set a reminder for an upcoming Live Class."
    },
    "Concept Map": {
        "description": "Generate an AI summary of a complex topic using the Study Buddy."
    },
    "First Aid Drill": {
        "description": "Complete a 2-minute 'Emergency Response' simulation/quiz."
    },

    # --- Group 5: Core Focus Activities (The "Learning & Alignment") ---
    "Macro Balancer": {
        "description": "Hit your protein goal for the day."
    },
    "Sugar Watch": {
        "description": "Stay below your recommended sugar limit for the day."
    },
    "Tempo Master": {
        "description": "Receive a 'Good Tempo' rating from the AI on a recorded set."
    },
    "Doubt Buster": {
        "description": "Ask the 'Study Buddy' AI one question."
    },
    "Quiz Whiz": {
        "description": "Complete a topic-specific quiz in the 'Practice Hub'."
    },
    "Class Attendance": {
        "description": "Join a 'Live Class' for at least 15 minutes."
    },
    "Flashcard Flip": {
        "description": "Review 10 flashcards in the practice mode."
    },
    "Homework Hero": {
        "description": "Submit a practice assignment."
    },
    "Gap Fill": {
        "description": "Complete a personalized exercise generated to fix a 'Knowledge Gap'."
    },
    "Active Listener": {
        "description": "Maintain an 'Engaged' status (via EduSmart Tracker) for 10 mins in a live class."
    },
    "Injury Check": {
        "description": "Use the 'Injury Assessment' chat to evaluate a minor issue."
    }
}

# --- Separate lists for assignment logic (based on the keys of the dictionary) ---

GROUP_1 = [
    "Hydration Hit", "Supplement Tick", "Fruit Snap", "Caffeine Log", "Step Up",
    "Mood Lift", "Cardio King", "Symptom Log", "Meds Check", "Mood Meter",
    "Sleep Log"
]

GROUP_2 = [
    "AI Food Scan", "Label Decoder", "Live Form Check", "Video Review",
    "Rep Counter", "Doc Locker"
]

GROUP_3 = [
    "Meal Peek", "Allergy Check", "Plan View", "Daily Fact", "Course Browse",
    "Transcript Peek", "Whiteboard View", "Contact Update", "Vitals View",
    "Vaccine Tracker"
]

GROUP_4 = [
    "Quick Swap", "Grocery Run", "Recipe Hunter", "Cooking Mode", "Goal Set",
    "Gear Check", "Warm-up", "Quick Stretch", "Full Session", "New Move",
    "Note Taker", "Reminder Set", "Concept Map", "First Aid Drill"
]

GROUP_5 = [
    "Macro Balancer", "Sugar Watch", "Tempo Master", "Doubt Buster", "Quiz Whiz",
    "Class Attendance", "Flashcard Flip", "Homework Hero", "Gap Fill",
    "Active Listener", "Injury Check"
]

ALL_ACTIVITIES = list(MASTER_ACTIVITY_DATA.keys())