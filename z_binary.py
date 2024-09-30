def is_multiple_of(nb, p):
    
    #is_multiple_of(nb, p) qui teste si un nombre nb est multiple d’un autre nombre p
  
    if p == 0:
        raise ValueError("The divisor 'p' cannot be zero.")
    return nb % p == 0

def sum_int(a, b):
    
    # sum(a, b) qui renvoi la somme des nombres a et b

    # return a + b
    return sum([a, b])

def diff(a, b):
    
    # diff(a, b) qui retourne la différence entre les nombres a et b

    return a - b
