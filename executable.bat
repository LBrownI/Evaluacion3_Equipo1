@echo off
if not exist ".venv/" (
    echo Seems like you dont have the envioremnt created!
    echo Please execute Setup.bat before the executable. This will create the envioremnt with his dependencies already installed.
    pause
    exit
)
echo Opening main...
call .venv\Scripts\activate.bat
python main.py