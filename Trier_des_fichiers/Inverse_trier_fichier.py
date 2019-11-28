import os 
import shutil

chemin = os.path.dirname(__file__)

def inverseTrieFichier(chemin, cheminCourant = chemin):
    for fichier in os.listdir(cheminCourant):
        # Si le cheminCourant est un fichier (pas un dossier)
        if os.path.isfile(os.path.join(cheminCourant, fichier)):
            shutil.move(os.path.join(cheminCourant, fichier), os.path.join(chemin, fichier))
        # Si le cheminCourant est un dossier (pas un fichier)
        elif os.path.isdir(os.path.join(cheminCourant, fichier)):
            inverseTrieFichier(chemin, os.path.join(cheminCourant, fichier))
        else:
            exit()
    # Supprime les dossiers vides
    if cheminCourant != chemin:
        os.rmdir(cheminCourant)

inverseTrieFichier(chemin)