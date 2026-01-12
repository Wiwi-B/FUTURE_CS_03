# SecureShare-AES

## Système de Partage de Fichiers Sécurisé

SecureShare-AES est une application web développée dans le cadre d’un stage pratique en cybersécurité. Elle permet de stocker et de partager des fichiers de manière confidentielle en garantissant qu’aucune donnée n’est jamais conservée en clair sur le serveur.

Le principe fondamental du projet est le **chiffrement côté serveur avant stockage** : chaque fichier est chiffré avant son écriture sur le disque et n’est déchiffré qu’au moment du téléchargement par l’utilisateur.

---

## Objectifs du projet

* Mettre en œuvre un mécanisme de chiffrement symétrique robuste pour la protection des fichiers.
* Garantir la confidentialité des données au repos.
* Illustrer des concepts clés de la cryptographie appliquée dans une application web.
* Fournir une base pédagogique pour des améliorations futures (authentification, gestion des clés, intégrité).

---

## Stack technique

### Backend

* Python 3.x
* Flask (framework web)

### Cryptographie

* PyCryptodome
* AES-128 (Advanced Encryption Standard)
* Mode CBC (Cipher Block Chaining)

### Frontend

* HTML5 / CSS3
* Design inspiré d’un style « Retro Terminal » (Matrix-like)

---

## Architecture de sécurité

### 1. Processus de chiffrement

* **Algorithme** : AES-128 en mode CBC.
* **Padding** : PKCS#7 afin d’aligner les données sur des blocs de 16 octets.
* **Vecteur d’initialisation (IV)** :

  * Généré aléatoirement pour chaque opération de chiffrement.
  * Garantit que deux fichiers identiques ne produisent jamais le même texte chiffré.
* **Stockage de l’IV** :

  * L’IV est concaténé au début du fichier chiffré afin d’être récupéré lors du déchiffrement.

### 2. Confidentialité au repos

Même en cas d’accès non autorisé au serveur ou au dossier de stockage (`fichiers_finaux/`), les fichiers restent illisibles. Les données sont stockées sous forme binaire chiffrée, avec l’extension `.locked`.

Aucun fichier n’est conservé en clair sur le disque.

---

## Structure du projet

```
secure-share/
│
├── app.py              # Logique principale du serveur Flask
├── fichiers_finaux/    # Dossier de stockage des fichiers chiffrés (exclu du dépôt)
├── templates/
│   └── index.html      # Interface utilisateur
├── .gitignore          # Exclusion des fichiers sensibles
├── README.md           # Documentation du projet
```

---

## Installation

### Prérequis

* Python 3.x installé
* pip (gestionnaire de paquets Python)

### Étapes

1. Cloner le dépôt :

```bash
git clone https://github.com/TON_PSEUDO/secure-share.git
cd secure-share
```

2. Installer les dépendances :

```bash
pip install flask pycryptodome
```

3. Lancer le serveur :

```bash
python app.py
```

4. Accéder à l’application via un navigateur :

```
http://127.0.0.1:5000
```

---

## Utilisation

* L’utilisateur sélectionne un fichier via l’interface web.
* Le fichier est chiffré côté serveur avant d’être enregistré sur le disque.
* Lors du téléchargement, le fichier est déchiffré dynamiquement puis transmis à l’utilisateur.

---

## Limitations connues

* La clé de chiffrement est actuellement codée en dur dans l’application.
* Absence de système d’authentification et de gestion des utilisateurs.
* Pas de mécanisme de vérification d’intégrité des fichiers.
* Le mode CBC ne fournit pas d’authentification des données.

---

## Pistes d’amélioration

* Gestion sécurisée des clés via un coffre-fort (ex. HashiCorp Vault).
* Authentification des utilisateurs avec des clés de chiffrement distinctes.
* Passage à AES-GCM pour assurer à la fois confidentialité et intégrité.
* Ajout d’un HMAC pour la vérification d’intégrité des fichiers.
* Journalisation et audit des accès.

---

## Avertissement de sécurité

Ce projet est à vocation pédagogique. Il ne doit pas être utilisé tel quel en production sans une revue de sécurité approfondie et la mise en place des améliorations mentionnées.

---

## Auteur

BARIKI Wilson
Stagiaire en cybersécurité
Projet réalisé en janvier 2026
