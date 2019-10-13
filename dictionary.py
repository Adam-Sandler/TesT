#creation dictionnaire
#association cle valeur
import sys

dict = {"chat":"cat", "chien":"dog", "maison":"house", "carte":"map", "vert":"green", "voiture":"car", "gros":"big"}

#je crée une boucle infini avec while

while True:
    saisie_utilisateur = input("enter a word:")
    #conversion saisie utilisateur
    saisie_utilisateur = saisie_utilisateur.lower()
    #possibilité de quiter le programme si entrer "stop"
    if saisie_utilisateur == "stop":
        print("au revoir")
        sys.exit(0)
    #si le mot est dans le dict comme clé
    elif saisie_utilisateur in dict:
        print(dict[saisie_utilisateur])
    #sinon
    else:#et pas elif
        print("ce mot n'est pas dans le dictionnaire")
