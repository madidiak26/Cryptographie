# SubstitutionCypher1.py

import random

def generate_key():
	"""
	generate_key()
	Fonction qui génère une clé pour le chiffrement
	On ne passe aucun paramètre, car nous allons utiliser
	une fonction aléatoire pour la générer.

	Paramètres:
	aucun
	
	Return
	Dictionnaire : la clé de mappage
	"""
	
	# Lettres utilisées pour le mappage
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	# Une liste de nos lettres pour utiliser avec
	# la partie aléatoire.
	cletters = list(letters)
	
	# La clé est toujours un dictionnaire
	key = {}
	
	# Nous allons faire un mappage, mais plus intelligent.
	# Nous allons utiliser un mappage plus aléatoire.
	# Pour chaque lettre, nous allons utiliser une autre
	# lettre aléatoire de la liste cletters
	
	for c in letters:
		key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
	return key

# Vérifions que notre clé est bien générée
key = generate_key()
print(key)