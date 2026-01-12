# SecureShare-AES : Système de Partage de Fichiers Sécurisé

## Présentation du Projet
Ce projet a été réalisé dans le cadre d'un stage pratique en cybersécurité. Il s'agit d'une application web permettant de stocker et de partager des fichiers de manière confidentielle.

**Le concept :** Aucun fichier n'est stocké en clair sur le serveur. Chaque document est chiffré avant l'écriture sur le disque et n'est déchiffré qu'au moment du téléchargement par l'utilisateur.

## Stack Technique
- **Backend :** Python 3.x avec le framework **Flask**.
- **Cryptographie :** Bibliothèque **PyCryptodome**.
- **Algorithme :** AES-128 (Advanced Encryption Standard) en mode **CBC** (Cipher Block Chaining).
- **Frontend :** HTML5/CSS3 avec un design "Retro Terminal" (Matrix style).

## Architecture de Sécurité

### 1. Processus de Chiffrement
- **Padding :** Utilisation du standard **PKCS7** pour aligner les données sur des blocs de 16 octets.
- **Vecteur d'Initialisation (IV) :** Un IV unique est généré aléatoirement pour chaque opération de chiffrement afin d'éviter que deux fichiers identiques n'aient le même contenu chiffré.
- **Stockage :** L'IV est concaténé au début du fichier chiffré pour être récupéré lors du déchiffrement.

### 2. Confidentialité au Repos
Même si un attaquant accède physiquement au serveur ou au dossier `fichiers_finaux/`, il ne pourra pas lire les données car elles apparaissent sous forme de données binaires aléatoires avec l'extension `.locked`.

## Installation et Lancement

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/TON_PSEUDO/secure-share.git
   cd secure-share
Installer les dépendances :
code
Bash
pip install flask pycryptodome
Lancer le serveur :
code
Bash
python app.py
Accès : Ouvrez votre navigateur sur http://127.0.0.1:5000
Structure du Projet
code
Text
.
├── app.py              # Logique du serveur et fonctions de cryptographie
├── fichiers_finaux/    # Dossier de stockage des fichiers chiffrés (exclu du commit)
├── templates/
│   └── index.html      # Interface utilisateur (Vert/Noir)
├── .gitignore          # Exclusion des fichiers sensibles
└── README.md           # Documentation du projet
Limitations & Améliorations Futures (Roadmap)
Gestion des clés : Actuellement, la clé est codée en dur. Une amélioration majeure serait d'utiliser un coffre-fort de clés (Key Vault).
Authentification : Ajouter un système de login pour que chaque utilisateur possède sa propre clé de chiffrement.
Intégrité : Passer du mode CBC au mode GCM pour ajouter une vérification d'intégrité (HMAC).
Auteur
BARIKI Wilson - Stagiaire en Cybersécurité
Projet réalisé en janvier 2024
