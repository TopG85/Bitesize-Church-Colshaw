module.exports = {
  safelist: ['bg-logo-red', 'navbar-red'],
  content: [
    './home/templates/**/*.html',
    './config/templates/**/*.html',
    './home/templates/home/home_page.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1F4D2E',        // deep green
        primarySoft: '#6E9B78',    // light green
        logoRed: '#B8351B',        // red from logo
      },
    },
  },
  plugins: [],
};
