# Encodage caractère

## Notions abordées

- Condition
- Fonctions utilisées : ```int(), hex(), bin()```

## Énoncé

Vous devez demander à l'utilisateur de choisir une option comme ceci :
```py
affichage = """
Choisissez une option:
\t1: Décimal en Binaire
\t2: Binaire en Décimal
\t3: Décimal en Hexadecimal
\t4: Hexadecimal en Décimal
\t5: Binaire en Hexadécimal
\t6: Hexadécimal en Binaire
"""
```

Puis vous devez pour chaque option calculer la conversion, convertir un nombre décimal en binaire, inversement, etc. 

__Exemple :__
Si l'utilisateur choisis la 1ère option et ensuite qu'il écrit 2, le programme devra afficher : 
```
Décimal : 2 
Binaire : 10
```
