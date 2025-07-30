# DoubleDES01.py
from pyDes import *
import random

# Notre message à envoyer
message = b"01234567"

# On génère une clé de 1 octet (petite clé)
key_11 = random.randrange(0, 256)

# On inclut la petite clé dans 8 octets.
# C'est ce qui est demandé par l'implémentation
# de DES que l'on utilise.
# On fait du padding avec les autres octets.
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])

# On se crée une 2e clé de la même façon.
key_21 = random.randrange(0, 256)
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])

# Notre vecteur d'initialisation pour CBC.
iv = bytes([0] * 8)

# Nos objets clés DES
k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

# Alice envoie un message à Bob
# On chiffre le message 2 fois avec 2 clés différentes.
# Pour une meilleure sécurité. ;)
secret = k2.encrypt(k1.encrypt(message))
print("La clé 11 : ", key_11)
print("La clé 21 : ", key_21)
print("Le message chiffré d'Alice : ", secret)

# Bob reçoit le message d'Alice
message = k1.decrypt(k2.decrypt(secret))
print("Le message que Bob reçoit : ", message)

# Eve s'attaque au Double DES
# Nous allons utiliser une table de recherche
lookup = {}

# Notre première boucle pour trouver la première clé.
# Nous avons une clé de 8 bits, donc 256 possibilités.
# Nous allons remplir une table de recherche
# avec toutes les possibilités de la première clé.
for i in range(256):
	# On se crée une clé
	k = bytes([i, 0, 0, 0, 0, 0, 0, 0])

	# On se crée un objet clé DES
	k = des(k, ECB, iv, pad=None, padmode=PAD_PKCS5)
	
	# On met le texte chiffré du texte connu
	# dans la table de recherche
	lookup[k.encrypt(message)] = i

# Notre deuxième boucle va trouver la deuxième clé.
# On déchiffre une fois avec toutes les possibilités
# de clé. À chaque itération, on vérifie le texte
# déchiffré avec les entrées de notre table de
# recherche. Si on a une équivalence, on a
# trouvé les 2 clés
for i in range(256):
	# On se crée une clé
	k = bytes([i, 0, 0, 0, 0, 0, 0, 0])

	# On se crée un objet clé DES
	k = des(k, ECB, iv, pad=None, padmode=PAD_PKCS5)
	
	# On vérifie si le texte déchiffré
	# une fois est dans notre table
	# de recherche. Si oui, Bingo!
	if k.decrypt(secret) in lookup:
		# On affiche la clé 1
		print("Clé k_11 : ", lookup[k.decrypt(secret)])
		# On affiche la clé 2
		print("Clé k_21 : ", i)
		# On n’a plus rien à faire.
		break