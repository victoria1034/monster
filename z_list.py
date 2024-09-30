import z_unary
import z_binary
# Le module z_list.py qui implémente les opérations sur les listes de nombre

# b. sum(l) qui évalue la somme des valeurs de la liste l passée en paramètre
# au moyen de la fonction sum(a, b) du module z_binary
def is_relative_integer(list):
    # qui teste si tous les nombres d'une liste sont des entiers relatifs avec is_relative_integer du module z_unary
    results = []
    for x in list:
        results.append(z_unary.is_relative_integer(x))
    return results


def sum_list(nums):
    # Le nom de la fonction a ete changer pour pouvoir utiliser la built-in sum dans le future
    # prens une liste de nombres comme arugment
    results = nums[0]
    nums.pop(0)
    for x in nums:
        results = z_binary.sum_int([results, x])
    # z_binary.sum_int n'est pas nécessaire pour accomplir le but, la ligne suivante marcherais parfaitement
    # proving_a_point = sum(list)

    return results

