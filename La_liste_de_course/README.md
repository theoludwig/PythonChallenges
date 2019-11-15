# La liste de course

## Notions abordées

- Conditions, Boucle et Liste
- Modules ```os``` et ```json```
- Try et except (facultatif)

## Énoncé

Vous devez demander à l'utilisateur de choisir une option comme ceci :
```py
affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Sauvegarder la liste
"""
```

Ensuite selon l'option choisis par l'utilisateur, ajoute/enlève un élément, afficher/vider la liste.

Puis une fois que l'utilisateur a finis de rajouter ces élements, il peut choisir l'option 5 pour sauvegarder la liste dans le dossier courant dans un fichier json, la prochaine fois que l'utilisateur relance le programme, il faudra que le programme s'occupe de charger le json afin de remettre la liste que l'utilisateur avait écrit.

## Solutions

Le code de la solution a été écrit sous Windows 10 avec Python v3.7.4.

Afin de rendre le terminal plus clair à certains endroits je clear la console pour avoir un meilleur affichage, sachez que cette commande est différente si vous êtes sur Mac/Linux donc si vous obtenez une erreur en lançant mon programme veuillez enlever les lignes :
```py
os.system('cls')
```