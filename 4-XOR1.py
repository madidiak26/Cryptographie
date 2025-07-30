import random

def generate_key_stream(n):
	"""
	generate_key_stream(n)
	Génère une clé aléatoire pour le chiffrement
	
	Paramètres:
	n (int) : la longueur de la clé
	
	Return:
	Une clé aléatoire d'octets (valeur binaire)
	"""
	
	return bytes([random.randrange(0, 256) for i in range(n)])

def xor_bytes(key_stream, texte):
	"""
	xor_bytes(key_stream, texte)
	Fait un XOR d'une clé aléatoire avec un texte
	
	Paramètres:
	key_stream (int) : clé aléatoire
	texte () : texte à faire un XOR
	
	Return:
	Texte chiffré ou déchiffré
	"""
	
	# Prends la longueur minimale entre les deux paramètres
	# La clé et le texte doivent être de la même longueur,
	# sinon on utilise le plus court des deux.
	length = min(len(key_stream), len(texte))
	# Le texte est traité octet par octet et retourne en octets
	return bytes([key_stream[i] ^ texte[i] for i in range(length)])

#message en texte clair
message = "AINSI VA LA VIE"
#Le message doit etre en binaire. LE XOR est en binaire
message = message.encode()
#print(len(message))
#Generer une cle aleatoire. La cle doit etre la longueur du message (description du One Time PAD)
key_stream = generate_key_stream(len(message))
print("La cle : ", key_stream)
#generer le texte chiffre
secret = xor_bytes(key_stream, message)
print("Le text chiffre :", secret)

#retrouver le texte original, On refaire un XOR
plain_text = xor_bytes(key_stream, secret)
print("Le texte original :", plain_text)