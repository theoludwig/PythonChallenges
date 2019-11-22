# Seulement les diviseurs non nul et positif
def listeDiviseur(nombre):
    liste = []
    # Boucle allant de 1 jusqu'au nombre inclu (range exclu ce nombre donc on fait + 1)
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            liste.append(i)
    return liste

def estPremier(nombre):
    return len(listeDiviseur(nombre)) == 2

try:
    nombre = int(input("Veuillez rentré un nombre : "))
    if estPremier(nombre):
        print(nombre, "est un nombre premier.")
    else:
        print(nombre, "n'est pas un nombre premier.")
except:
    print("Oups, il y a une erreur. \n")