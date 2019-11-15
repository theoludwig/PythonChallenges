# Mastermind

## Notions abordées
- Condition et Boucle
- Liste 
- Module ```random```
- Fonctions split ou/et compréhension de liste

## Histoire et Règles

Le Mastermind est un jeu de société pour deux joueurs dont le but est de trouver un code. Jeu de réflexion, et de déduction, inventé dans les années 1970.
Le but est de deviner, par déductions successives, la couleur et la position des 5 pions cachés que l'adversaire a choisi (en l'occurrence dans notre cas ça sera python qui choisira aléatoirement).
Donc le joueur a 12 essais pour deviner la couleur et la position de la combinaison, à chaque fois que le joueur essaye, l'adversaire (en l'occurrence python encore une fois) devra nous indiquer si il y a des pions qui ont la bonne couleur et bien placés ou si il y a des bonnes couleurs mais qui sont mal placés, voilà donc à chaque tour le joueur réessaye une combinaison en prenant compte le résultat de l'adversaire pour essayer de deviner la combinaison en moins d'essais possible.

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

## Solutions

Le code de la solution a été écrit sous Windows 10 avec Python v3.7.4.

Au moment où vous lancez mon programme, vous devrez entrer le nombre d'essais maximum, le nombre de couleurs à deviner et le mode de jeu (Facile ou Difficile).

Si vous n'entrez rien, les valeurs par défaut s'appliqueront :
```
- 12
- 5
- Facile
```

Le mode de jeu Facile affiche la position des couleurs justes/mauvaise place alors que le mode difficile dit rien sur la position ou sur la couleur, il dit juste le nombre de couleur juste/mauvaise place.