def xor(x, s):
    """
    xor(x, s)
    Fonction qui affiche un XOR entre deux nombres
    Parametres
    x (int): premier nombre
    s (int): deuxieme nombre

    return
    aucun
    """

    print(bin(x), "xor", bin(s), "=", bin(x^s))
xor(4, 8)
xor(4, 4)
xor(255, 1)
xor(255, 128)