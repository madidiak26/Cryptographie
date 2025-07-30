import random
class KeyStream:
	"""
	Classe KeyStream
	Classe pour générer un flux de clés
	"""
	def __init__(self, key=1):
		"""
		init (self, key=1)
		Initialise l'objet clé
		
		Paramètres:
		self : notre objet flux de clé
		key (int) : la clé partagée,
		elle est à 1 par défaut
		
		Return
		Notre objet KeyStream
		"""
		
		# Initialise l'objet à la clé
		self.next = key
	
	def rand(self):
		"""
		rand(self)
		Calcul la valeur aléatoire
		
		Paramètres:
		self : notre objet flux de clés

		Return:
		self.next (int) : la prochaine valeur aléatoire
		"""
		
		# L'équation pour notre LCG
		# Xnext+1 = (a*Xnext + c) mod m
		self.next = (1103515245 * self.next + 12345) % 2**31
		return self.next
		
	def get_key_byte(self):
		"""
		get_key_byte(self)
		Crée le flux de clé
		
		Paramètres:
		self : notre objet flux de clé
		
		Return:
		Retourne une clé aléatoire d’un caractère (le mod 256)
		"""
		
		return self.rand() % 256

def encryptDecrypt(key, message):
	"""
	encryptDecrypt(key, message)
	Chiffre le message
	
	Paramètres
	key (objet KeyStream): flux de clés
	message (bytes): message à chiffrer
	
	Return:
	(bytes) : message chiffré
	"""
	
	# On fait un XOR avec chacun des caractères du message
	# Une nouvelle clé est générée à chaque caractère
	return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def transmit(secret, tauxErreurs):
	"""
	transmit(secret, tauxErreurs)
	Fonction qui simule des erreurs de transmission.
	On passe le message octet par octet et de
	temps en temps on flip un bit selon le tauxErreur passé.
	
	Paramètres :
	secret (bytes) : le message qui est transmis
	tauxErreurs () : le niveau d'erreur qu'on veut insérer dans le message
	
	Return :
	(bytes) : le message avec des erreurs
	"""
	
	# Contiens le message modifié
	b = []
	
	# On passe chaque octet du message et
	# l'ajoute à b
	for c in secret:
		# Selon notre taux d'erreur, on
		# flip un bit dans l'octet
		if random.randrange(0, tauxErreurs) == 0:
			#
			c = c ^ 2**random.randrange(0, 8)
		b.append(c)
	return bytes(b)


# On chiffre le message
# Notre objet clé de flux
key = KeyStream(23)

# Notre message à chiffrer
# Il doit être binaire
message = "Nous allons attaquer a 12 h, par le cote Est de la prairie".encode()
secret = encryptDecrypt(key, message)
###### Partie de codes à ajouter #####
# On veut voir le message original
print("Notre message est : ", message)
# On génère les erreurs tous les 6 octets
secret = transmit(secret, 6)
#######################################
# On déchiffre le message
# On doit initialiser notre objet clé de flux de nouveau
# Notre clé seed
key = KeyStream(23)

# On déchiffre comme on chiffre avec un XOR
message = encryptDecrypt(key, secret)
print("Notre message en texte : ", message)