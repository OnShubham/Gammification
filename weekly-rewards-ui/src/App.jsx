import React, { useState } from 'react';
import WeeklyRewards from './components/WeeklyRewards';
import UserProfile from './components/UserProfile';
import './App.css';

function App() {
  const [currentView, setCurrentView] = useState('profile'); // 'profile' or 'rewards'

  return (
    <div className="App">
      <div className="view-toggle">
        <button
          className={currentView === 'profile' ? 'active' : ''}
          onClick={() => setCurrentView('profile')}
        >
          User Profile
        </button>
        <button
          className={currentView === 'rewards' ? 'active' : ''}
          onClick={() => setCurrentView('rewards')}
        >
          Weekly Rewards
        </button>
      </div>

      {currentView === 'profile' ? <UserProfile /> : <WeeklyRewards />}
    </div>
  );
}

export default App;
