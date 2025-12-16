import React, { useState } from 'react';
import './UserProfile.css';

const UserProfile = () => {
    const [expandedSections, setExpandedSections] = useState({
        personalInfo: true,
        features1: false,
        features2: false,
        notifications: false,
        privacy: false,
        account: false,
        other: false
    });

    const [pushNotifications, setPushNotifications] = useState(true);

    const toggleSection = (section) => {
        setExpandedSections(prev => ({
            ...prev,
            [section]: !prev[section]
        }));
    };

    const userData = {
        name: "Lorem Ipsum",
        avatar: "/avatar.png",
        currentXP: 540,
        maxXP: 2000,
        streak: 1,
        xp: 270,
        rewards: "Rookie",
        personalInfo: {
            name: "Vedant Kumar",
            dob: "Feb 16, 1999",
            sex: "Male",
            bloodType: "O+",
            height: "5'2\"",
            weight: "66"
        }
    };

    return (
        <div className="profile-container">
            {/* Header */}
            <header className="profile-header">
                <div className="header-left">
                    <img src="/logo.png" alt="Hey Bobo" className="logo" />
                </div>
                <div className="header-center">
                    <div className="search-bar">
                        <svg className="search-icon" width="16" height="16" viewBox="0 0 16 16" fill="none">
                            <path d="M7.33333 12.6667C10.2789 12.6667 12.6667 10.2789 12.6667 7.33333C12.6667 4.38781 10.2789 2 7.33333 2C4.38781 2 2 4.38781 2 7.33333C2 10.2789 4.38781 12.6667 7.33333 12.6667Z" stroke="#999" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                            <path d="M14 14L11.1 11.1" stroke="#999" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                        <input type="text" placeholder="Type here..." />
                    </div>
                </div>
                <div className="header-right">
                    <button className="icon-button new-badge">
                        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                            <path d="M15 6.66667L10 11.6667L5 6.66667" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </button>
                    <button className="icon-button">
                        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                            <path d="M15 6.66667C15.9205 6.66667 16.6667 5.92048 16.6667 5C16.6667 4.07953 15.9205 3.33334 15 3.33334C14.0795 3.33334 13.3333 4.07953 13.3333 5C13.3333 5.92048 14.0795 6.66667 15 6.66667Z" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                            <path d="M5 12.5C5.92047 12.5 6.66667 11.7538 6.66667 10.8333C6.66667 9.91286 5.92047 9.16667 5 9.16667C4.07953 9.16667 3.33333 9.91286 3.33333 10.8333C3.33333 11.7538 4.07953 12.5 5 12.5Z" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </button>
                    <button className="icon-button">
                        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                            <circle cx="10" cy="10" r="8" stroke="white" strokeWidth="1.5"/>
                            <path d="M10 6V10L13 13" stroke="white" strokeWidth="1.5" strokeLinecap="round"/>
                        </svg>
                    </button>
                </div>
            </header>

            {/* Main Content */}
            <div className="profile-content">
                {/* Breadcrumb */}
                <div className="breadcrumb">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                        <path d="M8 14.6667C11.6819 14.6667 14.6667 11.6819 14.6667 8C14.6667 4.3181 11.6819 1.33333 8 1.33333C4.3181 1.33333 1.33333 4.3181 1.33333 8C1.33333 11.6819 4.3181 14.6667 8 14.6667Z" stroke="#00BFA6" strokeWidth="1.5"/>
                        <path d="M8 5.33333V8L10 10" stroke="#00BFA6" strokeWidth="1.5" strokeLinecap="round"/>
                    </svg>
                    <span className="breadcrumb-text">Account</span>
                </div>

                {/* User Profile Card */}
                <div className="user-card">
                    <div className="user-avatar">
                        <img src="/avatar.png" alt={userData.name} />
                        <div className="avatar-badge">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                                <circle cx="12" cy="12" r="10" fill="#FFD700"/>
                                <path d="M12 7L13.5 10.5L17 11L14.5 13.5L15 17L12 15L9 17L9.5 13.5L7 11L10.5 10.5L12 7Z" fill="white"/>
                            </svg>
                        </div>
                    </div>
                    <h2 className="user-name">{userData.name}</h2>
                    
                    {/* XP Progress Bar */}
                    <div className="xp-progress">
                        <div className="xp-bar-container">
                            <div className="xp-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                                    <circle cx="12" cy="12" r="10" fill="#FFD700"/>
                                    <text x="12" y="16" textAnchor="middle" fill="#fff" fontSize="12" fontWeight="bold">★</text>
                                </svg>
                            </div>
                            <div className="xp-bar">
                                <div 
                                    className="xp-fill" 
                                    style={{ width: `${(userData.currentXP / userData.maxXP) * 100}%` }}
                                ></div>
                            </div>
                        </div>
                        <div className="xp-text">{userData.currentXP}/{userData.maxXP} XP</div>
                    </div>
                </div>

                {/* Stats Cards */}
                <div className="stats-grid">
                    <div className="stat-card">
                        <div className="stat-icon streak">
                            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                                <path d="M16 4L18 12L24 8L20 16L28 16L18 24L20 28L16 20L12 28L14 24L4 16L12 16L8 8L14 12L16 4Z" fill="#4FC3F7"/>
                            </svg>
                        </div>
                        <div className="stat-label">{userData.streak} Day Streak</div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon xp">
                            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                                <circle cx="16" cy="16" r="12" fill="#5C6BC0"/>
                                <text x="16" y="21" textAnchor="middle" fill="#fff" fontSize="14" fontWeight="bold">XP</text>
                            </svg>
                        </div>
                        <div className="stat-label">{userData.xp} XP</div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon reward">
                            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                                <path d="M16 2L18 10L26 10L20 15L22 23L16 18L10 23L12 15L6 10L14 10L16 2Z" fill="#FFB74D"/>
                            </svg>
                        </div>
                        <div className="stat-label">{userData.rewards}</div>
                    </div>
                </div>

                {/* Personal Information Section */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('personalInfo')}>
                        <h3>Personal Information</h3>
                        <svg 
                            className={`chevron ${expandedSections.personalInfo ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.personalInfo && (
                        <div className="section-content">
                            <div className="info-row">
                                <span className="info-label">Name</span>
                                <span className="info-value">{userData.personalInfo.name}</span>
                            </div>
                            <div className="info-row">
                                <span className="info-label">Date of Birth</span>
                                <span className="info-value">{userData.personalInfo.dob}</span>
                            </div>
                            <div className="info-row">
                                <span className="info-label">Sex</span>
                                <span className="info-value">{userData.personalInfo.sex}</span>
                            </div>
                            <div className="info-row">
                                <span className="info-label">Blood type</span>
                                <span className="info-value">{userData.personalInfo.bloodType}</span>
                            </div>
                            <div className="info-row">
                                <span className="info-label">Height</span>
                                <span className="info-value">{userData.personalInfo.height}</span>
                            </div>
                            <div className="info-row">
                                <span className="info-label">Weight</span>
                                <span className="info-value">{userData.personalInfo.weight}</span>
                            </div>
                        </div>
                    )}
                </div>

                {/* Features Section 1 */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('features1')}>
                        <h3>Features</h3>
                        <svg 
                            className={`chevron ${expandedSections.features1 ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.features1 && (
                        <div className="section-content">
                            <div className="feature-item">Health</div>
                            <div className="feature-item">Education</div>
                            <div className="feature-item">Coparenting</div>
                            <div className="feature-item">Dietary</div>
                            <div className="feature-item">Fitness</div>
                        </div>
                    )}
                </div>

                {/* Features Section 2 */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('features2')}>
                        <h3>Features</h3>
                        <svg 
                            className={`chevron ${expandedSections.features2 ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.features2 && (
                        <div className="section-content">
                            <div className="feature-item">Health</div>
                            <div className="feature-item">Education</div>
                            <div className="feature-item">Coparenting</div>
                            <div className="feature-item">Dietary</div>
                            <div className="feature-item">Fitness</div>
                        </div>
                    )}
                </div>

                {/* Notification Section */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('notifications')}>
                        <h3>Notification</h3>
                        <svg 
                            className={`chevron ${expandedSections.notifications ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.notifications && (
                        <div className="section-content">
                            <div className="notification-row">
                                <span className="notification-label">Push Notification</span>
                                <label className="toggle-switch">
                                    <input 
                                        type="checkbox" 
                                        checked={pushNotifications}
                                        onChange={() => setPushNotifications(!pushNotifications)}
                                    />
                                    <span className="toggle-slider"></span>
                                </label>
                            </div>
                        </div>
                    )}
                </div>

                {/* Privacy & Legal Terms Section */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('privacy')}>
                        <h3>Privacy & Legal Terms</h3>
                        <svg 
                            className={`chevron ${expandedSections.privacy ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.privacy && (
                        <div className="section-content">
                            <div className="feature-item">Apps</div>
                            <div className="feature-item">Devices</div>
                            <div className="feature-item">Terms</div>
                        </div>
                    )}
                </div>

                {/* Account Section */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('account')}>
                        <h3>Account</h3>
                        <svg 
                            className={`chevron ${expandedSections.account ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.account && (
                        <div className="section-content">
                            <div className="feature-item">Log Out</div>
                            <div className="feature-item">Delete Account</div>
                        </div>
                    )}
                </div>

                {/* Other Section */}
                <div className="info-section">
                    <div className="section-header" onClick={() => toggleSection('other')}>
                        <h3>Other</h3>
                        <svg 
                            className={`chevron ${expandedSections.other ? 'expanded' : ''}`}
                            width="20" 
                            height="20" 
                            viewBox="0 0 20 20" 
                            fill="none"
                        >
                            <path d="M5 7.5L10 12.5L15 7.5" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                    </div>
                    {expandedSections.other && (
                        <div className="section-content">
                            <div className="feature-item">Rate Wishings</div>
                            <div className="feature-item">Share the App</div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default UserProfile;
