from random import randint

# Génération d'un nombre mystère aléatoirement entre 1 inclus et 50 inclus 
nombre_mystere = randint(1, 50)

# Le joueur a 5 essais pour deviner le nombre 
for i in range(5): 
    nombre = input("Quel est le nombre mystère ? ")

    # Valeur tapée par l'utilisateur n'est pas un nombre
    if not nombre.isdigit(): 
        print("Veuillez entré un nombre valide...")
        continue

    nombre = int(nombre)

    # Vérifications si le nombre est plus petit/grand au nombre mystère
    if nombre > nombre_mystere:
        print("Le nombre mystère est plus petit que", nombre)
    elif nombre < nombre_mystere:
        print("Le nombre mystère est plus grand que", nombre)
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()

print("Vous avez perdu. Le nombre mystère était", nombre_mystere)