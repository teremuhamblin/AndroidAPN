#!/usr/bin/env python
import argparse
import logging
from androidapn.core import generate_apn_conf
import logging
from logging.config import fileConfig
from pathlib import Path

fileConfig("config/logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("androidapn")

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Générer un fichier apn.conf")
    parser.add_argument("--input", required=True, help="Fichier source APN")
    parser.add_argument("--output", required=True, help="Fichier de sortie apn.conf")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger.info("Génération du fichier APN...")
    generate_apn_conf(args.input, args.output)
    logger.info("Terminé.")

if __name__ == "__main__":
    main()
