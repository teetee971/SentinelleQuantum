# Sentinel Quantum Vanguard AI Pro

Sentinel Quantum Vanguard AI Pro est un logiciel de cybersécurité et de protection cognitive avancée intégrant :
- 🧠 Détection de manipulation cognitive (phishing, scareware, etc.)
- 🔊 Surveillance du microphone et anomalies audio
- 👁️ Analyse visuelle OCR contre les faux popups
- ⚙️ Blocage automatisé des menaces et alertes utilisateur

## 🛠 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/SentinelQuantumVanguardAIPro.git
cd SentinelQuantumVanguardAIPro
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Compilation Windows (.exe)
```bash
pyinstaller sentinel_main.spec
```

## 📁 Structure
- `main.py` : point d’entrée (à adapter selon votre architecture)
- `sentinel_main.spec` : configuration de build PyInstaller
- `assets/icon.ico` : icône personnalisée
- `README.md`, `.gitignore`, `requirements.txt`

## 📦 Release automatique
Lancez :
```bash
git tag v1.0.0
git push origin v1.0.0
```
Une release GitHub avec l'exécutable `.exe` sera générée automatiquement si GitHub Actions est activé.

---
© 2025 Sentinel Quantum Vanguard AI Pro - Tous droits réservés