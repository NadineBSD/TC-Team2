/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
 
  theme: {
    extend: {
      fontFamily: {
        'custom': ['Roboto', 'sans-serif'],
        'roboto': ['Roboto', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
      },
      colors: {
        'color1': '#00ACE8',
        'color2': '#F3F6F9', 
        'color3': '#BFBFBF',
        'color4': '#F5F5F5', 
        'color5': '#D9D9D9', 
        'color6': '#FF4D4F',
        
        
        

      },
    },
  },
  plugins: [],
}