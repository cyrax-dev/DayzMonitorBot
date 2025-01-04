@echo off
color 0A
chcp 65001 > nul

echo Creating venv...
echo ---------------------------------
python -m venv .venv
cls

echo Activation venv...
echo ---------------------------------
call .venv\Scripts\activate.bat
cls

echo Updating pip
echo ---------------------------------
python.exe -m pip install --upgrade pip
cls

echo Updating Libs...
echo ---------------------------------
pip install -r requirements.txt
cls

python -B run.py
pause
