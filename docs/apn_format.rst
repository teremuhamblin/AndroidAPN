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

Mise à jour : (YAML)
====================

Le format APN utilisé par AndroidAPN est simple, lisible et portable.

Exemple minimal
---------------

.. code-block:: yaml

    name: Orange F
    apn: orange
    mcc: 208
    mnc: 01
    type: default,supl

Champs disponibles
------------------

- name : Nom de l’APN
- apn : Identifiant APN
- mcc : Mobile Country Code
- mnc : Mobile Network Code
- type : default, mms, supl, dun, etc.
- proxy, port, user, password, etc.
