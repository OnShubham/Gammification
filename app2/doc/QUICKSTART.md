# 🚀 Quick Start Guide - App2 Frontend

## ⚡ Get Started in 3 Steps

### Step 1: Verify Server is Running
Your server should already be running on port **8001**. If not, run:
```bash
uvicorn app2.main:app --reload --port 8001
```

### Step 2: Open Your Browser
Navigate to:
```
http://localhost:8001
```

### Step 3: Start Using!
1. **Assign Quest** - Click the purple button
2. **Select Activity** - Choose from dropdown
3. **Log Activity** - Click the green button
4. **Watch Progress** - See XP and quest progress update!

---

## 🎯 What You'll See

### Beautiful Interface ✨
- Gradient background with floating orbs
- Glassmorphism cards
- Smooth animations
- Modern design

### Your Stats 📊
- **Level** - Your current level
- **Total XP** - All XP earned
- **Progress** - % to next level

### Daily Quest 📋
- 5 random tasks
- Progress tracker (X/5)
- Task descriptions
- Completion rewards

### Activity Logger ⚡
- 67+ activities to choose from
- Descriptions for each
- Real-time XP updates
- Toast notifications

---

## 💡 Quick Tips

### First Time?
1. Keep User ID as **1**
2. Click **"Assign Quest"**
3. You'll get 5 tasks to complete

### Logging Activities
1. Select any activity from dropdown
2. Read the description
3. Click **"Log Activity"**
4. Get **+10 XP** instantly!

### Completing Quests
- Complete **5 different tasks**
- Earn **10 LP** reward
- Get **50 XP** total (5 × 10)
- Quest auto-completes!

### Leveling Up
- Every **100 XP** = 1 Level
- Level 1: 0-99 XP
- Level 2: 100-199 XP
- And so on...

---

## 🎮 Example Session

```
1. Open http://localhost:8001
2. Click "Assign Quest"
   → Get 5 tasks

3. Log "Hydration Hit"
   → +10 XP (1/5 tasks)

4. Log "Meal Peek"
   → +10 XP (2/5 tasks)

5. Log "Quick Stretch"
   → +10 XP (3/5 tasks)

6. Log "AI Food Scan"
   → +10 XP (4/5 tasks)

7. Log "Doubt Buster"
   → +10 XP (5/5 tasks)
   → Quest Complete! 🎉
   → Earned 10 LP!
```

---

## 🎨 Features at a Glance

✅ **No Login Required** - Just enter User ID  
✅ **Real-time Updates** - Instant feedback  
✅ **Beautiful Design** - Premium UI/UX  
✅ **All Activities** - 67+ to choose from  
✅ **Quest System** - Daily challenges  
✅ **XP & Levels** - Gamification  
✅ **Progress Tracking** - Visual feedback  
✅ **Responsive** - Works on all devices  

---

## 🐛 Troubleshooting

### Page Won't Load?
- Check server is on port **8001** (not 8000)
- URL: `http://localhost:8001`

### No Activities in Dropdown?
- Check browser console (F12)
- Verify MongoDB is running

### XP Not Updating?
- Check activity name is correct
- Daily cap: 10 per activity
- Verify user exists

---

## 📚 Need More Help?

- **Full Guide**: See `FRONTEND_GUIDE.md`
- **API Docs**: See `API_REFERENCE.md`
- **Summary**: See `IMPLEMENTATION_SUMMARY.md`

---

## 🎊 That's It!

**You're ready to go!** Just open the URL and start earning XP! 🚀

---

**Built with ❤️ for Bobo Gamification**
