let token = localStorage.getItem('token');

async function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);

    try {
        const response = await fetch('/token', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            token = data.access_token;
            localStorage.setItem('token', token);
            loadUser();
        } else {
            alert('Login failed');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;

    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            alert('Registration successful! Please login.');
            showLogin();
        } else {
            const data = await response.json();
            alert(data.detail || 'Registration failed');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadUser() {
    if (!token) {
        showLogin();
        return;
    }

    try {
        const response = await fetch('/api/user/me', {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (response.ok) {
            const user = await response.json();
            showApp(user);
        } else {
            logout();
        }
    } catch (error) {
        console.error('Error:', error);
        logout();
    }
}

async function checkIn() {
    const localDate = new Date().toISOString().split('T')[0];

    try {
        const response = await fetch('/api/checkin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ local_date: localDate }),
        });

        if (response.ok) {
            const user = await response.json();
            updateUI(user);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function updateUI(user) {
    document.getElementById('streak-count').textContent = user.current_streak;
    document.getElementById('longest-streak').textContent = user.longest_streak;
    document.getElementById('last-checkin').textContent = user.last_checkin_date || "Never";
    document.getElementById('display-username').textContent = user.username;

    const btn = document.getElementById('checkin-btn');
    const today = new Date().toISOString().split('T')[0];

    if (user.last_checkin_date === today) {
        btn.textContent = "Checked In Today";
        btn.disabled = true;
    } else {
        btn.textContent = "Check In Now";
        btn.disabled = false;
    }
}

function showLogin() {
    document.getElementById('login-card').style.display = 'block';
    document.getElementById('register-card').style.display = 'none';
    document.getElementById('app-card').style.display = 'none';
}

function showRegister() {
    document.getElementById('login-card').style.display = 'none';
    document.getElementById('register-card').style.display = 'block';
    document.getElementById('app-card').style.display = 'none';
}

function showApp(user) {
    document.getElementById('login-card').style.display = 'none';
    document.getElementById('register-card').style.display = 'none';
    document.getElementById('app-card').style.display = 'block';
    updateUI(user);
}

function logout() {
    token = null;
    localStorage.removeItem('token');
    showLogin();
}

// Check for token on load
window.onload = loadUser;
