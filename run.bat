@echo off
cd /d %~dp0

echo ========================================
echo   News Classifier - Starting App
echo ========================================

IF NOT EXIST "venv" (
    python -m venv venv
)

venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install streamlit pandas scikit-learn numpy

IF EXIST requirements.txt (
    venv\Scripts\python.exe -m pip install -r requirements.txt
)

IF NOT EXIST "models" (
    mkdir models
)

IF NOT EXIST "models\model.pkl" (
    echo Training model...
    venv\Scripts\python.exe src\train_model.py
)

venv\Scripts\python.exe -m streamlit run app.py

pause