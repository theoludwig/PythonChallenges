def fibonacci(compteur):
    a, b = 0, 1 
    resultat = [] 
    for _ in range(compteur):
        resultat.append(a)
        a, b = b, a+b
    return resultat

try:
    compteur = int(input("Entrez le compteur de nombre : "))
    print(fibonacci(compteur))
except:
    print("Oups, il y a une erreur. \n")

"""
Démonstration en 6 tours de boucle : combient vaut a et b à chaque itération (après l'ajout de a au résultat).
a = 0 - b = 1
a = 1 - b = 0+1
a = 1 - b = 1+1
a = 2 - b = 1+2
a = 3 - b = 2+3
a = 5 - b = 3+5
"""