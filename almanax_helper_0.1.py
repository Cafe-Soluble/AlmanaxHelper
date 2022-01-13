import csv
import tkinter
from tkinter import *
import pyperclip

version = "0.2"

def PressePapierOffrande(offrande_a_copier):
    try:
        pyperclip.copy(offrande_a_copier)
        return True
    except ValueError:
        return False

def getLigne(file, n, sep=","):
    f = open(file, 'r')
    # lire le contenu du fichier
    r = csv.reader(f, delimiter=sep)
    liste = list(r)
    f.close()

    if (n < len(liste)) and (n >= -len(liste)):
        res = liste[n]
    else:
        res = []
    return res

def FaireUneListeFinale(liste_ressource, liste_equipement, liste_consommable, liste_autre):
    liste_offrande_finale=[]
    for offrande in liste_ressource:
        liste_offrande_finale.append(offrande)
    for offrande in liste_equipement:
        liste_offrande_finale.append(offrande)
    for offrande in liste_consommable:
        liste_offrande_finale.append(offrande)
    for offrande in liste_autre:
        liste_offrande_finale.append(offrande)
    return liste_offrande_finale


def offrande_voulu():
    # demander le nombre de jour d'almanax voulu
    print("NOMBRE DE JOUR DE STOCK ALMANAX ?")
    nb_jour_voulu = input("Donnez un nombre entre 1 et 365 : ______ ")

    try:
        int(nb_jour_voulu)
        input_type = True
    except ValueError:
        input_type = False

    if input_type == True:
        nb_jour_voulu = int(nb_jour_voulu)

        if nb_jour_voulu >= 1 and nb_jour_voulu <= 365:
            liste_offrande_finale = []
            liste_offrande_ressources = []
            liste_offrande_equipements = []
            liste_offrande_consommables = []
            liste_offrande_autres = []
            for i in range(nb_jour_voulu):
                ligne_offrande = getLigne("data_almanax.csv", i)
                if ligne_offrande[3] == "ressource":
                    liste_offrande_ressources.append(ligne_offrande)
                elif ligne_offrande[3] == "equipement" or ligne_offrande[3] == "arme":
                    liste_offrande_equipements.append(ligne_offrande)
                elif ligne_offrande[3] == "consommable":
                    liste_offrande_consommables.append(ligne_offrande)
                elif ligne_offrande[3] == "autre":
                    liste_offrande_autres.append((ligne_offrande))
                else:
                    print("ERREUR MOTHERFUCKER")

            return FaireUneListeFinale(liste_offrande_ressources, liste_offrande_equipements, liste_offrande_consommables, liste_offrande_autres)




        else:
            print("Erreur : le nombre doit être compris entre 1 et 365")
    else:
        print("Erreur : l'input doit être un entier")

def JourSuivant():
    if jour_actuel.get() < len(liste_offrande)-1:
        jour_actuel.set(jour_actuel.get() + 1)
        print("Jour actuel : "+str(jour_actuel.get()))
        etat['text'] = str(liste_offrande[jour_actuel.get()][1]) + " x " + str(liste_offrande[jour_actuel.get()][2])
        label_subtitle['text'] = liste_offrande[jour_actuel.get()][3]

        ChangerCouleurFond(liste_offrande[jour_actuel.get()][3])

        PressePapierOffrande(liste_offrande[jour_actuel.get()][2])

    else:
        label_subtitle['text'] = ""
        etat['text'] = "Terminé."

def JourPrecedent():
    if jour_actuel.get() >=1:
        jour_actuel.set(jour_actuel.get() - 1)
        print("Jour actuel : "+str(jour_actuel.get()))
        etat['text'] = str(liste_offrande[jour_actuel.get()][1]) + " x " + str(liste_offrande[jour_actuel.get()][2])
        label_subtitle['text'] = liste_offrande[jour_actuel.get()][3]

        ChangerCouleurFond(liste_offrande[jour_actuel.get()][3])

        PressePapierOffrande(liste_offrande[jour_actuel.get()][2])

    else:
        etat['text'] = ""
        label_subtitle['text'] = "Start."


def ChangerCouleurFond(type_offrande):
    if type_offrande == "ressource":
        AppliquerSurTouteLaFenetre(couleur_fond_ressource)
    elif type_offrande == "arme" or type_offrande == "equipement":
        AppliquerSurTouteLaFenetre(couleur_fond_equipement)
    elif type_offrande == "consommable":
        AppliquerSurTouteLaFenetre(couleur_fond_consommable)
    elif type_offrande == "autre":
        AppliquerSurTouteLaFenetre(couleur_fond_autre)
    else:
        AppliquerSurTouteLaFenetre('red')
        print("Error background")

def AppliquerSurTouteLaFenetre(couleur):
    window['bg']=couleur
    etat['bg']=couleur
    label_subtitle['bg']=couleur
    label_title['bg']=couleur
    button['bg']=couleur
    button2['bg']=couleur
    frame1['bg']=couleur
    frame2['bg']=couleur


liste_offrande = offrande_voulu()


couleur_fond_ressource = '#c8e6bc'
couleur_fond_equipement = '#c4f7fa'
couleur_fond_consommable = "#c7afd6"
couleur_fond_autre = "#ede996"

#--------------------- GUI --------------------


window = Tk()
window.wm_attributes("-topmost", 1)

font_button = ""
font_all = ""
jour_actuel = tkinter.IntVar()
jour_actuel.set(0)

print("Offrande sur " + str(jour_actuel.get()) + "jours")
print("Taille de la liste :" + str(len(liste_offrande)))
print("Mise en cache du presse-papier :")
print(PressePapierOffrande(liste_offrande[jour_actuel.get()][2]))
texte_etat = str(liste_offrande[jour_actuel.get()][1]) + " x " + str(liste_offrande[jour_actuel.get()][2]) #texte de base
type_offrande= liste_offrande[jour_actuel.get()][3]


window.title("ALMANAX HELPER"+version)
window.geometry("600x200")
window.minsize(200,75)
window.maxsize(700,475)
window['bg']=couleur_fond_ressource

frame1=Frame(window, bg=couleur_fond_ressource)
frame2=Frame(window, bg=couleur_fond_ressource)

# FRAME 1 -----------------------------------

label_title = Label(frame1, text="Almanax Helper"+version, font=("Cute Letters", 35), bg=couleur_fond_ressource, fg="#0f0503")
label_title.pack()


label_subtitle = Label(frame1, text=type_offrande, font=("Cute Letters", 25), bg=couleur_fond_ressource, fg="#0f0503")
label_subtitle.pack()



etat=Label(frame1, text=texte_etat, font=("Cute Letters", 25), bg=couleur_fond_ressource, fg="#0f0503")
etat.pack()

#bouton +1 jour
button=Button(frame2, text="Jour suivant", cursor="dotbox", font=("Cute Letters", 20), bg =couleur_fond_ressource, fg="#0f0503", command=JourSuivant)
button.pack(side='right', padx=10)

#bouton - 1 jour
button2=Button(frame2, text="Jour précédent", cursor="dotbox", font=("Cute Letters", 20), bg =couleur_fond_ressource, fg="#0f0503", command=JourPrecedent)
button2.pack(side='left', padx=10)

frame1.pack(padx=5, pady=5)
frame2.pack(padx=5, pady=5)

window.mainloop()

