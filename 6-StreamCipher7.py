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

def get_key(message, secret):
	"""
	get_key(message, secret)
	Génère un flux de clés à partir d'un message en texte clair
	et d'un message chiffré
	
	Paramètres :
	message (bytes) : message en clair
	secret (bytes) : message chiffré
	
	Return :
	(bytes) : flux de clés
	"""
	
	# Fait un XOR octet par octet
	return bytes([message[i] ^ secret[i] for i in range(len(secret))])


def crack(key_stream, secret):
	"""
	crack(key_stream, secret)
	Fonction qui utilise un flux de clés pour déchiffrer
	le message chiffré.
	
	Paramètres :
	key_stream (bytes) : le flux de clés
	secret (bytes) : le message chiffré
	
	Return :
	
	"""
	
	# On ne peut déchiffrer plus que la longueur
	# du flux de clés ou de la longueur du
	# message. On recherche le plus petit
	length = min(len(key_stream), len(secret))
	
	# On refait toujours la même chose :)
	return bytes([key_stream[i] ^ secret[i] for i in range(length)])



# Eve donne un message à Alice
message_Eve = "Ceci est un message super hyper important".encode()

# Alice communique avec Bob
cle_secret = 33
print("La cle secrete entre Alice et Bob : ", cle_secret)
key = KeyStream(cle_secret)
message = "MESSAGE : " + "Un message secret vers Bob"
message = message.encode()
print("Alice : ", message)
secret = encryptDecrypt(key, message)
print("Le secret : ", secret)

# Voilà Bob
key = KeyStream(cle_secret)
message = encryptDecrypt(key, secret)
print("Bob : ", message)

