# DES01.py

# Import l'implémentation de DES
# https://gist.github.com/eigenein/1275094
from pyDes import *

def modification(secret):
		
	# On créer une liste de zéro de la même
	# longueur que le secret
	mod = [0] * len(secret)
	#On modifie les caractere selon notre besoin
	#On modifie les caractere selon notre besoin
	mod[11] = ord(' ') ^ ord('1')
	mod[12] = ord(' ') ^ ord('0')
	mod[13] = ord('1') ^ ord('0')
	#comme on a deja des 0
	#le 1 va mettre seulement
	#un bit a 1
	mod[8] = 1
	
   
	# On fait la même opération que pour chiffrer
	return bytes([mod[i] ^ secret[i] for i in range(len(secret))])

# Notre message un peu spécial
message = b"Vers Bob:    10$ et lui souhaiter bonne chance"

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

# Alice envoie son message à la banque
secret = k.encrypt(message)
print("Longueur du texte plain : ", len(message))
print("Longueur du texte chiffré : ", len(secret))
print("Message chiffré d'Alice : ", secret)

# Bob se place entre Alice et la banque
secret = modification(secret)
print("Message chiffre de Bob : ", secret)

# La banque déchiffre ici
message = k.decrypt(secret)
print("Notre message déchiffré : ", message)