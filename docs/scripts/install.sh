#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "[+] Installation des dépendances Python..."
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt || true

echo "[+] Installation terminée."
