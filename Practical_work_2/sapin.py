#Question 1.1;
def a_la_chaine(n):
    """Retourne une chaîne de caractères composé d'une juxtaposition de n caractères A"""
    sapin = ""
    for i in range(n):
        sapin = "A" * (n)
    return sapin
#print(a_la_chaine(13))

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

#Question 1.4;
def diagonale1(n):
    """"Retourne n lignes, la première ligne devra contenir 1 caractère A et la deuxième ligne devra contenir 2 caractères A, et ainsi de suite jusqu'à n lignes"""
    sapin = ""
    for i in range(n):
        sapin = "A" * (i+1)
        print(sapin)
    return sapin
##print(diagonale1(5))

#Question 1.5;
def diagonale2(n):
    """Retourne n lignes, sur la première ligne il doit y avoir des espaces et un caractère 'A' en dernière position, sur la deuxième ligne il doit y avoir des espaces et deux caractères 'A' en dernière position"""
    sapin = ""
    for i in range(n):
        sapin = " " * (n-i) + "A" * (i+1)
        print(sapin)
    return sapin
#print(diagonale2(5))

#Question 1.6;
def sapin(n):
    """"Retourne n lignes, la première ligne doit contenir un caractère 'A', La deuxième devra en contenir 3 et ainsi de suite jusqu'à ce qu n lignes soit écritent.
        Le programme retourne trois caractères 'A' qui feront office de tronc pour le sapin"""
    hello = ""
    for i in range(n):
        hello = " " * (n-i) + "A" * (i*2+1)
        print(hello)
    return hello
#print(sapin(5))