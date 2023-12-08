@echo off
echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Virtual environment created and activated.

echo.
echo Installing dependencies...

python.exe -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo All dependencies have been sucsessfully installed.
pause
exit