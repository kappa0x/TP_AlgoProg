#Question 1.1;
def a_la_chaine(n):
    """Retourne une chaîne de caractères composé d'une juxtaposition de n caractères A"""
    sapin = ""
    for i in range(n):
        sapin = "A" * (n)
    return sapin

hello = a_la_chaine(5)
print(hello)
print(len(hello))

#Question 1.2;
def a_la_chaine2(esp,n):
    """Retourne une chaîne de caractères composé d'espaces suivis de n caractères A"""