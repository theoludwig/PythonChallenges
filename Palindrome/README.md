# Palindrome

## Notions abordées

- Boucle, Condition
- Fonction

## Énoncé

Vous devez créer une fonction qui doit renvoyer ```True``` si la phrase entrée par l'utilisateur est un **palindrome** et ```False``` si ce n'est pas le cas.

Un palindrome est une figure de style désignant un texte ou un mot dont l'ordre des lettres reste le même qu'on le lise de gauche à droite ou de droite à gauche.
Exemple : 'kayak', 'radar' ...

Vous devrez faire ceci sans utiliser la fonction toute faites de python  ```reverse```.

Exemple :
```py 
phrase = 'kayak'
```

Résultat :
```py
>>> True
```

Pour aller plus loin : faire fonctionner la fonction estPalindrome() pour une phrase, par exemple : « LEON a rasé César à Noël ». Il faudra éliminer les espaces, transformer les lettres accentuées et/ou en majuscules en lettres minuscules non accentuées.

Exemple :
```py
phrase = 'LEON a rasé César à Noël'
```

Résultat :
```py
>>> 'leonarasecesaranoel'
>>> True
```