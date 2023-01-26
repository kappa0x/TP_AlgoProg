#Question 1.1;
def a_la_chaine(n):
    """Retourne une chaîne de caractères composé d'une juxtaposition de n caractères A"""
    sapin = ""
    for i in range(n):
        sapin = "A" * (n)
    return sapin

#Question 1.2;
def a_la_chaine2(esp,n):
    """Retourne une chaîne de caractères composé d'espaces suivis de n caractères A"""
    sapin = ""
    for i in range(n):
        sapin = " " * (esp) + "A" * (n)
    return sapin

#Question 1.3;
def colonne(n):
    """Retourne None et Affiche 10 fois une chaîne de caractères composé de n fois  A"""
    sapin = ""
    i = 0
    for i in range(10):
        sapin = "A" * (n)
        print(sapin)
    return None