# Gamification XP & Level System

## 1. Overview
This system awards **Fixed XP** for every activity and uses a **Linear Arithmetic Formula** for levels.
It is designed to be simple: **Every 10 Activities = 1 Level Up.**

## 2. XP Rules
- **Value:** 10 XP per Activity.
- **Rules:** The specific activity type does NOT matter. All activities are treated equally.
- **Daily Limit:** There is a daily cap (default: 10 times per specific activity) to prevent abuse.

## 3. Level Formula
We use a simple **Linear Arithmetic Progression**.

**Formula:**
`Level = (Total_XP / 100) + 1`

**Milestones:**
- **Level 1:** 0 - 99 XP (0 - 9 Activities)
- **Level 2:** 100 - 199 XP (10 - 19 Activities)
- **Level 3:** 200 - 299 XP (20 - 29 Activities)
- **Level 10:** 900 XP

## 4. Recalculation
If you have old logs, you can rebuild the XP/Levels using the batch script:
```powershell
python -m app2.recalculate_xp
```
This counts *every* log in the database (subject to the new 10 XP value) and updates the user.

## 5. Usage in Code
The calculation is handled in `app2/xp_system.py`:
```python
FIXED_XP_PER_ACTIVITY = 10
XP_PER_LEVEL = 100
level = (total_xp // XP_PER_LEVEL) + 1
```
