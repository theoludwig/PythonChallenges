def dessinerPyramide(hauteur):
    nombresDeX = 1
    for iteration in range(hauteur):
        print(" " * (hauteur - iteration), "x" * nombresDeX)
        nombresDeX += 2
        
try:
    hauteur = int(input("Hauteur de la pyramide : "))
    dessinerPyramide(hauteur)
except:
    print("Oups, il y a une erreur. \n")