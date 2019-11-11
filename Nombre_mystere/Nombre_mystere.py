import random
import os
os.system('cls')

nombre_mystere = random.randint(1, 50)

for i in range(5): 
    nombre = input("Quel est le nombre mystère ? ")
    if not nombre.isdigit(): 
        print("Veuillez entré un nombre valide...")
        continue

    nombre = int(nombre)

    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        os.system('cls')
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()

print(f"Vous avez perdu. Le nombre mystère était {nombre_mystere}.")