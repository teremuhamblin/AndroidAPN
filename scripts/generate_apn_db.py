#!/usr/bin/env python
import argparse
import logging
from logging.config import fileConfig
from pathlib import Path

from androidapn.core import generate_apn_conf

# ---------------------------------------------------------
# Initialisation du logging via config/logging.conf
# (intégration de TA partie de code, mais version robuste)
# ---------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
LOGGING_CONF = ROOT_DIR / "config" / "logging.conf"

fileConfig(LOGGING_CONF, disable_existing_loggers=False)
logger = logging.getLogger("androidapn")
# ---------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Générer un fichier apn.conf")
    parser.add_argument("--input", required=True, help="Fichier source APN")
    parser.add_argument("--output", required=True, help="Fichier de sortie apn.conf")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        logger.error(f"Le fichier source n'existe pas : {input_path}")
        raise FileNotFoundError(f"Source APN introuvable : {input_path}")

    logger.info("--------------------------------------------------")
    logger.info(" Génération du fichier APN")
    logger.info("--------------------------------------------------")
    logger.info(f"Source : {input_path}")
    logger.info(f"Destination : {output_path}")

    try:
        generate_apn_conf(input_path, output_path)
        logger.info("Génération terminée avec succès.")
    except Exception as e:
        logger.exception("Erreur lors de la génération du fichier APN")
        raise e


if __name__ == "__main__":
    main()
