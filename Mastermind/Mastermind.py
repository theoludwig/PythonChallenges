from random import randint
import os
os.system('cls')

def mastermind(nombreEssaiMaximum  = 12, nombreCouleurADeviner = 5):

    # Initialisation des variables
    couleurDisponible = ["Vert", "Blanc", "Rouge", "Jaune", "Bleu", "Noir", "Rose", "Violet", "Orange", "Gris"]
    couleurEntree = []
    couleurADeviner = [couleurDisponible[randint(0, len(couleurDisponible) - 1)] for i in range(nombreCouleurADeviner)] 

    print("La combinaison à deviner est ", couleurADeviner, "\n") # pour tester uniquement

    # Combinaisons pour essayer de battre l'ordinateur
    for nombreTentative in range(nombreEssaiMaximum):

        # Demande les couleurs (ex: Rouge, Bleu, Vert, Jaune, Noir)
        couleurEntree = input("Entrez les couleurs : ").split(", ")
        couleurEntreeLength = len(couleurEntree)

        # Si la proposition ne dépasse pas nombreCouleurADeviner, on peut continuer :
        if couleurEntreeLength <= nombreCouleurADeviner:

            # Si mauvaise combinaison :
            if couleurEntree != couleurADeviner:

                # Remise à zéro des variables couleurJuste et couleurMauvaisePlace pour le prochain tour de boucle
                couleurMauvaisePlace = []
                couleurJuste = []

                # Boucle de vérification 
                for i in range(0, couleurEntreeLength):
                    if couleurEntree[i] == couleurADeviner[i]:
                        couleurJuste.append([couleurEntree[i], i + 1])
                    elif couleurEntree[i] in couleurADeviner:
                        couleurMauvaisePlace.append([couleurEntree[i], i + 1])

                # Si couleurMauvaisePlace et que couleurJuste est vide alors il n'y a aucune couleur de juste
                if not couleurMauvaisePlace and not couleurJuste:
                    print("Vous n'avez aucune couleur de juste.")
                # Affichage des couleurs mauvaises/justes
                else:
                    print("Couleurs justes et bonne place :", couleurJuste)
                    print("Couleurs justes mais mal placées :", couleurMauvaisePlace)

                # Affichage du nombre d'essai restant
                essaiRestant = nombreEssaiMaximum - (nombreTentative + 1)
                if essaiRestant > 0:
                    print("Il vous reste", essaiRestant ,"essais...\n")
                    continue
                else:
                    print("\nVous avez perdu, la combinaison était :", couleurADeviner)
                    break

            # Si bonne combinaison :
            else:
                print("Bravo, vous avez gagné, les couleurs étaient bien :", couleurEntree)
                break
        else:
            print("Vous ne pouvez pas rentré plus de", nombreCouleurADeviner, "couleurs...\n")

mastermind()