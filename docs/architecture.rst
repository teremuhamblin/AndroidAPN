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
