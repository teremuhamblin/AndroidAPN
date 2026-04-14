Utilisation ADB
===============

AndroidAPN permet d’exporter les APN d’un appareil Android.

Prérequis
---------

- ADB installé
- Mode développeur activé
- Débogage USB activé

Commande d’export
-----------------

.. code-block:: bash

    adb shell content query --uri content://telephony/carriers
