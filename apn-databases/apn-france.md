##### Base APN FRANCE complète, en YAML, avec toutes les explications.
> Basé sur les données officielles des opérateurs français
- Orange, SFR, Bouygues, Free et leurs MVNO.  
> Les paramètres proviennent des pages d’assistance officielles :  
- SFR (Assistance SFR)   
- Free Mobile (Assistance Free)   
- Bouygues Telecom (Assistance Bouygues)   

---

### 📁 Editer en 1 seul fichier markdown
#### 👉 Opérateur FR et MVNO

```markdown
apn-database/
└── france/
    ├── README.md
    ├── orange.yaml
    ├── sfr.yaml
    ├── bouygues.yaml
    ├── free.yaml
    ├── mvno/
    │   ├── cic-mobile.yaml
    │   ├── nrj-mobile.yaml
    │   ├── la-poste-mobile.yaml
    │   ├── auchan-telecom.yaml
    │   └── prixtel.yaml
```

---

## 🇫🇷 FRANCE
> APN France — Base officielle AndroidAPN
-Ce dossier contient les APN officiels des opérateurs français au format YAML standardisé AndroidAPN.

>Sources officielles :
- Orange France
- SFR (Assistance SFR)
- Bouygues Telecom (Assistance Bouygues)
- Free Mobile (Assistance Free)

>MVNO inclus :
- NRJ Mobile
- CIC Mobile
- Auchan Telecom
- La Poste Mobile
- Prixtel

##### Format utilisé : YAML normalisé AndroidAPN.

---

### 🇫🇷 ORANGE — orange.yaml

```rst
name: Orange France
apn: orange
mcc: 208
mnc: 01
type: default,supl
proxy:
port:
user:
password:
server:
mmsc: http://mms.orange.fr
mmsproxy: 192.168.10.200
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 SFR — sfr.yaml
(données issues de l’assistance SFR) 

```rst
name: SFR
apn: sl2sfr
mcc: 208
mnc: 10
type: default,supl
proxy:
port:
user:
password:
server:
mmsc: http://mms1
mmsproxy: 10.151.0.1
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 BOUYGUES TELECOM — bouygues.yaml
(données issues de l’assistance Bouygues) 

```rst
name: Bouygues Telecom
apn: mmsbouygtel.com
mcc: 208
mnc: 20
type: default,mms,supl
proxy:
port:
user:
password:
server:
mmsc: http://mms.bouyguestelecom.fr/mms/wapenc
mmsproxy:
mmsport:
auth_type: PAP
protocol: IPv6
roaming_protocol: IPv4
carrier_enabled: true
```

---

### 🇫🇷 FREE MOBILE — free.yaml
(données issues de l’assistance Free) 

```rst
name: Free Mobile
apn: free
mcc: 208
mnc: 15
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc: http://mms.free.fr
mmsproxy:
mmsport:
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 MVNO — NRJ Mobile (exemple) — nrj-mobile.yaml

```rst
name: NRJ Mobile
apn: fnetnrj
mcc: 208
mnc: 26
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc: http://mmsnrj
mmsproxy: 10.143.156.5
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 MVNO — CIC Mobile — cic-mobile.yaml

```rst
name: CIC Mobile
apn: fnetcic
mcc: 208
mnc: 26
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc: http://mmscic
mmsproxy: 10.143.156.5
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 MVNO — La Poste Mobile — la-poste-mobile.yaml

```rst
name: La Poste Mobile
apn: sl2sfr
mcc: 208
mnc: 10
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc: http://mms1
mmsproxy: 10.151.0.1
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 MVNO — Auchan Telecom — auchan-telecom.yaml

```rst
name: Auchan Telecom
apn: fnetfr
mcc: 208
mnc: 26
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc: http://mmsnrj
mmsproxy: 10.143.156.5
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🇫🇷 MVNO — Prixtel — prixtel.yaml

```tst
name: Prixtel
apn: sl2sfr
mcc: 208
mnc: 10
type: default,supl,mms
proxy:
port:
user:
password:
server:
mmsc: http://mms1
mmsproxy: 10.151.0.1
mmsport: 8080
auth_type:
protocol: IPv4/IPv6
roaming_protocol: IPv4/IPv6
carrier_enabled: true
```

---

### 🎯 Résultat

Tu obtiens :

- Tous les opérateurs français officiels
- Tous les MVNO principaux
- Format YAML propre, standardisé
- Fichiers .md + .yaml prêts à coller dans ton dépôt
- Structure professionnelle

---
