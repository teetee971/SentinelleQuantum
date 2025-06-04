#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Point d’entrée principal pour Sentinel Quantum Vanguard AI Pro
"""

import logging
import sqlite3
from pathlib import Path
from modules.audio_guardian import MicrophoneProtector
from modules.cognitive_shield import ContentAnalyzer

# Configuration basique
config = {
    "audio_unauthorized_access_block": True,
    "audio_auto_mute_suspicious": True,
    "audio_privacy_mode": True,
    "audio_level_analysis": True,
    "cognitive_manipulation_detection": True,
    "cognitive_auto_block": True,
    "cognitive_user_warnings": True,
    "cognitive_visual_analysis": True
}

# Initialisation logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SentinelMain")

# Création ou connexion à la base de données
db_path = Path("sentinel_data.db")
db_conn = sqlite3.connect(str(db_path))

# Initialisation des modules
audio_guardian = MicrophoneProtector(config, logger, db_conn)
cognitive_shield = ContentAnalyzer(config, logger, db_conn)

# Lancement des modules
logger.info("Démarrage des modules Sentinel...")
audio_guardian.start()
cognitive_shield.start()

# Maintien en exécution
try:
    while True:
        pass
except KeyboardInterrupt:
    logger.info("Arrêt de Sentinel...")
    audio_guardian.stop()
    cognitive_shield.stop()
    db_conn.close()
