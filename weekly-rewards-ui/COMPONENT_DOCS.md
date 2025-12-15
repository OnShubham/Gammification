# Component Documentation

## WeeklyRewards Component Architecture

### Component Hierarchy

```
WeeklyRewards
├── Header Section
│   ├── Mascot Container
│   │   ├── Left Reward Icons (Coin + Star)
│   │   ├── Mascot Character
│   │   └── Right Reward Icons (Gift + Star)
│   └── Title Banner ("Weekly Rewards")
├── Rewards Grid
│   ├── Day 1 Card (Gold x5)
│   ├── Day 2 Card (Gold x20)
│   ├── Day 3 Card (Gold x25)
│   ├── Day 4 Card (Gold x30)
│   ├── Day 5 Card (Gold x35)
│   ├── Day 6 Card (Gold x40)
│   └── Day 7 Card (Mystery Gift - spans 2 columns)
└── Claim Button
```

## Detailed Measurements

### Container
- **Max Width**: 400px
- **Border Radius**: 24px
- **Background**: #FFFFFF
- **Box Shadow**: 0 8px 24px rgba(0, 0, 0, 0.15)

### Header Section
- **Background**: Linear gradient #5DADE2 → #85C1E9
- **Padding**: 20px (sides), 30px (bottom)
- **Border Radius**: 24px 24px 0 0

### Mascot
- **Width**: 120px
- **Height**: Auto (maintains aspect ratio)
- **Position**: Centered

### Decorative Icons
- **Coin Icon**: 40px × 40px
- **Star Icon**: 35px × 35px
- **Gift Icon**: 45px × 45px
- **Left Icons Position**: -30px from mascot, 20px from top
- **Right Icons Position**: -30px from mascot, 20px from top

### Title Banner
- **Background**: #FFFFFF
- **Padding**: 12px (vertical), 24px (horizontal)
- **Border Radius**: 12px
- **Box Shadow**: 0 4px 12px rgba(0, 0, 0, 0.1)
- **Font Size**: 24px
- **Font Weight**: 700
- **Color**: #85C1E9

### Rewards Grid
- **Padding**: 24px (all sides)
- **Grid Columns**: 4 (repeat)
- **Gap**: 12px
- **Day 7 Special**: Spans 2 columns

### Reward Card
- **Background**: Linear gradient #5DADE2 → #85C1E9
- **Border Radius**: 12px
- **Padding**: 12px (vertical), 8px (horizontal)
- **Box Shadow**: 0 2px 8px rgba(0, 0, 0, 0.1)
- **Gap**: 8px (between elements)

#### Day Label
- **Background**: rgba(255, 255, 255, 0.2)
- **Color**: #FFFFFF
- **Font Size**: 13px
- **Font Weight**: 600
- **Padding**: 4px (vertical), 12px (horizontal)
- **Border Radius**: 8px

#### Reward Icon Container
- **Width**: 50px
- **Height**: 50px
- **Background**: rgba(255, 255, 255, 0.3)
- **Border Radius**: 50% (circle)
- **Icon Size**: 40px × 40px

#### Special Card (Day 7)
- **Icon Container**: 60px × 60px
- **Icon Size**: 50px × 50px

#### Reward Amount
- **Color**: #FFFFFF
- **Font Size**: 12px
- **Font Weight**: 600

### Claim Button
- **Width**: 100%
- **Background**: Linear gradient #5DADE2 → #3498DB
- **Color**: #FFFFFF
- **Border**: None
- **Border Radius**: 16px
- **Padding**: 16px
- **Font Size**: 18px
- **Font Weight**: 700
- **Box Shadow**: 0 4px 12px rgba(93, 173, 226, 0.4)
- **Hover Shadow**: 0 6px 16px rgba(93, 173, 226, 0.5)
- **Hover Transform**: translateY(-2px)

## Color Reference

### Primary Blues
```css
--blue-light: #5DADE2;
--blue-lighter: #85C1E9;
--blue-medium: #3498DB;
--blue-dark: #2E86AB;
```

### Gold/Yellow
```css
--gold-bright: #FFD700;
--gold-medium: #FDB813;
--gold-dark: #D4A017;
--yellow-bright: #FFD93D;
--yellow-light: #FFED4E;
--yellow-pale: #FFF9E6;
```

### Pink (Ribbon)
```css
--pink-medium: #FF6B9D;
--pink-light: #FF8FB3;
--pink-pale: #FFB6C1;
```

### Orange (Gift)
```css
--orange-bright: #FF9500;
--orange-light: #FFB84D;
--orange-medium: #FFC107;
--orange-dark: #E8A03D;
```

### Neutrals
```css
--white: #FFFFFF;
--gray-lightest: #F0F0F0;
--gray-light: #E8E8E8;
--gray-medium: #D5D5D5;
--gray-dark: #4A4A4A;
--gray-darkest: #2C3E50;
```

### Background
```css
--bg-gradient-start: #A63B1F;
--bg-gradient-end: #8B2F15;
```

## SVG Icon Specifications

### CoinIcon
- **Outer Glow**: #FFF9E6 at 50% opacity, radius 48px
- **Main Ring**: Gradient #FFD700 → #FDB813 → #D4A017, radius 40px
- **Inner Ring**: Gradient #FFED4E → #FDB813, radius 35px
- **Diamond Center**: Gradient #FF9500 → #FFB84D → #FF9500
- **Highlight**: White ellipse at 40% opacity

### GiftIcon
- **Box Base**: Gradient #FFD93D → #FFC107 → #F5B84D
- **Box Sides**: #E8A03D (left), #F5B84D (right)
- **Ribbon**: Gradient #FF6B9D → #FF8FB3 → #FF6B9D
- **Bow**: Gradient #FF8FB3 → #FF6B9D
- **Bow Center**: #FF5A8A
- **Decorative Elements**: Yellow circles and pink triangles

### StarIcon
- **Outer Glow**: #FFF9E6 at 30% opacity, radius 45px
- **Main Star**: Gradient #FFED4E → #FFD700 → #FDB813
- **Inner Star**: #FFD700
- **Highlight**: White ellipse at 60% opacity

### MascotIcon
- **Head**: Gradient #FFFFFF → #F0F0F0, radius 60px
- **Eyes**: White ellipses 18px × 22px
- **Pupils**: #2C3E50 ellipses 12px × 16px
- **Hoodie**: Gradient #5DADE2 → #3498DB
- **Headphones**: Gradient #E8E8E8 → #D0D0D0 → #E8E8E8
- **Headphone Pads**: #2E86AB (outer), #5DADE2 (inner)
- **Microphone**: #4A4A4A (arm), #2C3E50 (tip)
- **Blush**: #FFB6C1 at 40% opacity

## State Management

### claimedDays State
```javascript
const [claimedDays, setClaimedDays] = useState([]);
```

**Purpose**: Track which days have been claimed

**Usage**:
- Add day to array when claimed
- Check if day is in array to apply "claimed" styling
- Claimed cards have 60% opacity and no hover effect

### Rewards Data Structure
```javascript
const rewards = [
  { day: 1, type: 'coin', amount: 'x5' },
  { day: 2, type: 'coin', amount: 'x20' },
  { day: 3, type: 'coin', amount: 'x25' },
  { day: 4, type: 'coin', amount: 'x30' },
  { day: 5, type: 'coin', amount: 'x35' },
  { day: 6, type: 'coin', amount: 'x40' },
  { day: 7, type: 'gift', amount: 'Mystery Gift', special: true }
];
```

## Animations & Interactions

### Hover Effects

#### Reward Card Hover
```css
transform: translateY(-2px);
transition: transform 0.2s ease;
```

#### Claim Button Hover
```css
transform: translateY(-2px);
box-shadow: 0 6px 16px rgba(93, 173, 226, 0.5);
transition: all 0.2s ease;
```

#### Claim Button Active
```css
transform: translateY(0);
```

### Disabled States

#### Claimed Card
```css
opacity: 0.6;
cursor: default;
/* No hover transform */
```

#### Disabled Button
```css
opacity: 0.5;
cursor: not-allowed;
/* No hover transform */
```

## Responsive Behavior

The component is designed for a maximum width of 400px and scales down gracefully on smaller screens. The grid layout automatically adjusts with the 4-column structure, and Day 7 always spans 2 columns.

## Integration Example

```javascript
import React from 'react';
import { WeeklyRewards } from './components';

function App() {
  return (
    <div className="App">
      <WeeklyRewards />
    </div>
  );
}

export default App;
```

## Customization Points

1. **Rewards Array**: Modify the rewards data structure
2. **Colors**: Update CSS variables or gradient definitions
3. **Claim Logic**: Implement handleClaim function
4. **Icons**: Replace SVG components with custom designs
5. **Grid Layout**: Adjust grid-template-columns for different layouts
6. **Animations**: Modify transition properties and transforms

## Browser Compatibility

- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid support required
- SVG support required
- ES6+ JavaScript features used

## Performance Notes

- All icons are inline SVGs (no external requests)
- CSS animations use transform (GPU-accelerated)
- Component uses React hooks for efficient state management
- No external dependencies beyond React
