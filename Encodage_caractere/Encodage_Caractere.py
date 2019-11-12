# Formate les nombres avec des espaces (ex : 76120 = 76 120)
def formatNumberResult(x):
    x = int(x)
    return '{:,}'.format(x).replace(',', ' ')

affichage = """
Choisissez une option:
\t1: Décimal en Binaire
\t2: Binaire en Décimal
\t3: Décimal en Hexadecimal
\t4: Hexadecimal en Décimal
\t5: Binaire en Hexadécimal
\t6: Hexadécimal en Binaire
\t7: Quitter le programme
"""

option = "0"
resultat = ""
while option != "7":
    option = input(affichage)
    try:
        # Décimal en Binaire
        if option == "1":
            valeur = input("Votre valeur : ")
            valeur = valeur.replace(" ", "")
            resultat = bin(int(valeur)).replace("0b", "")
            print(f"Décimal : {formatNumberResult(valeur)} \nBinaire : {resultat} \n")

        # Binaire en Décimal
        elif option == "2":
            valeur = input("Votre valeur : ")
            resultat = int(valeur, 2)
            print(f"Binaire : {valeur} \nDécimal : {formatNumberResult(resultat)} \n")

        # Décimal en Hexadécimal
        elif option == "3":
            valeur = input("Votre valeur : ")
            valeur = valeur.replace(" ", "")
            resultat = hex(int(valeur)).replace("0x", "").upper()
            print(f"Décimal : {formatNumberResult(valeur)} \nHexadécimal : {resultat} \n")

        # Hexadécimal en Décimal
        elif option == "4":
            valeur = input("Votre valeur : ")
            resultat = int(valeur, 16)
            print(f"Hexadécimal : {valeur} \nDécimal : {formatNumberResult(resultat)}")

        # Binaire en Hexadécimal
        elif option == "5":
            valeur = input("Votre valeur : ")
            resultat = hex(int(valeur, 2)).replace("0x", "").upper()
            print(f"Binaire : {valeur} \nHexadécimal : {resultat}")

        # Hexadécimal en Binaire
        elif option == "6":
            valeur = input("Votre valeur : ")
            resultat = bin(int(valeur, 16)).replace("0b", "")
            print(f"Hexadécimal : {valeur} \nBinaire : {resultat}")
    except:
        print("Vous n'avez pas rentré de valeur valide.\n")

print("Vous avez quitté le programme.")