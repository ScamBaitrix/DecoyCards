@echo off 
title DecoyCards GUI - Scambaiting Tool by Baitrix 
cd /d "%~dp0" 
python gift_card_generator.py --gui 
if %errorlevel% neq 0 ( 
    echo. 
    echo Something went wrong! Make sure you ran setup.bat first. 
    pause 
) 
