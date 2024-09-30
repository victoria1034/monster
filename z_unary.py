def is_relative_integer(nb):
    # Teste si un nombre nb est un entier relatif
    return isinstance(nb, int)

def is_even(nb):
    # Teste si un nombre nb est pair
    return nb % 2 == 0

def last_digit(nb):
    # Renvoie le dernier chiffre d'un nombre nb
    return abs(nb) % 10

def sum_of_digit(nb):
    # Obtenir la valeur absolue pour traiter les nombres négatifs
    nb = abs(nb)
    return sum(int(digit) for digit in str(nb))
