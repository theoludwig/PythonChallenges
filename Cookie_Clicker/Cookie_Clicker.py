import tkinter
from PIL import Image, ImageTk # pip install Pillow
import os
import json

dossier_courant = os.path.dirname(__file__)
chemin_nombreClique = os.path.join(dossier_courant, "nombreClique.json")
chemin_imageCookie = os.path.join(dossier_courant, "cookie.png")
chemin_iconCookie = os.path.join(dossier_courant, "cookie.ico")

try:
    with open(chemin_nombreClique, "r") as f:
        nombreCompteur = json.load(f)[0]
except:
    nombreCompteur = 0

def compteur():
    global nombreCompteur 
    nombreCompteur += 1
    labelCompteur.config(text = nombreCompteur)

# Paramètres fenètre
window = tkinter.Tk()
window.title("Cookie Clicker")
window.geometry("640x540")
window.minsize(480, 360)
window.iconbitmap(chemin_iconCookie)

# Titre 
labelTitle = tkinter.Label(window, text="Cookie Clicker", font=("Arial", 25))
labelTitle.pack()

# Compteur
labelCompteur = tkinter.Label(window, text=nombreCompteur, font=("Arial", 18))
labelCompteur.pack()

# Image 
img = Image.open(chemin_imageCookie)
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)
panel = tkinter.Button(window, image = img, bd=0, command=compteur)
panel.pack(expand="yes")

# Affiche la fenètre
window.mainloop()

# Enregistre le compteur dans le json
with open(chemin_nombreClique, "w") as f:
    json.dump([nombreCompteur], f)