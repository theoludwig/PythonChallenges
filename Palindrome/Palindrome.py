# Retourne un booléen, True si la phrase est un palindrome, False si ce n'est pas le cas
def estPalindrome(phrase):
    phraseTaille = len(phrase) - 1 # Taille de la phrase -1 car commence à 0
    nouvellePhrase = "" # Phrase qui va être inversée
    indexNormal = 0 # IndexNormal commence à compter à partir de 0
    # IndexInverser commence à compter à partir de la phraseTaille, puis descend de -1 à chaque tour de boucle
    for indexInverser in range(phraseTaille, -1, -1):
        # Si le caractère à l'indexInverser est le même que dans l'indexNormal alors tu l'ajoutes à nouvellePhrase
        if phrase[indexInverser] == phrase[indexNormal]:
            nouvellePhrase = nouvellePhrase + phrase[indexNormal]
        # Incrémente de 1 à chaque tour de boucle l'indexNormal
        indexNormal+=1
    return phrase == nouvellePhrase

# Retourne la phrase sans espaces
def enleveEspace(phrase):
    return phrase.replace(" ", "")

# Retourne la phrase sans accents
def enleveAccent(phrase):
    # Initialistion des listes contenant les accents
    avecAccent = ['é', 'è', 'ê', 'ë', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sansAccent = ['e', 'e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']

    # Boucle qui parcourt chaque accent dans la liste 'avecAccent'
    for i in range(len(avecAccent)):
        # Remplace toutes les occurences d'un accent par ça lettre sans accent
        phrase = phrase.replace(avecAccent[i], sansAccent[i])
    return phrase

# Demande à l'utilisateur une phrase à vérifier
phrase = input("Entrez une phrase : ") # exemple de phrase : LEON a rasé César à Noël

# Éxecution dans l'ordre : .lower pour mettre en minuscule puis enleveEspace puis enleveAccent et pour finir estPalindrome
if estPalindrome(enleveAccent(enleveEspace(phrase.lower()))):
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")

print(enleveAccent(enleveEspace(phrase.lower())))