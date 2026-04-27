@echo off
setlocal

for %%I in ("%~dp0.") do set "PROJECT_DIR=%%~fI"
set "PYTHON_EXE=C:\Users\28100\Desktop\renpy-8.5.2-sdk\lib\py3-windows-x86_64\python.exe"
set "RENPY_PY=C:\Users\28100\Desktop\renpy-8.5.2-sdk\renpy.py"

if not exist "%PYTHON_EXE%" (
    echo Python runtime not found:
    echo %PYTHON_EXE%
    pause
    exit /b 1
)

if not exist "%RENPY_PY%" (
    echo renpy.py not found:
    echo %RENPY_PY%
    pause
    exit /b 1
)

"%PYTHON_EXE%" "%RENPY_PY%" "%PROJECT_DIR%" run
set "ERR=%ERRORLEVEL%"

if not "%ERR%"=="0" (
    echo.
    echo Launch failed. Exit code: %ERR%
    pause
)

exit /b %ERR%
