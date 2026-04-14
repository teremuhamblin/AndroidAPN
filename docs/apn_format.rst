===========
Format APN
===========

Un fichier APN contient les paramètres nécessaires à la configuration réseau d'un opérateur.

Exemple
-------

.. code-block:: ini

   [APN]
   name=ExampleAPN
   mcc=208
   mnc=01
   apn=example.fr
   type=default,supl
   protocol=IPV4V6

Champs courants
---------------

- **name** : nom de l'APN
- **mcc/mnc** : identifiants opérateur
- **apn** : point d'accès
- **type** : usages (default, mms, supl…)
- **protocol** : IPV4, IPV6, IPV4V6
