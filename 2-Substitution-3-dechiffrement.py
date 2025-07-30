import random

def generate_key():
    """
    Fonction qui génère une clé de chiffrement aléatoire (substitution monoalphabétique).
    
    Retour :
        dict : Clé de mappage aléatoire entre lettres majuscules.
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}

    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    
    return key

def encrypt(key, message):
    """
    Chiffre un message à l’aide d’une clé de substitution.
    
    Paramètres :
        key (dict) : Clé de mappage pour le chiffrement.
        message (str) : Message en lettres majuscules à chiffrer.
        
    Retour :
        str : Message chiffré.
    """
    secret = ""
    for c in message:
        if c in key:
            secret += key[c]
        else:
            secret += c  # Laisser les espaces ou ponctuations inchangés
    return secret

def generate_dkey(key):
    """
    Génère une clé de déchiffrement à partir de la clé de chiffrement.
    
    Paramètre :
        key (dict) : Clé de chiffrement.
        
    Retour :
        dict : Clé de déchiffrement (inversée).
    """
    return {v: k for k, v in key.items()}

# Exemple d’utilisation :
key = generate_key()
print("Clé de chiffrement :", key)

message = "AINSI VA LA VIE"
secret = encrypt(key, message)
print("Message chiffré :", secret)

dkey = generate_dkey(key)
decrypted = encrypt(dkey, secret)
print("Message déchiffré :", decrypted)
