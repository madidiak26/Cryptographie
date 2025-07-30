import random

def generate_dkey(key):
    """
    Génère une clé de déchiffrement en inversant manuellement la clé de chiffrement.
    
    Paramètre :
        key (dict) : Clé de chiffrement.
        
    Retour :
        dict : Clé de déchiffrement.
    """
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey

def generate_key():
    """
    Génère une clé de chiffrement de substitution aléatoire pour les lettres majuscules A-Z.
    
    Retour :
        dict : Clé de mappage (dictionnaire).
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}

    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    
    return key

def encrypt(key, message):
    """
    Chiffre ou déchiffre un message en utilisant une clé de substitution.
    
    Paramètres :
        key (dict) : Clé de mappage (chiffrement ou déchiffrement).
        message (str) : Message à traiter.
    
    Retour :
        str : Message transformé.
    """
    secret = ""
    for c in message:
        if c in key:
            secret += key[c]
        else:
            secret += c
    return secret

# ----- Exemple d'utilisation -----

key = generate_key()
print("Clé de chiffrement :", key)

message = "AINSI VA LA VIE"
secret = encrypt(key, message)
print("Message chiffré :", secret)

dkey = generate_dkey(key)
decrypted = encrypt(dkey, secret)
print("Message déchiffré :", decrypted)
