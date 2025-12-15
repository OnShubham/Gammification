import React, { useState } from 'react';
import './WeeklyRewards.css';
import CoinIcon from './CoinIcon';
import GiftIcon from './GiftIcon';

const WeeklyRewards = () => {
    const [claimedDays, setClaimedDays] = useState([]);

    const rewards = [
        { day: 1, type: 'coin', amount: 'x5' },
        { day: 2, type: 'coin', amount: 'x20' },
        { day: 3, type: 'coin', amount: 'x25' },
        { day: 4, type: 'coin', amount: 'x30' },
        { day: 5, type: 'coin', amount: 'x35' },
        { day: 6, type: 'coin', amount: 'x40' },
        { day: 7, type: 'gift', amount: 'Mystery Gift', special: true }
    ];

    const handleClaim = () => {
        // Logic to claim rewards
        console.log('Claim button clicked');
    };

    return (
        <div className="weekly-rewards-container">
            <div className="header-section">
                <img src="/header-logo.png" alt="Weekly Rewards" className="header-logo" />
            </div>

            <div className="rewards-grid">
                {rewards.map((reward) => (
                    <div
                        key={reward.day}
                        className={`reward-card ${reward.special ? 'special' : ''} ${claimedDays.includes(reward.day) ? 'claimed' : ''
                            }`}
                    >
                        <div className="day-label">Day {reward.day}d</div>
                        <div className="reward-icon-container">
                            {reward.type === 'coin' ? (
                                <CoinIcon />
                            ) : (
                                <GiftIcon />
                            )}
                        </div>
                        <div className="reward-amount">
                            {reward.type === 'coin' ? `Gold ${reward.amount}` : reward.amount}
                        </div>
                    </div>
                ))}
            </div>

            <div className="claim-button-container">
                <button className="claim-button" onClick={handleClaim}>
                    Claim
                </button>
            </div>
        </div>
    );
};

export default WeeklyRewards;
