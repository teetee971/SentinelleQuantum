# 🛡️ Quantum Reflex - Module d'Urgence Automatique

Ce module fait partie de la suite **Sentinelle Quantum Vanguard AI Pro**. Il est dédié à la **réponse automatique face aux menaces critiques** détectées sur le système.

---

## 🔍 Fonctionnalités principales

- **Analyse comportementale intelligente** (ThreatAnalyzer)
- **Réponse autonome en temps réel** (EmergencyResponseEngine)
- Lockdown système, isolation réseau, gel de processus, capture forensique
- **Snapshots du système** pour rollback
- **Base de données SQLite** pour journalisation des événements
- Mode automatique ou manuel configurable

---

## 📦 Structure

```
quantum_reflex/
├── reflex_engine.py       # Moteur principal
├── __init__.py            # Initialisation du module
├── demo.py                # Démo CLI rapide
└── README.md              # Documentation
```

---

## ▶️ Lancer une démonstration

```bash
python demo.py
```

---

## 🧠 Dépendances

- `psutil`
- `Pillow`
- `pywin32` *(Windows uniquement)*
