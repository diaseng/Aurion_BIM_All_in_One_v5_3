# 🚀 Aurion BIM Suite — ALL-IN-ONE v5.3

## Backend (Render + Docker)
- Configure o serviço no Render com root `apps/backend`.
- Use variáveis: `ENVIRONMENT=production`, `PORT=10000`, `DATABASE_URL=<Neon>`.
- Deploy automático via `.github/workflows/render_backend.yml`.

## Banco de Dados (Neon)
- Crie instância Postgres gratuita.
- Copie a URL `postgresql+asyncpg://...` e salve no Render como `DATABASE_URL`.

## Frontend (Vercel + Vite)
- Importar repositório GitHub com root `apps/frontend`.
- Install command: `npm install`
- Build command: `npm run build`
- Output: `dist`
- Variável: `VITE_API_URL=https://<seu_backend>.onrender.com`

## CI/CD (GitHub Actions)
- Workflows:
  - `render_backend.yml` → Deploy automático no Render.
  - `vercel_frontend.yml` → Deploy automático na Vercel.

## Pós-deploy
- Teste `/health/ping` no backend.
- Verifique viewer IFC.js no frontend.
- Métricas: `/metrics` via Prometheus FastAPI Instrumentator.

© 2025 Cleber Antonio Dias | CPF: 082.414.406-69 | Email: cleberdiasx10@gmail.com
License: All Rights Reserved
