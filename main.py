import z_unary
import z_binary
import z_ternary
import z_list


def get_user_number(text="Entre un numero: ", num_type=float):
    while True:
        try:
            num = num_type(input(text))
            return num
        except:
            print("Erreur, rentre un numero")


if __name__ == "__main__":
    # a. Détermine la parité d’un nombre saisit par l’utilisateur.
    print("A. Parité")
    if z_unary.is_even(get_user_number()):
        print("Est un nombre pair")
    else:
        print("N'est pas un nombre")
    # b. Teste si un nombre saisit par l’utilisateur est multiple de 9 lorsque la somme de ses chiffres est 9.
    print("B. Multiple de 9 et somme de 9")
    num = get_user_number(num_type=int)
    if z_unary.sum_of_digit(num) == 9 and z_binary.is_multiple_of(num, 9):
            print("Rempli les conditions")
    else:
            print("Rempli pas les conditions")
    # c. Teste si un nombre saisit par l’utilisateur est multiple de 5 lorsqu'il se termine par 0 ou 5
    print("C. Multiple de 5")
    if z_unary.last_digit(get_user_number()) in (5, 0):
        print("C'est un multiple de 5")
    else:
        print("C'est pas un multiple de 5")

    # d. Evalue si le triplet de valeurs saisit par l’utilisateur forme un triplet de Pythagore
    print("D. triplet de Pytagore")
    if z_ternary.pythagore(get_user_number(), get_user_number(), get_user_number()):
        print("C'est un triangle carre")
    else:
        print("C'est pas un triangle carre")

