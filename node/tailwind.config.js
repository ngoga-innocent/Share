/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./../**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#5A67D8',
          DEFAULT: '#00B0FF',
          dark: '#434190',
        },
        secondary: {
          light: '#F687B3',
          DEFAULT: '#ED64A6',
          dark: '#D53F8C',
        },
        accent: '#FF4081',
        background: '#F2F2F2',
        text:'#333333'
      },
    },
    fontFamily: {
      // 'sans': ['"Proxima Nova"', ...defaultTheme.fontFamily.sans],
    },
  },
  plugins: [],
}

