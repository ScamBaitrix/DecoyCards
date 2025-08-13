@echo off
title DecoyCards - Easy Setup by Baitrix
color 0A

echo.
echo  ====================================
echo   DecoyCards - Easy Setup by Baitrix
echo  ====================================
echo.
echo  This will install everything you need!
echo.
echo  WARNING: This makes FAKE gift card codes
echo  for scambaiting only!
echo.
pause

echo.
echo [1/4] Checking if Python is installed...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Python not found! Please install Python 3.7+ from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

python --version
echo Python found!

echo.
echo [2/4] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [3/4] Installing required packages...
python -m pip install customtkinter requests playsound3

echo.
echo [4/4] Creating launcher scripts...
echo Creating GUI launcher...
echo @echo off > start_gui.bat
echo title DecoyCards GUI - Scambaiting Tool by Baitrix >> start_gui.bat
echo cd /d "%%~dp0" >> start_gui.bat
echo python gift_card_generator.py --gui >> start_gui.bat
echo if %%errorlevel%% neq 0 ( >> start_gui.bat
echo     echo. >> start_gui.bat
echo     echo Something went wrong! Make sure you ran setup.bat first. >> start_gui.bat
echo     pause >> start_gui.bat
echo ^) >> start_gui.bat

echo Creating CLI launcher...
echo @echo off > start_cli.bat
echo title DecoyCards CLI - Scambaiting Tool by Baitrix >> start_cli.bat
echo cd /d "%%~dp0" >> start_cli.bat
echo python gift_card_generator.py >> start_cli.bat
echo if %%errorlevel%% neq 0 ( >> start_cli.bat
echo     echo. >> start_cli.bat
echo     echo Something went wrong! Make sure you ran setup.bat first. >> start_cli.bat
echo     pause >> start_cli.bat
echo ^) >> start_cli.bat

echo.
echo  ====================================
echo   Setup Complete!
echo  ====================================
echo.
echo  DecoyCards is ready to use!
echo.
echo  TO START:
echo  - Double-click "start_gui.bat" for easy interface
echo  - Double-click "start_cli.bat" for menu version
echo.
echo  REMEMBER: These are FAKE codes for scambaiting only!
echo.
pause
