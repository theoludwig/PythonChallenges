from fractions import Fraction

def mesurePrincipale(numerateur, denominateur):
  # abs renvoie la valeur absolue
  if numerateur/denominateur < 0:
    while abs(numerateur / denominateur) > 1:
      numerateur=numerateur + 2 * denominateur
  else:
    while abs(numerateur / denominateur) > 1:
      numerateur=numerateur - 2 * denominateur
  return [numerateur, denominateur]

print ("On entre la valeur de l'angle sous la forme N/D*pi")
numerateur = input("Entrez un numérateur : ")
denominateur = input("Entrez un dénominateur : ")

try: 
  numerateur = int(numerateur)
  denominateur = int(denominateur)
  resultat = mesurePrincipale(numerateur, denominateur)
  fractionReduite = Fraction(resultat[0], resultat[1])
  print("La mesure principale est", fractionReduite, "π")
except:
  print("Oups, il y a une erreur. \n") 