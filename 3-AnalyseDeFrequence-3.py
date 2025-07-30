# AnalyseDeFrequence2.py

secret = """LRVMNIR BPR SUMVBWVR JX BPR LMIWV YJERYRKBI JX QMBM WI
BPR XJVNI MKD YMIBRUT JX IRHX WI BPR RIIRKVR JX
YMBINLMTMIPW UTN QMUMBR DJ W IPMHH BUT BJ RHNVWDMBR BPR
YJERYRKBI JX BPR QMBM MVVJUDWKO BJ YT WKBRUSURBMBWJK
LMIRD JK XJUBT TRMUI JX IBNDT
WB WI KJB MK RMIT BMIQ BJ RASHMWK RMVP YJERYRKB MKD WBI
IWOKWXWVMKVR MKD IJYR YNIB URYMWK NKRASHMWKRD BJ OWER M
VJYSHRBR RASHMKMBWJK JKR CJNHD PMER BJ LR FNMHWXWRD MKD
WKISWURD BJ INVP MK RABRKB BPMB PR VJNHD URMVP BPR IBMBR
JX RKHWOPBRKRD YWKD VMSMLHR JX URVJOKWGWKO IJNKDHRII
IJNKD MKD IPMSRHRII IPMSR W DJ KJB DRRY YTIRHX BPR XWKMH
MNBPJUWBT LNB YT RASRUWRKVR CWBP QMBM PMI HRXB KJ DJNLB
BPMB BPR XJHHJCWKO WI BPR SUJSRU MSSHWVMBWJK MKD
WKBRUSURBMBWJK W JXXRU YT BPRJUWRI WK BPR PJSR BPMB BPR
RIIRKVR JX JQWKMCMK QMUMBR CWHH URYMWK WKBMVB
"""

class Attaque:
	"""
	Classe Attaque
	Classe pour analyse cryptographique (attaque) d'un
	texte chiffré par chiffrement de substitution
	"""
	def __init__(self):
		# On doit initialiser notre alphabet et
		# la fréquence
		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		
		# On utilise un dictionnaire pour enregistrer
		# la fréquence de nos lettres
		self.freq = {}
	
	def calculate_freq(self, secret):
		"""
		calculate_freq(self, secret)
		Méthode qui calcule la fréquence d'un
		caractère dans le texte
		
		Paramètres:
		self : notre objet d'Attaque
		secret (string) : le message secret
		
		Return
		Dictionnaire : la clé de mappage
		"""
		
		# On va utiliser un compteur pour compter les lettres
		# de notre alphabet dans le texte.
		# On va mettre le compteur à 0 pour chacune des lettres
		for c in self.alphabet:
			self.freq[c] = 0
		
		# On doit également connaître le nombre
		# de caractères dans le texte
		letter_count = 0
		
		# Nous allons compter la fréquence de chacun
		# des caractères dans le texte et le
		# nombre de caractères dans le texte
		for c in secret:
			if c in self.freq:
				self.freq[c] += 1
				letter_count += 1
		
		# On doit maintenant connaître le pourcentage
		# d'utilisation de chacun des caractères
		for c in self.freq:
			self.freq[c] = round(self.freq[c]/letter_count, 4)
		
	def print_freq(self):
		"""
		print_freq(self)
		Méthode qui imprime le résultat
		sur 3 colonnes
		
		Paramètres:
		self : notre objet d'Attaque
		
		Return
		Aucun
		"""
		
		# On imprime le résultat sur 3 colonnes
		new_line_count = 0
		for c in self.freq:
			print(c, ":", self.freq[c], " ", end='')
			if new_line_count % 3 == 2:
				print()
			new_line_count += 1

# Créer un objet d'attaque
pirate = Attaque()
# Calcul la fréquence de caractères
pirate.calculate_freq(secret)
pirate.print_freq()

class Attaque:
	"""
	Classe Attaque
	Classe pour analyse cryptographique (attaque) d'un
	texte chiffré par chiffrement de substitution
	"""
	
	def __init__(self):
		# On doit initialiser notre alphabet et
		# la fréquence
		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

		# On utilise un dictionnaire pour enregistrer
		# la fréquence de nos lettres
		self.freq = {}
		
		# On utilise un dictionnaire pour la
		# correspondance de nos caractères
		self.mappings = {}
		
		# Notre référence de correspondance des
		# caractères
		self.freq_eng = {'A':0.08167, 'B':0.01492, 'C':0.02782, 'D':0.04253, 'E':0.12702, 'F':0.02228, 'G':0.02015, 'H':0.06094, 'I':0.06966, 'J':0.00153, 'K':0.00772, 'L':0.04025, 'M':0.02406, 'N':0.06749, 'O':0.07507, 'P':0.01929, 'Q':0.00095, 'R':0.05987, 'S':0.06327, 'T':0.09056, 'U':0.02758, 'V':0.00978, 'W':0.02360, 'X':0.00150, 'Y':0.01974, 'Z':0.00074}