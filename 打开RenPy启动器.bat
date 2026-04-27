@echo off
setlocal

for %%I in ("%~dp0.") do set "PROJECT_DIR=%%~fI"
for %%I in ("%~dp0..") do set "WORKSPACE_DIR=%%~fI"
set "RENPY_EXE=%WORKSPACE_DIR%\renpy-8.5.2-sdk\renpy.exe"

if not exist "%RENPY_EXE%" (
    echo RenPy not found:
    echo %RENPY_EXE%
    pause
    exit /b 1
)

start "" "%RENPY_EXE%" launcher set_project "%PROJECT_DIR%"
exit /b 0
