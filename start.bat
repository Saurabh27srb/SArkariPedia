@echo off
setlocal
title SarkariPedia - Indian Government Services Portal
color 0B

echo ========================================================
echo               SarkariPedia Platform
echo    National Directory of Indian Government Portals
echo ========================================================
echo.

:: 1. Verify Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not found in system PATH.
    echo Please install Python 3.10 or higher from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PY_VER=%%i
echo [*] %PY_VER% detected.

:: 2. Check and install dependencies
echo [*] Checking and verifying dependencies from requirements.txt...
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [WARNING] Dependency verification returned a non-zero code. Attempting to start anyway...
) else (
    echo [*] All dependencies are ready.
)

:: 3. Launch browser and web server
echo.
echo ========================================================
echo   Starting Web Server at http://localhost:8000
echo   Press Ctrl+C in this window to stop the server
echo ========================================================
echo.

:: Open browser automatically after a 2-second delay
start "" cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:8000"

:: Start the application
python -m app.main

echo.
echo Server has stopped.
pause
