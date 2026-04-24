# Frontend React README

## Overview

React-based user interface for the AI Project Idea Generator. Built with Tailwind CSS for styling and real-time components for dynamic interactions.

## Features

- **Clean, Modern UI**: Dark-themed interface with gradient accents
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Tab-based Navigation**: Switch between Ideas, Scoring, Tech Stack, and Recommendations
- **Real-time Feedback**: Loading states and error handling
- **Component-based Architecture**: Modular, reusable components

## Project Structure

```
frontend/
├── src/
│   ├── api.js                    # API client (axios)
│   ├── App.js                    # Main application component
│   ├── index.js                  # React entry point
│   ├── index.css                 # Global styles
│   └── components/
│       ├── IdeaCard.js           # Displays individual ideas
│       ├── ScoringCard.js        # Shows scoring metrics
│       └── TechStackCard.js      # Displays tech recommendations
├── public/
│   └── index.html               # HTML template
├── package.json                 # Dependencies and scripts
├── tailwind.config.js           # Tailwind configuration
└── postcss.config.js            # PostCSS configuration
```

## Setup

### Install Dependencies

```bash
npm install
```

### Environment Variables

Create `.env.local` in the frontend directory:

```env
REACT_APP_API_URL=http://localhost:3000
```

### Development Server

```bash
npm start
```

App runs on http://localhost:3000

### Production Build

```bash
npm run build
```

Optimized build in `build/` directory

## Components

### App (Main)

- Handles form input (domain and context)
- Manages evaluation state
- Displays results with tab navigation
- Error handling and loading states

### IdeaCard

Displays:
- Idea title and description
- Use case and potential impact
- Complexity score and difficulty level
- Development time estimate

### ScoringCard

Displays:
- Feasibility score
- Innovation score
- Market potential score
- Overall composite score
- Score breakdown with reasoning

### TechStackCard

Displays:
- Technology recommendations by category
- Reason for each recommendation
- Color-coded by category (Backend, Frontend, etc.)

## Styling

Uses **Tailwind CSS** with custom configuration:

- Dark theme (slate, purple, pink gradient)
- Responsive grid system
- Custom animations
- Accessible color contrast

### Color Palette

- **Primary**: Purple (#7c3aed)
- **Secondary**: Pink (#ec4899)
- **Background**: Slate-900 (#0f172a)
- **Accent**: Gradient (purple → pink)

## API Integration

API client in `src/api.js`:

```javascript
import { evaluateDomain, healthCheck } from './api';

// Evaluate a domain
const result = await evaluateDomain('Healthcare AI', 'Optional context');

// Check API health
const health = await healthCheck();
```

## State Management

Uses React hooks for state:

- `domain`: Input domain string
- `context`: Optional context
- `loading`: Loading indicator
- `error`: Error messages
- `evaluation`: Complete evaluation result
- `activeTab`: Current tab view

## Loading & Error States

### Loading State

- Button shows spinner with "Generating Ideas..."
- Button is disabled
- Previous results remain visible

### Error State

- Red error box with message
- User can retry without clearing forms
- Network errors are caught and displayed

## Performance Optimization

1. **Component Memoization**: Use React.memo for cards
2. **Code Splitting**: Lazy load components if needed
3. **Image Optimization**: SVG icons via lucide-react
4. **CSS Optimization**: Tailwind purges unused styles

## Responsive Design

```css
/* Mobile-first approach */
/* Base styles (mobile) */

/* sm: 640px */
/* md: 768px */
/* lg: 1024px */
/* xl: 1280px */
```

Grid layouts adjust responsively:
- Mobile: Single column
- Tablet: 1-2 columns
- Desktop: 2+ columns

## Accessibility

- Semantic HTML
- ARIA labels for interactive elements
- Keyboard navigation support
- Color contrast ratios ≥ 4.5:1

## Browser Support

- Chrome/Edge ≥ 90
- Firefox ≥ 88
- Safari ≥ 14

## Dependencies

- **react**: UI library
- **react-dom**: DOM rendering
- **axios**: HTTP client
- **tailwindcss**: Utility CSS
- **lucide-react**: Icon library

## Scripts

```bash
npm start         # Development server
npm run build     # Production build
npm test          # Run tests
npm run eject     # Expose config (one-way!)
```

## Customization

### Change API URL

Edit `.env.local`:
```env
REACT_APP_API_URL=https://api.example.com
```

### Change Colors

Edit `tailwind.config.js`:
```javascript
colors: {
  purple: {
    600: '#your-color'
  }
}
```

### Add New Components

1. Create `src/components/YourComponent.js`
2. Import in `App.js`
3. Add to appropriate tab or section

## Deployment

### Vercel (Recommended)

```bash
npm install -g vercel
vercel --prod
```

### Netlify

```bash
npm run build
# Deploy build/ folder to Netlify
```

### GitHub Pages

Set `homepage` in package.json:
```json
{
  "homepage": "https://username.github.io/project"
}
```

## Troubleshooting

### API Connection Failed

```javascript
// Check .env.local has correct URL
REACT_APP_API_URL=http://localhost:3000

// Restart development server
npm start
```

### Styles Not Loading

```bash
# Rebuild Tailwind
npm run build
```

### Module Not Found

```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

## Development Tips

1. **Hot Reload**: Changes auto-reload in browser
2. **React DevTools**: Install extension for debugging
3. **Console**: Check browser console for errors
4. **Network Tab**: Monitor API requests

## Testing

```bash
# Run tests
npm test

# Run with coverage
npm test -- --coverage

# E2E tests with Cypress
npm install cypress
npx cypress open
```

## Build Optimization

```bash
# Analyze bundle size
npm install -g netlify-cli
npx source-map-explorer 'build/static/js/*.js'
```

## Environment-Specific Builds

### Development

```bash
npm start
```

### Production

```bash
npm run build
# Optimized, minified, source maps removed
```

---

**Happy coding! 🚀**

Questions? See [README.md](../README.md) for full documentation.
