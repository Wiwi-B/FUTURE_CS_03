
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY_FILE = "master.key"

# Génère ou charge la clé de 256 bits
def get_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = get_random_bytes(32) # AES-256
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_data(data):
    key = get_or_create_key()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    # On renvoie tout ce qui est nécessaire pour déchiffrer plus tard
    return nonce + tag + ciphertext

def decrypt_data(encrypted_data):
    key = get_or_create_key()
    # On extrait les composants (nonce=16 octets, tag=16 octets)
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data
    except ValueError:
        return None # Erreur : Clé invalide ou fichier corrompu
