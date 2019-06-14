from os import system
from fonctions import *
from donnees import *
from random  import *

print("*****************************************************\n")
print("*         Bienveue dans le jeu 'le Pendu'           *\n")
print("*****************************************************\n")



nom_joueur = input("Veuillez Saisir votre nom : ")

verifer_joueur(nom_joueur, fichier_score)

print("\nVous allez commencer la partie\n")
system("pause")

mot_choisi = choice(liste_mots)

#On peut commencer
coups_restant = coup_max
score = 0
reste_a_trouver = mot_choisi
jeu_termine = False
message_de_fin = ""
_nb_lettres_trouvees = 0

while coups_restant > 0:
    coups_restant -= 1
    lettre = lettre_ok()
    mot_deja_trouve = lettres_trouvees(lettre, reste_a_trouver)
    reste_a_trouver = lettres_a_trouvees(lettre, reste_a_trouver)

    _nb_lettres_trouvees += nb_lettres_trouvees(mot_deja_trouve)
    _nb_lettres_a_trouvees = nb_lettres_trouvees(reste_a_trouver)

    resultat_provisoire(_nb_lettres_trouvees,mot_deja_trouve, _nb_lettres_a_trouvees, coups_restant)

    if _nb_lettres_a_trouvees == 0:
        score = coups_restant
        jeu_termine = True        
        message_de_fin = "Bravo vous avez trouvé le mot en {} coups!!!".format(coup_max-coups_restant)
        break

    elif coups_restant == 0:
        score = coups_restant
        message_de_fin = "\nDésolé mais vous tenterez votre chance une autre fois..."
        jeu_termine = True

print("\n")
system("pause")  
print("\nEnregistrement du score...\n")
enregistrer_score(nom_joueur, score, fichier_score)

question = input("\nVoulez-vous consulter la liste des scores ? O/Y : ")

if question == "y" or question == "Y":
    afficher_scores(fichier_score)


input("\nAttendez 3 secondes et appuyez sur une touche pour quitter")      





