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

def modification(secret):
	"""
	modification(secret)
	Fonction qui modifie certains octets du message,
	sans la clé
	Nous allons flipper des bits, mais pas
	n'importe quels bits, ceux en notre faveur
	
	Paramètres :
	secret (bytes) : le message secret

	Return :
	(bytes) : le message secret modifié
	"""
	
	# On créer une liste de zéro de la même
	# longueur que le secret
	mod = [0] * len(secret)
	#On modifie les caractere selon notre besoin
	mod[18] = ord(' ') ^ ord('1')
	mod[19] = ord(' ') ^ ord('0')
	mod[20] = ord('1') ^ ord('0')
	
	# On fait la même opération que pour chiffrer
	return bytes([mod[i] ^ secret[i] for i in range(len(secret))])

# Alice envoie son message à la banque
# Les deux se sont accordé pour la clé 10
key = KeyStream(10)

# Notre message à chiffrer
message = "Transfert a Bob :   10$".encode()
print("Alice : ", message)
secret = encryptDecrypt(key, message)
print("Le secret : ", secret)

# Bob intercepte le message ici
secret=modification(secret)

# La banque reçoit le message
# La banque connait la clé d'Alice
key = KeyStream(10)
message = encryptDecrypt(key, secret)
print("La banque : ", message)
