import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: { 
    host: true,
    port: 3000,
    proxy: {
      "/api": { 
        target: "https://8000-...cloudworkstations.dev",
        changeOrigin: true,
        secure: false,
      }
    }
  }
})
