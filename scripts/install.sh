#!/usr/bin/env bash

# Donner les droits necessaires pour l'installation  
# chmod +x scripts/install.sh
# ./scripts/install.sh

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "[+] Installation des dépendances Python..."
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt || true

echo "[+] Installation terminée."
