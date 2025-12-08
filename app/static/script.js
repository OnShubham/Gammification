let currentUserId = localStorage.getItem('user_id');

async function setUserId() {
    const userId = document.getElementById('user-id-input').value.trim();

    if (!userId) {
        alert('Please enter a User ID');
        return;
    }

    try {
        // Create or get user
        const response = await fetch(`/api/user/create?user_id=${encodeURIComponent(userId)}`, {
            method: 'POST'
        });

        if (response.ok) {
            const user = await response.json();
            currentUserId = userId;
            localStorage.setItem('user_id', userId);
            showApp(user);
            // Automatically check in after setting user ID
            await autoCheckIn();
        } else {
            alert('Failed to create/get user');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
}

async function loadUser() {
    if (!currentUserId) {
        showUserIdInput();
        return;
    }

    try {
        const response = await fetch(`/api/user/${encodeURIComponent(currentUserId)}`);

        if (response.ok) {
            const user = await response.json();
            showApp(user);
            // Automatically check in after loading user
            await autoCheckIn();
        } else {
            // User not found, show input
            changeUser();
        }
    } catch (error) {
        console.error('Error:', error);
        changeUser();
    }
}

async function checkIn() {
    const localDate = new Date().toISOString().split('T')[0];

    try {
        const response = await fetch('/api/checkin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: currentUserId,
                local_date: localDate
            }),
        });

        if (response.ok) {
            const user = await response.json();
            updateUI(user);
        } else {
            alert('Check-in failed. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during check-in.');
    }
}

async function autoCheckIn() {
    const localDate = new Date().toISOString().split('T')[0];

    try {
        const response = await fetch('/api/checkin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: currentUserId,
                local_date: localDate
            }),
        });

        if (response.ok) {
            const user = await response.json();
            updateUI(user);
            console.log('Auto check-in successful');
        }
    } catch (error) {
        console.error('Auto check-in error:', error);
    }
}

function updateUI(user) {
    document.getElementById('streak-count').textContent = user.current_streak;
    document.getElementById('longest-streak').textContent = user.longest_streak;
    document.getElementById('last-checkin').textContent = user.last_checkin_date || "Never";
    document.getElementById('display-user-id').textContent = user.user_id;

    // Update counting streaks
    const countingStreaks = user.counting_streaks || 0;
    document.getElementById('counting-streaks').textContent = countingStreaks;

    // Update milestone badges
    const milestones = [3, 7, 14, 30, 60, 90, 180, 365];
    const regularStreaks = user.regular_streaks || {};
    const milestonesGrid = document.getElementById('milestones-grid');

    milestonesGrid.innerHTML = ''; // Clear existing badges

    milestones.forEach(milestone => {
        const milestoneKey = `${milestone}_day`;
        const count = regularStreaks[milestoneKey] || 0;
        const isAchieved = count > 0;

        const badge = document.createElement('div');
        badge.className = `milestone-badge ${isAchieved ? 'achieved' : ''}`;

        badge.innerHTML = `
            <div class="milestone-day">${milestone}</div>
            <div class="milestone-label">DAYS</div>
            ${isAchieved ? `<div class="milestone-count">×${count}</div>` : ''}
        `;

        milestonesGrid.appendChild(badge);
    });

    const btn = document.getElementById('checkin-btn');
    const today = new Date().toISOString().split('T')[0];

    if (user.last_checkin_date === today) {
        btn.textContent = "Checked In Today ✓";
        btn.disabled = true;
    } else {
        btn.textContent = "Check In Now";
        btn.disabled = false;
    }
}

function showUserIdInput() {
    document.getElementById('user-id-card').style.display = 'block';
    document.getElementById('app-card').style.display = 'none';
}

function showApp(user) {
    document.getElementById('user-id-card').style.display = 'none';
    document.getElementById('app-card').style.display = 'block';
    updateUI(user);
}

function changeUser() {
    currentUserId = null;
    localStorage.removeItem('user_id');
    document.getElementById('user-id-input').value = '';
    showUserIdInput();
}

// Check for user ID on load
window.onload = loadUser;
