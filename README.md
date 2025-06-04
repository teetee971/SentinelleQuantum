![Version stable](https://img.shields.io/badge/version-v1.0.0-blue.svg?style=for-the-badge&logo=github)
[![GitHub Release](https://img.shields.io/github/v/release/teetee971/SentinelleQuantum?style=for-the-badge)](https://github.com/teetee971/SentinelleQuantum/releases/latest)



<p align="center">
  <img src="https://raw.githubusercontent.com/teetee971/SentinelleQuantum/main/splash.png" width="400" alt="Sentinelle Splash">
</p>

# 🛡️ Sentinelle Quantum Vanguard AI Pro ![Build Status](https://github.com/teetee971/SentinelleQuantum/actions/workflows/build.yml/badge.svg)
# Sentinelle Quantum Vanguard AI Pro

[![Website](https://img.shields.io/badge/Site%20Web-SentinelleQuantum-blue?style=for-the-badge&logo=githubpages)](https://teetee971.github.io/SentinelleQuantum)
[![Télécharger .EXE](https://img.shields.io/badge/Télécharger-Windows%20Installer-blue?style=for-the-badge&logo=windows)](https://github.com/teetee971/SentinelleQuantum/releases/latest)
![Sécurité signée](https://img.shields.io/badge/Signature%20numérique-Démonstration%20OK-green?style=for-the-badge&logo=trustpilot)


Bienvenue dans le dépôt officiel de **Sentinelle Quantum Vanguard AI Pro**, un système de protection numérique avancé alliant intelligence artificielle, modules OSINT, sécurité vocale, et compilation Windows.

---

## 🔧 Fonctionnalités principales

- 🎯 Application sécurisée backend avec **Flask**
- 🧠 Modules IA : comportement prédictif, surveillance OSINT
- 🗣️ Synthèse vocale (fr/en/es) intégrée
- 🌐 Interface API locale `http://localhost:8080`
- 🖥️ Génération automatique de `.exe` et `.msi`
- 🔁 Workflow CI/CD avec GitHub Actions

---

## 🗂️ Structure du projet

| Fichier                           | Description |
|----------------------------------|-------------|
| `sentinelle_pc_flask.py`         | Script principal Flask |
| `Sentinelle.ico`                 | Icône officielle |
| `splash.png`                     | Splash screen |
| `build_exe.bat`                  | Compilation `.exe` via PyInstaller |
| `inno_setup.iss`                 | Script de setup Windows (Inno Setup) |
| `requirements.txt`               | Dépendances Python |
| `.github/workflows/build.yml`    | Automatisation de la compilation via GitHub Actions |

---

## 🔐 Modules intégrés

### 🔍 `module_osint.py` *(à venir)*
- Analyse des sources ouvertes, détection d'ingérences

### 🧠 `module_behavioral.py` *(à venir)*
- IA de prédiction comportementale (protection proactive)

### 🎙️ `vwa_sentinèl.py` *(prévu)*
- Synthèse vocale multilingue dynamique

---

## 📆 Roadmap (modules à venir)

- 🔒 `vpn_quantum.py` : tunnel chiffré hybride IA+quantique
- 🔬 `threat_scanner.py` : scanner réseau en temps réel
- 🌍 `geo_ai_alert.py` : alertes IA par zone géographique
- 🛰️ `remote_control_guard.py` : contrôle à distance sécurisé
- 🔔 `live_emergency_response.py` : module d’intervention immédiate

---

## ▶️ Lancer localement

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Lancer le backend :
```bash
python sentinelle_pc_flask.py
```

3. Ouvrir le navigateur sur :
[http://localhost:8080](http://localhost:8080)

---

## 🔁 Compilation `.exe`

1. Double-clique sur `build_exe.bat`
2. Fichier généré : `dist/sentinelle_pc_flask.exe`

---

## 🏗️ Compilation `.msi`

1. Ouvrir `inno_setup.iss` avec Inno Setup
2. Cliquer sur **Compiler** → fichier `.msi` généré

---

## 🚀 Déploiement CI/CD

Ce dépôt contient un workflow automatique :
- Compile le `.exe` à chaque push sur `main`
- Accessible depuis l’onglet **Actions**

---

## 📥 Téléchargement

Les fichiers `.exe` et `.msi` seront disponibles dans l’onglet [Releases](../../releases) dès publication.

---

## ✍️ Auteur

Développé par **Thierry Naud**  
🔗 Projet GitHub : [teetee971](https://github.com/teetee971)
