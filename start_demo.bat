@echo off
echo ========================================================
echo   AI Project Idea Generator + Evaluator - Demo Startup
echo ========================================================
echo.
echo [1] Starting Backend API Server (FastAPI)...
start cmd /k "cd backend && call venv\Scripts\activate.bat && python main.py"

echo [2] Starting Frontend UI (React)...
start cmd /k "cd frontend && npm start"

echo.
echo Servers are starting up!
echo - Backend will be available at: http://localhost:3000/docs
echo - Frontend will be available at: http://localhost:3001
echo.
echo Have a great presentation!
