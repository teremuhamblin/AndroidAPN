Architecture
============

Vue d'ensemble
--------------

- Module ``androidapn.core`` : logique principale.
- Dossier ``config/`` : fichiers de configuration APN.
- Dossier ``scripts/`` : outils CLI.

Flux
----

1. L'utilisateur fournit des sources APN.
2. Le script génère ``apn.conf``.
3. L'application Android ou l'outil consomme ce fichier.

Mise à jour 
============

Le projet est organisé en modules indépendants :

androidapn/
    Module principal Python (validation, génération, parsing)

docs/
    Documentation complète du projet

examples/
    Exemples d’APN au format YAML

scripts/
    Scripts utilitaires (export ADB, conversion)

Structure logique
-----------------

- Parser YAML → Objet APN
- Validateur APN (schéma)
- Générateur APN Android
- Export ADB (optionnel)
