def est_premier(p):
	"""
	est_premier(p)
	Vérifier si p est un nombre premier
	
	Paramètres:
	p (int) : le nombre à vérifier
	
	Return:
	False ou True.
	"""
	# On ne vérifie pas 1 et 2.
	# On va jusqu'au nombre à vérifier
	# en excluant le nombre
	for i in range(2, p):
		# Si la division n'a pas de reste
		# donc il n'est pas premier
		if p % i == 0:
			return False
	return True

# On vérifie avec un nombre non premier et un premier.
print("46 est non premier : ", est_premier(46))
print("23 est premier : ", est_premier(23))
print("33 est premier : ", est_premier(31))