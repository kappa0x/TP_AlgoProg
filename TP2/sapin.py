#Question 1.1;
def a_la_chaine(n):
    """Retourne une chaîne de caractères représentant un sapin de hauteur n"""
    sapin = ""
    for i in range(n):
        sapin = "A" * (n)
    return sapin

hello = a_la_chaine(5)
print(hello)
print(len(hello))