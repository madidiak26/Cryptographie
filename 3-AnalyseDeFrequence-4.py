# AnalyseDeFrequenceFinal.py
import operator
import sys

# Texte chiffré
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
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.freq = {}
        self.mappings = {}
        self.key = {}  # clé actuelle
        self.plain_chars_left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.secret_chars_left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.freq_eng = {
            'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
            'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
            'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
            'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
            'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074
        }

    def calculate_freq(self, secret):
        for c in self.alphabet:
            self.freq[c] = 0
        letter_count = 0
        for c in secret:
            if c in self.freq:
                self.freq[c] += 1
                letter_count += 1
        for c in self.freq:
            self.freq[c] = round(self.freq[c] / letter_count, 4)

    def print_freq(self):
        count = 0
        for c in self.freq:
            print(f"{c} : {self.freq[c]}", end='   ')
            count += 1
            if count % 3 == 0:
                print()
        if count % 3 != 0:
            print()

    def calculate_matches(self):
        for secret_char in self.alphabet:
            map_scores = {}
            for plain_char in self.alphabet:
                map_scores[plain_char] = round(abs(self.freq.get(secret_char, 0) - self.freq_eng[plain_char]), 4)
            self.mappings[secret_char] = sorted(map_scores.items(), key=operator.itemgetter(1))

    def guess_key(self):
        for secret_char in self.mappings:
            for plain_char, score in self.mappings[secret_char]:
                if plain_char in self.plain_chars_left and secret_char in self.secret_chars_left:
                    self.set_key_mapping(secret_char, plain_char)
                    break

    def get_key(self):
        return self.key

    def set_key_mapping(self, secret_char, plain_char):
        if secret_char not in self.secret_chars_left or plain_char not in self.plain_chars_left:
            print("Erreur de mappage de clés : ", secret_char, plain_char)
            sys.exit(-1)
        self.key[secret_char] = plain_char
        self.secret_chars_left = self.secret_chars_left.replace(secret_char, '')
        self.plain_chars_left = self.plain_chars_left.replace(plain_char, '')

# Fonction de déchiffrement
def decrypt(key, secret):
    message = ""
    for c in secret:
        if c in key:
            message += key[c]
        else:
            message += c
    return message

# --- EXÉCUTION DU SCRIPT ---
pirate = Attaque()
pirate.calculate_freq(secret)
pirate.print_freq()
pirate.calculate_matches()

# Ajout de caractères devinés
pirate.set_key_mapping('R', 'E')
pirate.set_key_mapping('B', 'T')
pirate.set_key_mapping('M', 'A')
pirate.set_key_mapping('V', 'C')
pirate.set_key_mapping('P', 'H')
pirate.set_key_mapping('W', 'I')
pirate.set_key_mapping('S', 'P')
pirate.set_key_mapping('U', 'R')

# Essai de clé
pirate.guess_key()
key = pirate.get_key()

print("\n=== Clé actuelle ===")
print(key)

# Déchiffre le message
message = decrypt(key, secret)

# Affiche message déchiffré + texte chiffré
message_lines = message.splitlines()
secret_lines = secret.splitlines()
print("\n=== Texte déchiffré vs Texte chiffré ===")
for i in range(len(message_lines)):
    print("P:", message_lines[i])
    print("C:", secret_lines[i])
