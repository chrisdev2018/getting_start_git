import string
from os import path 
import pickle

def lettres_trouvees(_lettre, mot):
    mot_tmp = str()
    i = 0

    #Ici on obtient les lettres que l'on a déjà trouvé
    while i < len(mot):
        if _lettre == mot[i]:
            mot_tmp += mot[i]
            i += 1
        else:
            mot_tmp += '*'
            i += 1    
    return mot_tmp


def lettres_a_trouvees(_lettre, mot):
    mot_tmp = str()
    i = 0

    #Ici on obtient les lettres que l'on a pas encore trouvé
    while i < len(mot):
        if _lettre == mot[i]:
            mot_tmp += '*'
            i += 1
        else:
            mot_tmp += mot[i]
            i += 1    
    return mot_tmp


def nb_lettres_trouvees(mot):
    i = 0 
    nb_lettre_trouve = 0
    while i < len(mot):
        if mot[i] != '*':
            nb_lettre_trouve += 1
            i += 1 
        else:
            i += 1

    return nb_lettre_trouve        

    #print("Il vous reste encore",nb_lettre_trouve)                


def lettre_ok():
    est_lettre = False
    lettre = ''

    while est_lettre == False:
        lettre = input("\nSaisir une lettre : ")
        if lettre in string.ascii_letters and lettre != "":
                est_lettre = True
                break
    return lettre 
 

def resultat_provisoire(_nb_lettres_trouvees, mot_lettre, _nb_lettres_a_trouvees, coups_restants):
    
    print("\nVous avez déja trouve {} lettres '{}' il vous reste encore {} lettres a trouver".format(_nb_lettres_trouvees,mot_lettre, _nb_lettres_a_trouvees))
    print("\nEt il ne vous reste plus que {} coups dans cette partie".format(coups_restants))
    print("\n")      
     

def enregistrer_score(joueur, score, nom_fichier):
    dico = lire_fichier(nom_fichier)

    for cle in dico:
        if cle == joueur:
            dico[cle] = score
            break
    ecrire_fichier(dico, nom_fichier)        


def lire_fichier(nom_fichier):
    with open(nom_fichier, 'rb') as fichier:
        mon_pickler = pickle.Unpickler(fichier)
        contenu = mon_pickler.load()
        return contenu


def ecrire_fichier(_objet, nom_fichier):    
    with open(nom_fichier, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(_objet)


def verifer_joueur(nom_joueur, nom_fichier):
    
    a_score = False

    if path.exists(nom_fichier):
        dico = lire_fichier(nom_fichier)
        #print(dico)

        if bool(dico):
            for cle in dico:
                if cle == nom_joueur:
                    a_score = True
                    break
            if a_score == False:
                dico[nom_joueur] = 0
                ecrire_fichier(dico, nom_fichier)

        else:
            dico[nom_joueur] = 0
            ecrire_fichier(dico, nom_fichier)    
         
    else:
        dico={}
        ecrire_fichier(dico, nom_fichier)

def afficher_scores(nom_fichier):
    scores = lire_fichier(nom_fichier)

    for cle in scores:
        print("\n --> [{} : {}]".format(cle, scores[cle]))



