"""
Configuration for Tailwind CSS
"""

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        slate: {
          900: '#0f172a',
          800: '#1e293b',
          700: '#334155',
          600: '#475569',
          500: '#64748b',
          400: '#94a3b8',
          300: '#cbd5e1',
        },
        purple: {
          600: '#7c3aed',
          500: '#a855f7',
          400: '#c084fc',
        },
        pink: {
          600: '#ec4899',
          500: '#f43f5e',
        },
      },
      animation: {
        spin: 'spin 1s linear infinite',
      },
    },
  },
  plugins: [],
}
