import os
import json

os.system('cls')

dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "liste.json")

try:
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
except:
    liste_de_courses = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Sauvegarder la liste
"""

option = "0"

while option != "5":
    option = input(affichage)
    if option == "1":
        item_a_ajouter = input("Entrez le nom de l'élément à ajouter: ")
        os.system('cls')
        if item_a_ajouter == '':
            print("Vous ne pouvez pas rajouté un élement vide.")
        else:
            print(f"L'élément '{item_a_ajouter}' a été ajouté à la liste.")
            liste_de_courses.append(item_a_ajouter)
    elif option == "2":
        item_a_retirer = input("Entrez le nom de l'élément à enlever: ")
        if item_a_retirer in liste_de_courses:
            os.system('cls')
            print(f"L'élément '{item_a_retirer}' a été retiré de la liste.")
            liste_de_courses.remove(item_a_retirer)
        else:
            os.system('cls')
            print("L'élément que vous voulez enlever n'est pas dans la liste...")
    elif option == "3":
        if liste_de_courses: 
            os.system('cls')
            print("La liste des éléments de votre liste :")
            print("\n".join(liste_de_courses))
        else:
            os.system('cls')
            print("La liste ne contient aucun élément.")    
    elif option == "4":
        liste_de_courses.clear()
        os.system('cls') 
        print("La liste de course est vide.")     

with open(chemin_liste, "w") as f:
    json.dump(liste_de_courses, f)
    os.system('cls') 
    print("Votre liste a été sauvegardé sur votre disque (fichier json).")