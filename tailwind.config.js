// tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/templates/**/*.html", // Agrega esta línea
    "./**/static/**/*.js",      // Y esta, si usas JS para clases
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'), // <-- Agrega esta línea
  ],
}