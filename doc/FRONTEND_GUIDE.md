# App2 Frontend - User Guide

## 🎯 Overview

The App2 frontend is a **beautiful, modern, and fully functional** web interface that allows you to interact with all the gamification features without any authentication. It provides a premium user experience with glassmorphism effects, smooth animations, and real-time updates.

## 🚀 Accessing the Frontend

1. **Make sure the server is running** (it should already be running on port 8001)
2. **Open your browser** and navigate to: `http://localhost:8001`
3. You'll see the stunning gamification dashboard!

## ✨ Features

### 1. **User Selection**
- In the top-right corner, you can enter any User ID (default is 1)
- Change the User ID to track different users' progress
- All data is automatically loaded when you change the user

### 2. **Stats Dashboard**
The top section shows three key metrics:
- **⭐ Level**: Your current level
- **💎 Total XP**: Your accumulated experience points
- **📈 Progress**: Your progress towards the next level (%)

### 3. **XP Progress Bar**
- Visual representation of your progress to the next level
- Shows current XP / required XP
- Animated gradient fill with shimmer effect

### 4. **Daily Quest Panel** (Left Side)

#### Assign Quest
- Click the **"Assign Quest"** button to get your daily quest
- You'll receive 5 random tasks based on the assignment logic:
  - 1 task from Group 1 (Daily Tracker)
  - 1 task from Group 4 (Action Taker)
  - 1 task from Group 3 (Quick View)
  - 1 task from Group 2 or 5 (Smart Scan or Core Focus)
  - 1 wildcard task from any group

#### Quest Progress
- Shows how many tasks you've completed (e.g., "3/5")
- Visual progress bar updates in real-time
- Quest status message shows reward (10 LP)

#### Task List
- All 5 assigned tasks are displayed with:
  - Task name
  - Detailed description
  - Checkbox (filled when completed)

### 5. **Activity Logger Panel** (Right Side)

#### Log Activities
1. **Select an Activity** from the dropdown
   - All 67+ activities are available
   - Sorted alphabetically for easy finding
2. **View Description** - The activity description appears automatically
3. **Click "Log Activity"** to record the activity

#### What Happens When You Log:
- ✅ Activity is recorded in the database
- 💎 You earn **10 XP** (unless daily cap reached)
- 📊 Quest progress updates automatically
- ⭐ Level increases if you reach the threshold (100 XP per level)
- 🎉 Quest completes when you finish 5 tasks
- 📱 Toast notification shows success/failure

### 6. **Activity Categories**
The bottom section shows all 5 activity groups:
- **📝 Daily Tracker** - Logging & Manual Inputs (Group 1)
- **🤖 Smart Scan** - AI Analysis & Media Uploads (Group 2)
- **👁️ Quick View** - Information Retrieval (Group 3)
- **🎬 Action Taker** - Planning & Completion (Group 4)
- **🎓 Core Focus** - Learning & Alignment (Group 5)

## 🎮 How to Use - Complete Workflow

### First Time Setup
1. Open `http://localhost:8001`
2. Enter your User ID (or keep it as 1)
3. Click **"Assign Quest"** to get your daily tasks

### Daily Usage
1. **Check your quest** - See what 5 tasks you need to complete
2. **Select an activity** from the dropdown
3. **Read the description** to understand what it involves
4. **Click "Log Activity"** to record it
5. **Watch your progress** - XP increases, quest progress updates
6. **Complete 5 tasks** to finish the quest and earn 10 LP!

### Example Session
```
User ID: 1
1. Assign Quest → Get 5 tasks
2. Select "Hydration Hit" → Log it → +10 XP (1/5 tasks)
3. Select "Meal Peek" → Log it → +10 XP (2/5 tasks)
4. Select "Quick Stretch" → Log it → +10 XP (3/5 tasks)
5. Select "AI Food Scan" → Log it → +10 XP (4/5 tasks)
6. Select "Doubt Buster" → Log it → +10 XP (5/5 tasks)
7. Quest Complete! 🎉 Earned 10 LP + 50 XP total
```

## 🎨 Design Features

### Visual Excellence
- **Glassmorphism**: Frosted glass effect on all cards
- **Gradient Backgrounds**: Vibrant purple, cyan, and pink orbs
- **Smooth Animations**: Hover effects, transitions, and micro-interactions
- **Modern Typography**: Inter font family
- **Responsive Design**: Works on desktop, tablet, and mobile

### Interactive Elements
- **Hover Effects**: Cards lift and glow on hover
- **Button Ripples**: Click animation on all buttons
- **Toast Notifications**: Elegant pop-up messages
- **Progress Animations**: Smooth bar fills with shimmer effect
- **Loading States**: Spinner animations during API calls

## 📊 Backend Integration

The frontend seamlessly integrates with all backend endpoints:

### API Endpoints Used
1. **GET /api/activities** - Loads all 67+ activities
2. **POST /quests/{user_id}/assign** - Assigns daily quest
3. **GET /quests/{user_id}/status** - Gets quest progress
4. **POST /log_activity** - Logs completed activities

### Data Flow
```
Frontend → API → MongoDB → Response → Frontend Update
```

### Real-time Updates
- Quest progress updates immediately after logging
- XP and level calculations happen server-side
- All stats refresh automatically
- No page reload needed!

## 🔧 Technical Details

### Files Structure
```
app2/
├── main.py                 # FastAPI backend (updated)
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   ├── style.css          # Premium CSS with animations
│   └── app.js             # JavaScript for API integration
├── Master_Activities.py   # All 67+ activities
├── assign_tasks.py        # Quest assignment logic
├── xp_system.py          # XP and level calculations
└── database.py           # MongoDB connection
```

### Key Technologies
- **Backend**: FastAPI, Python, MongoDB
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Styling**: Custom CSS with CSS Variables
- **Fonts**: Google Fonts (Inter)
- **No Framework**: Pure vanilla JS for maximum performance

## 🎯 XP System Details

### XP Rules
- **Every activity** = 10 XP (equal value)
- **Daily cap** = 10 times per activity per day
- **Level formula**: Linear progression (100 XP per level)
  - Level 1: 0-99 XP
  - Level 2: 100-199 XP
  - Level 3: 200-299 XP
  - And so on...

### Quest Rewards
- **Complete 5 tasks** = 10 LP (Loyalty Points)
- **Plus XP** from each activity (5 × 10 = 50 XP)
- **Total per quest** = 10 LP + 50 XP

## 🐛 Troubleshooting

### Page doesn't load
- Check if server is running: `uvicorn app2.main:app --reload --port 8001`
- Verify URL: `http://localhost:8001` (not 8000)

### Activities not showing
- Check browser console for errors (F12)
- Verify MongoDB connection in backend
- Ensure `/api/activities` endpoint works

### Quest not assigning
- Check User ID is valid (positive integer)
- Verify MongoDB is running
- Check backend logs for errors

### XP not updating
- Ensure activity name matches exactly
- Check daily cap (max 10 per activity)
- Verify user exists in database

## 🎉 Success Indicators

You'll know everything is working when you see:
- ✅ Beautiful gradient background with floating orbs
- ✅ Stats dashboard showing level and XP
- ✅ Quest panel with 5 tasks after clicking "Assign Quest"
- ✅ Activity dropdown populated with 67+ activities
- ✅ Toast notifications on successful actions
- ✅ Real-time progress updates
- ✅ Smooth animations and hover effects

## 🚀 Next Steps

1. **Test the frontend** - Open http://localhost:8001
2. **Assign a quest** - Click the button
3. **Log some activities** - Try different ones
4. **Watch your progress** - See XP and level increase
5. **Complete the quest** - Finish all 5 tasks
6. **Enjoy the experience** - Beautiful UI with smooth interactions!

---

**Built with ❤️ for the Bobo Gamification System**
