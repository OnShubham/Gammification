// ===== STATE MANAGEMENT =====
let currentUserId = 1;
let currentActivities = {};
let currentQuest = null;
let userStats = null;

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
});

function initializeApp() {
    // Load activities
    loadActivities();

    // Load user stats
    loadUserStats();

    // Set initial user ID
    const userIdInput = document.getElementById('userId');
    currentUserId = parseInt(userIdInput.value);
}

function setupEventListeners() {
    // User ID change
    document.getElementById('userId').addEventListener('change', (e) => {
        currentUserId = parseInt(e.target.value);
        loadUserStats();
        loadQuestStatus();
    });

    // Assign Quest button
    document.getElementById('assignQuestBtn').addEventListener('click', assignQuest);

    // Activity selection
    document.getElementById('activitySelect').addEventListener('change', (e) => {
        const activityName = e.target.value;
        updateActivityDescription(activityName);
        document.getElementById('logActivityBtn').disabled = !activityName;
    });

    // Log Activity button
    document.getElementById('logActivityBtn').addEventListener('click', logActivity);
}

// ===== API CALLS =====

async function loadActivities() {
    try {
        const response = await fetch('/api/activities');
        const data = await response.json();
        currentActivities = data.activities;
        populateActivityDropdown();
    } catch (error) {
        console.error('Error loading activities:', error);
        showToast('❌ Failed to load activities', 'error');
    }
}

async function loadUserStats() {
    // Since we don't have a dedicated user stats endpoint, we'll update this when logging activities
    // For now, we'll just show placeholder values
    updateStatsDisplay({
        current_level: '--',
        total_xp: '--',
        xp_progress: '--'
    });
}

async function assignQuest() {
    const btn = document.getElementById('assignQuestBtn');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="loading"></span> Assigning...';
    btn.disabled = true;

    try {
        const response = await fetch(`/quests/${currentUserId}/assign`, {
            method: 'POST'
        });

        if (!response.ok) throw new Error('Failed to assign quest');

        const data = await response.json();
        currentQuest = data.quest;

        displayQuest(data);
        showToast('🎯 Quest assigned successfully!', 'success');

        // Populate activity dropdown with only the assigned tasks
        populateActivityDropdownFromQuest(data.quest);

        // Load quest status to get progress
        loadQuestStatus();
    } catch (error) {
        console.error('Error assigning quest:', error);
        showToast('❌ Failed to assign quest', 'error');
    } finally {
        btn.innerHTML = originalText;
        btn.disabled = false;
    }
}

async function loadQuestStatus() {
    try {
        const response = await fetch(`/quests/${currentUserId}/status`);

        if (!response.ok) {
            // No quest found
            document.getElementById('questStatus').innerHTML =
                '<p class="quest-message">Click "Assign Quest" to get started!</p>';
            document.getElementById('questProgress').style.display = 'none';
            document.getElementById('tasksList').innerHTML = '';
            return;
        }

        const data = await response.json();
        displayQuest(data);
        updateQuestProgress(data.progress);

        // Populate activity dropdown with quest tasks
        populateActivityDropdownFromQuest(data.quest_details || data.quest);
    } catch (error) {
        console.error('Error loading quest status:', error);
    }
}

async function logActivity() {
    const activitySelect = document.getElementById('activitySelect');
    const activityName = activitySelect.value;

    if (!activityName) {
        showToast('⚠️ Please select an activity', 'warning');
        return;
    }

    const btn = document.getElementById('logActivityBtn');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="loading"></span> Logging...';
    btn.disabled = true;

    try {
        const response = await fetch('/log_activity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: currentUserId,
                activity_name: activityName
            })
        });

        if (!response.ok) throw new Error('Failed to log activity');

        const data = await response.json();

        // Update UI with results
        displayActivityResult(data);

        // Update XP stats if available
        if (data.xp_update) {
            updateStatsDisplay({
                current_level: data.xp_update.new_level,
                total_xp: data.xp_update.new_total_xp,
                xp_progress: data.xp_update.stats.xp_progress_percent
            });
            updateXPProgress(data.xp_update.stats);
        }

        // Update quest progress
        if (data.quest_status) {
            updateQuestProgress(data.quest_status);

            // Check if quest completed
            if (data.quest_status.status === 'QUEST_COMPLETE') {
                showToast('🎉 Quest Complete! ' + data.quest_status.message, 'success');
                // Reload quest status to show completion
                setTimeout(() => loadQuestStatus(), 1000);
            } else {
                showToast(`✅ Activity logged! +${data.xp_update?.xp_gained || 10} XP`, 'success');
            }
        }

        // Reset activity selection
        activitySelect.value = '';
        document.getElementById('activityDescription').innerHTML =
            '<p class="description-text">Select an activity to see its description</p>';
        btn.disabled = true;

    } catch (error) {
        console.error('Error logging activity:', error);
        showToast('❌ Failed to log activity', 'error');
    } finally {
        btn.innerHTML = originalText;
    }
}

// ===== UI UPDATE FUNCTIONS =====

function populateActivityDropdown() {
    const select = document.getElementById('activitySelect');
    select.innerHTML = '<option value="">-- Assign a quest first --</option>';
}

function populateActivityDropdownFromQuest(quest) {
    const select = document.getElementById('activitySelect');
    const tasks = quest.tasks || [];

    // Clear existing options
    select.innerHTML = '<option value="">-- Choose a task to log --</option>';

    // Add only the assigned quest tasks
    tasks.forEach(task => {
        const option = document.createElement('option');
        option.value = task.name;
        option.textContent = task.name;
        select.appendChild(option);
    });
}

function updateActivityDescription(activityName) {
    const descriptionDiv = document.getElementById('activityDescription');

    if (!activityName) {
        descriptionDiv.innerHTML = '<p class="description-text">Select an activity to see its description</p>';
        return;
    }

    const activity = currentActivities[activityName];
    if (activity) {
        descriptionDiv.innerHTML = `<p class="description-text">${activity.description}</p>`;
    }
}

function displayQuest(data) {
    const questDetails = data.quest_details || data.quest;
    const tasks = questDetails.tasks || [];
    const status = questDetails.status;

    // Update quest status message
    const statusDiv = document.getElementById('questStatus');
    if (status === 'Complete') {
        statusDiv.innerHTML = `
            <p class="quest-message" style="border-left-color: var(--success);">
                ✅ Quest completed! Reward: ${questDetails.reward_lp || 10} LP
            </p>
        `;
    } else {
        statusDiv.innerHTML = `
            <p class="quest-message">
                📋 Complete 5 tasks to earn ${questDetails.reward_lp || 10} LP!
            </p>
        `;
    }

    // Display tasks
    const tasksList = document.getElementById('tasksList');
    tasksList.innerHTML = '';

    tasks.forEach((task, index) => {
        const taskItem = document.createElement('div');
        taskItem.className = 'task-item';
        taskItem.innerHTML = `
            <div class="task-header">
                <div class="task-checkbox">${status === 'Complete' ? '✓' : ''}</div>
                <div class="task-name">${task.name}</div>
            </div>
            <div class="task-description">${task.description}</div>
        `;
        tasksList.appendChild(taskItem);
    });
}

function updateQuestProgress(progress) {
    if (!progress) return;

    const progressDiv = document.getElementById('questProgress');
    const progressCount = document.getElementById('progressCount');
    const progressFill = document.getElementById('questProgressFill');

    const completed = progress.completed || 0;
    const total = 5;
    const percentage = (completed / total) * 100;

    progressDiv.style.display = 'block';
    progressCount.textContent = `${completed}/${total}`;
    progressFill.style.width = `${percentage}%`;
}

function updateStatsDisplay(stats) {
    document.getElementById('userLevel').textContent = stats.current_level;
    document.getElementById('totalXP').textContent = stats.total_xp;
    document.getElementById('xpProgress').textContent =
        stats.xp_progress !== '--' ? `${stats.xp_progress}%` : '--';
}

function updateXPProgress(stats) {
    const currentLevelLabel = document.getElementById('currentLevelLabel');
    const xpProgressLabel = document.getElementById('xpProgressLabel');
    const xpProgressFill = document.getElementById('xpProgressFill');

    currentLevelLabel.textContent = `Level ${stats.current_level}`;
    xpProgressLabel.textContent = `${stats.xp_in_current_level} / ${stats.xp_target_next_level - (stats.current_level - 1) * 100} XP`;
    xpProgressFill.style.width = `${stats.xp_progress_percent}%`;
}

function displayActivityResult(data) {
    const resultDiv = document.getElementById('activityResult');
    const xpUpdate = data.xp_update;
    const questStatus = data.quest_status;

    let resultHTML = '<div class="result-success">';
    resultHTML += '<div class="result-title">✅ Activity Logged Successfully!</div>';
    resultHTML += '<div class="result-details">';

    if (xpUpdate) {
        resultHTML += `<p>🎯 XP Gained: +${xpUpdate.xp_gained}</p>`;
        resultHTML += `<p>💎 Total XP: ${xpUpdate.new_total_xp}</p>`;
        resultHTML += `<p>⭐ Level: ${xpUpdate.new_level}</p>`;
    }

    if (questStatus) {
        if (questStatus.status === 'QUEST_COMPLETE') {
            resultHTML += `<p>🎉 ${questStatus.message}</p>`;
        } else if (questStatus.status === 'IN_PROGRESS') {
            resultHTML += `<p>📊 Quest Progress: ${questStatus.completed}/5 tasks completed</p>`;
        }
    }

    resultHTML += '</div></div>';

    resultDiv.innerHTML = resultHTML;
    resultDiv.style.display = 'block';

    // Hide after 5 seconds
    setTimeout(() => {
        resultDiv.style.display = 'none';
    }, 5000);
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    const toastIcon = document.getElementById('toastIcon');
    const toastMessage = document.getElementById('toastMessage');

    // Set icon based on type
    const icons = {
        success: '✅',
        error: '❌',
        warning: '⚠️',
        info: 'ℹ️'
    };

    toastIcon.textContent = icons[type] || icons.success;
    toastMessage.textContent = message;

    // Show toast
    toast.classList.add('show');

    // Hide after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// ===== AUTO-LOAD QUEST ON PAGE LOAD =====
setTimeout(() => {
    loadQuestStatus();
}, 500);
