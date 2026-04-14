import logging
from pathlib import Path
import yaml

logger = logging.getLogger("androidapn")

def generate_apn_conf(input_file: Path, output_file: Path):
    """
    Génère un fichier apn.conf à partir d'un fichier source YAML.
    """
    logger.info("Lecture du fichier source APN...")

    with open(input_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    logger.info("Génération du fichier apn.conf...")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Fichier APN généré par AndroidAPN\n\n")
        f.write("[APN]\n")
        for key, value in data.items():
            f.write(f"{key}={value}\n")

    logger.info("Fichier apn.conf généré avec succès.")
