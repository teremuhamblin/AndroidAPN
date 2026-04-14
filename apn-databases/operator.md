# ALL OPERATORS — FRANCE
Index global des opérateurs français et MVNO
============================================

Ce document liste tous les opérateurs français et leurs fichiers APN
au format YAML standardisé AndroidAPN.

Structure du dossier :
- apn-database/france/<operateur>.yaml
- apn-database/france/mvno/<operateur>.yaml

---

## 🇫🇷 Opérateurs principaux

### Orange France
- Fichier : `france/orange.yaml`
- MCC : 208
- MNC : 01
- Types : data, MMS, SUPL

### SFR
- Fichier : `france/sfr.yaml`
- MCC : 208
- MNC : 10
- Types : data, MMS, SUPL

### Bouygues Telecom
- Fichier : `france/bouygues.yaml`
- MCC : 208
- MNC : 20
- Types : data, MMS, SUPL

### Free Mobile
- Fichier : `france/free.yaml`
- MCC : 208
- MNC : 15
- Types : data, MMS, SUPL

---

## 🇫🇷 MVNO (Réseaux virtuels)

### NRJ Mobile
- Fichier : `france/mvno/nrj-mobile.yaml`
- Réseau hôte : Bouygues / Orange / SFR (selon SIM)
- MCC : 208
- MNC : 26

### CIC Mobile
- Fichier : `france/mvno/cic-mobile.yaml`
- Réseau hôte : Bouygues / SFR
- MCC : 208
- MNC : 26

### Auchan Telecom
- Fichier : `france/mvno/auchan-telecom.yaml`
- Réseau hôte : Bouygues / SFR
- MCC : 208
- MNC : 26

### La Poste Mobile
- Fichier : `france/mvno/la-poste-mobile.yaml`
- Réseau hôte : SFR
- MCC : 208
- MNC : 10

### Prixtel
- Fichier : `france/mvno/prixtel.yaml`
- Réseau hôte : SFR / Orange (selon offre)
- MCC : 208
- MNC : 10

---

## 📦 Format YAML utilisé

Tous les fichiers APN suivent ce format :

```yaml
name: <Nom opérateur>
apn: <apn>
mcc: <code pays>
mnc: <code opérateur>
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc:
mmsproxy:
mmsport:
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
