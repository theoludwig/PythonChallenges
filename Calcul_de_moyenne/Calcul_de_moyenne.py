try:
    # Demande à l'utilisateur une liste de notes (exemple: 12, 16, 18, 6, 10) 
    nombres = input("Veuillez rentrer une liste de notes (séparées par virgules) : ").split(", ")

    # Convertis chaque élément de la liste créé avec split() en float
    nombresListe = [float(x) for x in nombres]

    # Calcul et affichage du résultat de la moyenne des notes
    resultat = 0
    for element in nombresListe:
        resultat = resultat + element
    resultat = resultat / len(nombresListe)
    print("Moyenne de notes :", resultat)
except:
    print("Oups, il y a une erreur. \n")