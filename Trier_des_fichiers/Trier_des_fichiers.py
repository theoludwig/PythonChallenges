import os
import shutil

chemin = os.path.dirname(__file__)
listeFichiers = [f for f in os.listdir(chemin) if os.path.isfile(os.path.join(chemin, f))] # Liste contenant tous les fichiers (dossier exclu)

dictionnaireDossier = {
    "Musiques": (".mp3", ".wav"),
    "Videos": (".mp4", ".mov"),
    "Images": (".png", ".jpg", ".jpeg", ".gif"),
    "Documents": (".pdf", ".json", ".txt")
}

def trieFichier(cheminFichier, fichier, cle):
    # Accède au tuple contenant toutes les extensions de fichiers 
    if fichier.endswith(dictionnaireDossier[cle]):
        # Créer le dossier s'il n'existe pas 
        dossier = os.path.join(chemin, cle)
        if not os.path.exists(dossier): 
            os.makedirs(dossier)
        # Déplace le fichier dans le bon dossier
        cheminCible = os.path.join(chemin, cle + "/" + fichier)
        shutil.move(cheminFichier, cheminCible)

# Trie les fichiers 
for fichier in listeFichiers:
    cheminFichier = os.path.join(chemin, fichier)
    for cle in dictionnaireDossier.keys():
        trieFichier(cheminFichier, fichier, cle)