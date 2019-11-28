# Trier des fichiers

## Notions abordées

- Boucle et Condition
- Fonction (et récursivité)
- Liste
- Module ```os```
- Module ```shutil```

## Énoncé

Vous devez créer une fonction qui trie automatiquement des fichiers dans des sous-dossiers en fonction de leur type (et donc de leur extension).
Facultatif : Réaliser la fonction inverse → déplacer les fichiers des sous-dossiers dans le dossier principale.

Exemple :
```
├── facture.pdf 
├── Tour_eiffel.jpg     
├── Logo.png    
├── Despacito.mp3 
├── Court_metrage.mp4  
```

Résultat : Videos
```
├── Documents
|   ├── Facture.pdf 
├── Images  
│   ├── Tour_eiffel.jpg     
│   ├── Logo.png    
├── Musiques
│   ├── Despacito.mp3 
├── Videos    
│   ├── Court_metrage.mp4        
```