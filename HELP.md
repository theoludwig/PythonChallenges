# Méthodologie pour résoudre un problème 

Afin de vous aider à résoudre ses différents exercices, je vais vous partager ma méthodologie que j'utilise quand je suis face à un problème donné.
C'est une méthodologie parmi tant d'autres et malheureusement ça ne fait pas des miracles alors motivez-vous et au boulot ! 😉

## Décrire la solution

Concrètement, vous allez rédiger les **étapes en français**, c'est-à-dire vous écrivez selon vous ce qu'il faudrait faire (ça peut être en vrac au début, juste toutes les idées qui vous passent par la tête), n'hésitez pas à prendre un brouillon et à faire un schéma si cela vous aide.

Posez-vous toujours la question de comment **nous** humain réglons ce problème, mettez ça sur un **brouillon étape par étape**.

## Diviser le problème en plusieurs sous-problèmes

Une fois que vous avez des idées comme ça en français, vous pouvez vous concentrer chaque étape un à un.
Si vraiment vous n'avez absolument aucune idée, aucune piste, de comment résoudre l'exercice, c'est probablement qu'il est trop difficile pour votre niveau.
Si l'exercice est de votre niveau, normalement, vous devrez avoir au moins des pistes.
Après aussi, il faut bien connaître le langage. **Connaître les méthodes des chaînes de caractères, des listes, des nombres entiers etc**, ça aide à trouver des solutions.
Vous n'êtes pas obligé de tout connaître. Vous pouvez faire une recherche sur **google (sur Stack Overflow)** devrait vous permettre de trouver la méthode ou fonction pour faire cette étape.

## Exemple concret :

Énoncé : *Vous devez créer une liste qui contiendra des sous-listes, pour chaque phrase une sous-liste contenant les mots dont la taille ainsi que sa position dans la phrase est paire.*

* Étapes en français :
```
- Trouver les phrases dans ton texte.
- Trouver les mots dans ta phrase.
- Compter la taille d'un mot.
- Vérifier si la taille du mot et que sa position est paire
- Rajouter les éléments qui vérifient cette condition dans une nouvelle liste
```

* Sous-problèmes :
```
- Trouver les phrases dans ton texte : qu'est-ce qui définit une phrase ? Généralement un point. Comment trouver les points dans une chaîne de caractères ? Tu peux utiliser split en python par exemple.
- Compter la taille d'un mot : Une fonction qui nous donne la taille du mot ?
- Position paire : Boucle qui énumère sur la liste avec un i qui vaut 1 au début puis à chaque itération de boucle fait + 1, pourquoi 1 car une liste commence par 0...
etc.
...
```

Comme je l'ai dit, il est **inutile de tout savoir** et c'est même quasiment **impossible**, vaut mieux connaître en survol les fonctions mais si vous avez besoin de la syntaxe exacte, vous **rechercherez sur internet**, par exemple pour trouver la taille d'un mot :
De préférence en anglais : ```length string Python```, 1er résultat, vous trouverez la fonction ```len()```, par ailleurs noté que je n'ai pas fait de phrase, mettez des mots-clés ça sera plus efficace.

Ainsi de suite...

Bon courage ! 🙂