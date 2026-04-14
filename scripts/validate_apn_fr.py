#!/usr/bin/env python3
import os
import yaml
import json
from jsonschema import validate, ValidationError
from rich import print
from rich.table import Table

BASE_DIR = "apn-database/france"
SCHEMA_FILE = "config/apn_schema.json"

def load_schema():
    with open(SCHEMA_FILE, "r") as f:
        return json.load(f)

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def validate_file(path, schema):
    try:
        data = load_yaml(path)
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Erreur de parsing YAML : {e}"

def main():
    schema = load_schema()
    table = Table(title="Validation APN France")
    table.add_column("Fichier", style="cyan")
    table.add_column("Statut", style="green")
    table.add_column("Détails", style="red")

    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".yaml"):
                path = os.path.join(root, file)
                ok, msg = validate_file(path, schema)
                if ok:
                    table.add_row(path, "[green]OK[/green]", "")
                else:
                    table.add_row(path, "[red]FAIL[/red]", msg)

    print(table)

if __name__ == "__main__":
    main()
