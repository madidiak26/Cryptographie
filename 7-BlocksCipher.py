# DES01.py

# Import l'implémentation de DES
# https://gist.github.com/eigenein/1275094
from pyDes import *

# Notre message un peu spécial
message = b"0123456701234567"

# On utilise la même clé que dans les commentaires
# La clé doit avoir 8 octets, dont les 8 caractères
key = b"DESCRYPT"

# Un vecteur d’initialisation, encore comme
# dans les commentaires, on utilise 8 zéros.
# Ce vecteur n'est pas utilisé dans le
# mode ECB, notre premier mode utilisé.
iv = bytes([0]*8)

# On crée notre objet clé, on ne met pas de
# caractère de padding et on utilise
# le mode de padding recommandé
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

# On chiffre le message
secret = k.encrypt(message)

# On va comparer la longueur du message original
# avec celui chiffré.
print("Longueur du texte plain : ", len(message))
print("Longueur du texte chiffré : ", len(secret))

# On imprime les 3 blocs de messages
print("Premier bloc chiffré : ", secret[0:8])
print("Deuxième bloc chiffré : ", secret[8:16])
print("Le reste chiffré : ", secret[16:])

# On déchiffre ici
message = k.decrypt(secret)
print("Notre message déchiffré : ", message)