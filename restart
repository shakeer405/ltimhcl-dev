@echo off
setlocal

:: Check if a process prefix is provided
if "%~1"=="" (
    echo Usage: restart_process.bat ProcessPrefix
    exit /b
)

set PROCESS_PREFIX=%~1

echo Searching for process starting with "%PROCESS_PREFIX%"...

:: Find and stop matching processes
for /f "tokens=1" %%A in ('tasklist ^| findstr /i "^%PROCESS_PREFIX%"') do (
    echo Stopping %%A...
    taskkill /F /IM %%A 2>nul
    set PROCESS_NAME=%%A
)

:: If no process was found, exit
if "%PROCESS_NAME%"=="" (
    echo No process found with prefix "%PROCESS_PREFIX%".
    exit /b
)

echo Waiting for 5 seconds...
timeout /t 5 /nobreak >nul
