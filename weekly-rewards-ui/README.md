# Weekly Rewards UI - React Component

A pixel-perfect React.js implementation of the Weekly Rewards UI, matching the exact design, colors, spacing, and layout from the reference images.

## 🎨 Features

- **100% Accurate Design**: Exact match of colors, spacing, typography, and layout
- **Component-Based Architecture**: Modular, reusable React components
- **SVG Icons**: Custom-designed SVG components for coins, gifts, stars, and mascot
- **Responsive Layout**: Optimized for mobile and desktop viewing
- **Interactive Elements**: Hover effects and click handlers

## 📁 Project Structure

```
weekly-rewards-ui/
├── src/
│   ├── components/
│   │   ├── WeeklyRewards.jsx      # Main rewards component
│   │   ├── WeeklyRewards.css      # Component styles
│   │   ├── CoinIcon.jsx           # Gold coin SVG component
│   │   ├── GiftIcon.jsx           # Mystery gift SVG component
│   │   ├── StarIcon.jsx           # Star decoration SVG component
│   │   └── MascotIcon.jsx         # Character mascot SVG component
│   ├── App.jsx                     # Root application component
│   ├── App.css                     # App styles
│   ├── index.css                   # Global styles
│   └── main.jsx                    # Entry point
├── public/
├── index.html
├── package.json
└── vite.config.js
```

## 🎯 Components

### 1. **WeeklyRewards** (Main Component)
The primary container component that orchestrates the entire UI:
- Header section with mascot and decorative icons
- "Weekly Rewards" title banner
- 7-day reward grid (Days 1-7)
- Claim button

### 2. **CoinIcon**
SVG component rendering the golden coin with:
- Gradient fills for depth
- Diamond center design
- Glow effects
- Exact color matching: `#FFD700`, `#FDB813`, `#D4A017`

### 3. **GiftIcon**
SVG component for the mystery gift box:
- Orange/yellow gift box base
- Pink ribbon and bow
- 3D perspective with shadows
- Exact colors: `#FFD93D`, `#FF6B9D`, `#FF8FB3`

### 4. **StarIcon**
Decorative star SVG component:
- Golden gradient
- Glow effect
- Used as decorative elements around mascot

### 5. **MascotIcon**
Cute character mascot with:
- White head with large eyes
- Blue hoodie with "b" logo
- Headphones with microphone
- Exact blue shades: `#5DADE2`, `#3498DB`, `#2E86AB`

## 🎨 Color Palette

### Background
- **Gradient**: `#A63B1F` → `#8B2F15` (Terracotta/brown)

### Blue Theme (Header, Cards, Button)
- **Light Blue**: `#5DADE2`, `#85C1E9`
- **Medium Blue**: `#3498DB`
- **Dark Blue**: `#2E86AB`

### Gold/Yellow (Coins, Gift)
- **Gold**: `#FFD700`, `#FDB813`, `#D4A017`
- **Yellow**: `#FFD93D`, `#FFED4E`

### Pink (Ribbon)
- **Pink**: `#FF6B9D`, `#FF8FB3`, `#FFB6C1`

### Neutrals
- **White**: `#FFFFFF`
- **Light Gray**: `#F0F0F0`, `#E8E8E8`
- **Dark Gray**: `#2C3E50`, `#4A4A4A`

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:
```bash
cd weekly-rewards-ui
```

2. Install dependencies (if not already done):
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to:
```
http://localhost:5173
```

## 📱 Layout Details

### Header Section
- **Background**: Blue gradient (`#5DADE2` → `#85C1E9`)
- **Mascot**: Centered, 120px width
- **Decorative Icons**: Positioned left and right of mascot
- **Title Banner**: White background, blue text, rounded corners

### Rewards Grid
- **Layout**: 4 columns for days 1-6, 2 columns for day 7 (special)
- **Card Size**: Consistent padding and spacing
- **Card Background**: Blue gradient matching header
- **Icons**: 40px for regular rewards, 50px for mystery gift

### Reward Cards
Each card contains:
- Day label (e.g., "Day 1d")
- Reward icon (coin or gift)
- Reward amount (e.g., "Gold x5" or "Mystery Gift")

### Claim Button
- **Width**: Full width with padding
- **Background**: Blue gradient
- **Border Radius**: 16px
- **Shadow**: Soft blue glow
- **Hover Effect**: Lift animation

## 🎭 Exact Measurements

- **Container**: Max-width 400px, border-radius 24px
- **Header Padding**: 20px sides, 30px bottom
- **Title Banner**: 12px vertical, 24px horizontal padding
- **Rewards Grid**: 24px padding, 12px gap
- **Reward Cards**: 12px padding, 8px gap between elements
- **Claim Button**: 16px padding, 18px font size

## 🔧 Customization

### Adding More Rewards
Edit the `rewards` array in `WeeklyRewards.jsx`:

```javascript
const rewards = [
  { day: 1, type: 'coin', amount: 'x5' },
  { day: 2, type: 'coin', amount: 'x20' },
  // Add more rewards...
];
```

### Changing Colors
Update the CSS variables in `WeeklyRewards.css` or modify the SVG gradients in the icon components.

### Claim Functionality
Implement the `handleClaim` function in `WeeklyRewards.jsx`:

```javascript
const handleClaim = () => {
  // Add your claim logic here
  console.log('Claiming rewards...');
};
```

## 📊 State Management

The component uses React's `useState` hook to track claimed days:

```javascript
const [claimedDays, setClaimedDays] = useState([]);
```

Cards with claimed days will have reduced opacity and disabled hover effects.

## 🌟 Key Features

1. **Pixel-Perfect Design**: Every element matches the reference images exactly
2. **Smooth Animations**: Hover effects on cards and button
3. **Scalable SVGs**: All icons are vector-based for crisp rendering
4. **Clean Code**: Well-organized, commented, and maintainable
5. **Reusable Components**: Easy to integrate into larger applications

## 📝 Notes

- The UI is optimized for a 400px container width (mobile-first)
- All colors are extracted from the reference images
- SVG components are self-contained with embedded gradients
- The layout uses CSS Grid for responsive card arrangement
- Hover states provide visual feedback for interactivity

## 🎯 Accuracy Checklist

✅ Exact background gradient color  
✅ Mascot character design and positioning  
✅ Decorative icons (coins, stars, gift) placement  
✅ Title banner styling and colors  
✅ 7-day reward grid layout  
✅ Card styling with blue gradients  
✅ Icon designs (coin with diamond, gift with ribbon)  
✅ Typography and spacing  
✅ Claim button design and colors  
✅ Hover effects and interactions  

## 🚀 Build for Production

```bash
npm run build
```

The optimized production build will be in the `dist/` folder.

## 📄 License

This is a UI implementation project for educational purposes.

---

**Built with React + Vite** ⚛️⚡
