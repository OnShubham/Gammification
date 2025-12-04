// Example: How to display the new streak fields in your frontend

// After successful check-in or when fetching user data:
async function displayStreakStats(userData) {
    // Display current and longest streaks (already implemented)
    document.getElementById('current-streak').textContent = userData.current_streak;
    document.getElementById('longest-streak').textContent = userData.longest_streak;

    // NEW: Display total milestone achievements
    document.getElementById('total-milestones').textContent = userData.counting_streaks;

    // NEW: Display individual milestone achievements
    const regularStreaks = userData.regular_streaks || {};
    const milestonesList = document.getElementById('milestones-list');
    milestonesList.innerHTML = '';

    // Define milestone badges
    const milestones = [
        { days: 3, emoji: '🔥', name: '3-Day Streak' },
        { days: 7, emoji: '⭐', name: 'Week Warrior' },
        { days: 14, emoji: '💪', name: 'Two Weeks Strong' },
        { days: 30, emoji: '🏆', name: 'Monthly Master' },
        { days: 60, emoji: '💎', name: 'Diamond Dedication' },
        { days: 90, emoji: '👑', name: 'Quarterly Champion' },
        { days: 180, emoji: '🎯', name: 'Half-Year Hero' },
        { days: 365, emoji: '🌟', name: 'Yearly Legend' }
    ];

    // Display earned milestones
    milestones.forEach(milestone => {
        const key = `${milestone.days}_day`;
        const count = regularStreaks[key] || 0;

        if (count > 0) {
            const badge = document.createElement('div');
            badge.className = 'milestone-badge earned';
            badge.innerHTML = `
                <span class="emoji">${milestone.emoji}</span>
                <span class="name">${milestone.name}</span>
                <span class="count">×${count}</span>
            `;
            milestonesList.appendChild(badge);
        } else {
            // Show locked milestones
            const badge = document.createElement('div');
            badge.className = 'milestone-badge locked';
            badge.innerHTML = `
                <span class="emoji-locked">🔒</span>
                <span class="name">${milestone.name}</span>
            `;
            milestonesList.appendChild(badge);
        }
    });

    // Show progress to next milestone
    const currentStreak = userData.current_streak;
    const nextMilestone = milestones.find(m => m.days > currentStreak);

    if (nextMilestone) {
        const daysRemaining = nextMilestone.days - currentStreak;
        document.getElementById('next-milestone').innerHTML = `
            <p>Next milestone: <strong>${nextMilestone.name}</strong></p>
            <p>Only <strong>${daysRemaining}</strong> more day(s) to go! ${nextMilestone.emoji}</p>
        `;
    } else {
        document.getElementById('next-milestone').innerHTML = `
            <p>🌟 You've reached the highest milestone! Keep going!</p>
        `;
    }
}

// Example HTML structure to add to your page:
/*
<div class="streak-stats">
    <div class="stat-card">
        <h3>Current Streak</h3>
        <p id="current-streak" class="big-number">0</p>
    </div>

    <div class="stat-card">
        <h3>Longest Streak</h3>
        <p id="longest-streak" class="big-number">0</p>
    </div>

    <div class="stat-card">
        <h3>Total Milestones</h3>
        <p id="total-milestones" class="big-number">0</p>
    </div>
</div>

<div class="milestones-section">
    <h2>Your Achievements</h2>
    <div id="milestones-list" class="milestones-grid"></div>
</div>

<div id="next-milestone" class="next-milestone"></div>
*/

// Example CSS for styling:
/*
.milestone-badge {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}

.milestone-badge.earned {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.milestone-badge.locked {
    background: #f0f0f0;
    color: #999;
    opacity: 0.6;
}

.milestone-badge .emoji {
    font-size: 2em;
}

.milestone-badge .count {
    margin-left: auto;
    background: rgba(255, 255, 255, 0.3);
    padding: 5px 10px;
    border-radius: 20px;
    font-weight: bold;
}

.big-number {
    font-size: 3em;
    font-weight: bold;
    color: #667eea;
}
*/
