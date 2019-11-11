# Mastermind

## Difficulté
Pas évident au premier abord, je vous conseille avant de taper du code de mettre en commentaire comment vous allez procéder. 

## Notions abordées
- Condition 
- Boucle
- Liste 
- Module random
- Fonctions split ou/et compréhension de liste

## Histoire et Règles
```
Le Mastermind est un jeu de société pour deux joueurs dont le but est de trouver un code. Jeu de réflexion, et de déduction, inventé dans les années 1970.
Le but est de deviner, par déductions successives, la couleur et la position des 5 pions cachés que l'adversaire a choisi (en l'occurrence dans notre cas ça sera python qui choisira aléatoirement).
Donc le joueur a 12 essais pour deviner la couleur et la position de la combinaison, à chaque fois que le joueur essaye, l'adversaire (en l'occurrence python encore une fois) devra nous indiquer si il y a des pions qui ont la bonne couleur et bien placés ou si il y a des bonnes couleurs mais qui sont mal placés, voilà donc à chaque tour le joueur réessaye une combinaison en prenant compte le résultat de l'adversaire pour essayer de deviner la combinaison en moins d'essais possible.
```

## Énoncé
Les couleurs disponibles seront :
```py
couleurDisponible = ["Vert", "Blanc", "Rouge", "Jaune", "Bleu", "Noir", "Rose", "Violet", "Orange", "Gris"]
```
L'ordinateur devra créer une liste qui contiendra 5 couleurs prises au hasard dans les couleurs disponibles (il peut avoir plusieurs fois la même couleur dans une combinaison)
Le joueur tapera les couleurs dans un input qui formera une liste :
```py
couleurEntree = input("Entrez les couleurs : ").split(", ")
```
Si la combinaison à deviner est : 
```py 
['Rose', 'Gris', 'Rouge', 'Bleu', 'Jaune'] 
```
Et que le joueur tape :
```
Rose, Rouge, Gris, Vert, Blanc
```
Alors python devra afficher :
```
Couleurs juste et bonne place :  [['Rose', 1]]        
Couleurs mauvaise place :  [['Rouge', 2], ['Gris', 3]]
Il vous reste 11 essais...
```

Bon courage! 😃