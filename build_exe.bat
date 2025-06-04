
@echo off
title Compilation - Sentinelle Quantum Vanguard AI Pro

echo ===============================
echo 🛠️ COMPILATION EN COURS...
echo Fichier source : sentinelle_pc_flask.py
echo Icône : Sentinelle.ico
echo ===============================

REM Installer PyInstaller si besoin
pip install pyinstaller

REM Compilation avec icône intégrée
pyinstaller --onefile --noconsole --icon=Sentinelle.ico sentinelle_pc_flask.py

echo.
if exist dist\sentinelle_pc_flask.exe (
    echo ✅ Compilation réussie ! Fichier créé : dist\sentinelle_pc_flask.exe
) else (
    echo ❌ Erreur : le fichier EXE n'a pas été généré.
)

pause
