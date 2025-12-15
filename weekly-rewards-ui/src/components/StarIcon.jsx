import React from 'react';

const StarIcon = ({ className }) => {
    return (
        <div
            className={className}
            style={{
                width: '100%',
                height: '100%',
                borderRadius: '50%',
                background: 'linear-gradient(135deg, #FFD700 0%, #FDB813 100%)',
                boxShadow: '0 2px 8px rgba(255, 215, 0, 0.4)'
            }}
        />
    );
};

export default StarIcon;
