def generate_key(n):
	"""
	generate_key(n)
	Fonction qui génère une clé pour le chiffrement
	On passe un entier qui est en fait la vraie clé.
	Paramètres:
	n (int) : entier, clé de chiffrement
	
	Return
	Dictionnaire : la clé de mappage
	"""
	# Lettres utilisées pour le mappage
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	# Nous allons utiliser un dictionnaire pour faire le mappage
	key = {}
	cnt = 0
	
	# Génère la clé
	for c in letters:
		# Le modulo permet de gérer un nombre qui déborde du nombre de lettre
		# Le modulo permet de redémarrer au début si la valeur de c est
		# plus grande que 25
		key[c] = letters[(cnt + n) % len(letters)]
		cnt += 1
	
	return key

# Vérifions que notre clé est bien générée
key = generate_key(3)
print(key)

def encrypt(key, message):

	"""
	encrypt(key, message)
	Fonction qui chiffre le message.
	
	Paramètres :
	key (dict): clé de mappage.
	message (string): mesage à chiffrer

	Return :
	string : le message chiffré
	"""
	
	# Va contenir le message chiffré
	secret = ""
	for c in message:
		if c in key:
			secret += key[c]
		else:
			secret += c
	
	
	# Vous devez créer une boucle for qui vérifie si le caractère est dans
	# dans la clé de mappage. Si oui, on le substitue. Sinon, on le
	# le remet tel quel.
	#--- code à ajouter ---
	
	return secret

# Vérifions que notre clé est bien générée
key = generate_key(3)
print(key)

# Vérifions que le chiffrement fonctionne
message = "AINSI VA LA VIE"
secret = encrypt(key, message)
print(secret)

message = encrypt(key, secret)
print (message)