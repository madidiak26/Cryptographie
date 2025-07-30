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

