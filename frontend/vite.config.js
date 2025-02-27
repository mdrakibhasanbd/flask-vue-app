import { fileURLToPath, URL } from 'node:url'
import dotenv from 'dotenv';
dotenv.config(); // Load environment variables from .env

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

const { VITE_API_URL } = process.env;


// https://vite.dev/config/
export default defineConfig({

  server: {
    port: 8080,
    proxy: {
      '/api/v1': {
        target: VITE_API_URL,
        changeOrigin: true,
      },
    },
      
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
