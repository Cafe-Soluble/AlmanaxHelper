import csv
import tkinter
from tkinter import *
import pyperclip
from urllib.request import urlopen
import datetime
import time
from datetime import timedelta
import re
from html import unescape
import threading

version = "0.5"
global NBOFFRANDE
NBOFFRANDE = 999

def Run():
    t1 = threading.Thread(target=DataAlmanax)

    t1.start()



def ScriptDemarrage():
    print("Démarrage du scrapping ", end="", flush=True)
    time.sleep(0.05)
    print(".", end="", flush=True)
    time.sleep(0.05)
    print(".", end="", flush=True)
    time.sleep(0.05)
    print(".", end="", flush=True)
    time.sleep(0.05)
    print(" Ok.")

def DataAlmanax():
    aujourdhui = datetime.date.today()
    fichier = open("data_almanax.csv", "w")
    fichier.close()

    i = 0
    #while i < 365:
    while i < int(NBOFFRANDE):
        fichier = open("data_almanax.csv", "a")
        i = i + 1

        TupleAlmanax = ScrapAlmanax("http://www.krosmoz.com/fr/almanax/" + str(aujourdhui))
        typeObjet = type_objet(TupleAlmanax[1])
        EcrireFichierAlmanax(aujourdhui, TupleAlmanax[0], TupleAlmanax[1], typeObjet, fichier)
        aujourdhui = DatePlusUnJour(aujourdhui)
        fichier.close()


def ScrapAlmanax(url):
    htlm_code = urlopen(url).read().decode("utf-8")
    #print(htlm_code)
    start = htlm_code.find("Récupérer ") + len("Récupérer ")
    end = htlm_code.find(" et rapporter ")
    full_sentence = str(htlm_code[start:end])
    #print(full_sentence)
    nombre=re.findall(r'\d+',full_sentence)
    nombre=nombre[0]
    objet_a_acheter=full_sentence.replace(nombre+" ", "", 1)
    return nombre, objet_a_acheter

def EcrireFichierAlmanax(dateAlmanax, quantiteAlmanax, ressourceAlmanax, type, fichier):
    ligneaecrire=str(dateAlmanax) + "," + quantiteAlmanax + "," + ressourceAlmanax + "," + type + "\n"
    #print(ligneaecrire)
    fichier.write(ligneaecrire)

def DatePlusUnJour(la_date):

    la_date = la_date + timedelta(days = 1)
    return la_date


def ExisteDansFichier(objet_a_trouver, path_file):

    #file = open(path_file, 'r', encoding='utf-8')
    file = open(path_file, 'r', encoding='utf-8')
    texte_html=file.read()
    texte_utf8=unescape(texte_html)
    if texte_utf8.find(objet_a_trouver) >= 0:
        file.close()
        return True
    else:
        file.close()
        return False

def type_objet(objet_a_trouver):
    path_file_ressources = 'ressources_dofus.txt'
    path_file_consommables = 'consommables_dofus.txt'
    path_file_armes = 'armes_dofus.txt'
    path_file_equipements = 'equipements_dofus.txt'

    if ExisteDansFichier(objet_a_trouver, path_file_ressources) == True:
        #print("L'item est une ressource")
        return "ressource"
    elif ExisteDansFichier(objet_a_trouver, path_file_consommables) == True:
        #print("L'item est une consommable")
        return("consommable")
    elif ExisteDansFichier(objet_a_trouver, path_file_armes) == True:
        #print("L'item est une arme")
        return("arme")
    elif ExisteDansFichier(objet_a_trouver, path_file_equipements) == True:
        #print("L'item est un équipement")
        return("equipement")
    else:
        return("autre")

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


    try:
        int(NBOFFRANDE)
        input_type = True
    except ValueError:
        input_type = False

    if input_type == True:
        nb_jour_voulu = int(NBOFFRANDE)

        if nb_jour_voulu >= 1 and nb_jour_voulu <= 365:
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
                    exit()

            return FaireUneListeFinale(liste_offrande_ressources, liste_offrande_equipements, liste_offrande_consommables, liste_offrande_autres)




        else:
            print("Erreur : le nombre doit être compris entre 1 et 365")
            exit()
    else:
        print("Erreur : l'input doit être un entier")
        exit()

def JourSuivant():
    if jour_actuel.get() < len(liste_offrande)-1:
        jour_actuel.set(jour_actuel.get() + 1)
        print("Jour actuel : "+str(jour_actuel.get()+1))
        print(liste_offrande[jour_actuel.get()])
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
        print("Jour actuel : "+str(jour_actuel.get()+1))
        print(liste_offrande[jour_actuel.get()])
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


# PREMIERE FENETRE ---------------------------------------------------------------------------------------------------------------




def Accueil():
    x=15
    y = 15
    font_style = "Cute Letters"
    font_size = 18
    padx = 17
    pady = 17
    button1semaine=Button(frame1, text="7 Jours", cursor="dotbox", font=(font_style, font_size), command=button_1semaine)
    button2semaines=Button(frame1, text="15 Jours", cursor="dotbox", font=(font_style, font_size), command=button_2semaines)
    button3semaines=Button(frame1, text="3 Semaines", cursor="dotbox", font=(font_style, font_size), command=button_3semaines)
    button1mois=Button(frame1, text="1 Mois", cursor="dotbox", font=(font_style, font_size), command=button_1mois)
    button2mois = Button(frame1, text="2 Mois", cursor="dotbox", font=(font_style, font_size), command=button_2mois)
    button3mois=Button(frame1, text="3 Mois", cursor="dotbox", font=(font_style, font_size), command=button_3mois)
    button6mois=Button(frame1, text="6 Mois", cursor="dotbox", font=(font_style, font_size), command=button_6mois)
    button1an=Button(frame1, text="1 An", cursor="dotbox", font=(font_style, font_size), command=button_1an)
    buttonautre = Button(frame1, text="Autre", cursor="dotbox", font=(font_style, font_size), command=button_autre)
    button1semaine.grid(column=0, row=0, pady=pady, padx=padx)
    button2semaines.grid(column=1, row=0, pady=pady, padx=padx)
    button3semaines.grid(column=2, row=0, pady=pady, padx=padx)
    button1mois.grid(column=0, row=1, pady=pady, padx=padx)
    button2mois.grid(column=1, row=1, pady=pady, padx=padx)
    button3mois.grid(column=2, row=1, pady=pady, padx=padx)
    button6mois.grid(column=0, row=2, pady=pady, padx=padx)
    button1an.grid(column=1, row=2, pady=pady, padx=padx)
    buttonautre.grid(column=2, row=2, pady=pady, padx=padx)
    FirstWindow.mainloop()

def button_1semaine():
    print("Choix = 7 jours")
    global NBOFFRANDE
    NBOFFRANDE = 7
    FirstWindow.destroy()
def button_2semaines():
    print("Choix = 15 jours")
    global NBOFFRANDE
    NBOFFRANDE = 15
    FirstWindow.destroy()
def button_3semaines():
    print("Choix = 3 semaines")
    global NBOFFRANDE
    NBOFFRANDE = 22
    FirstWindow.destroy()
def button_1mois():
    print("Choix = 1 mois")
    global NBOFFRANDE
    NBOFFRANDE = 31
    FirstWindow.destroy()
def button_2mois():
    print("Choix = 2 mois")
    global NBOFFRANDE
    NBOFFRANDE = 60
    FirstWindow.destroy()
def button_3mois():
    print("Choix = 3 mois")
    global NBOFFRANDE
    NBOFFRANDE = 90
    FirstWindow.destroy()
def button_6mois():
    print("Choix = 6 mois")
    global NBOFFRANDE
    NBOFFRANDE = 180
    FirstWindow.destroy()
def button_1an():
    print("Choix = 1 an")
    global NBOFFRANDE
    NBOFFRANDE = 365
    FirstWindow.destroy()




def ChoixInput():
    ChoixWindow = Tk()  # Fenetre pour choix manuel nb jour

    def button_choice_pressed():
        choixUtilisateur = InputUser.get()
        print("L'utilisateur a choisi "+choixUtilisateur+" jours d'offrande.")
        try:
            if int(choixUtilisateur) > 0 and int(choixUtilisateur)<365:
                global NBOFFRANDE
                NBOFFRANDE = int(choixUtilisateur)
                ChoixWindow.destroy()
            else:
                print("Erreur dans le nombre rentré")
                ChoixWindow.destroy()
                quit()
        except ValueError:
            print("Le nombre rentré n'est pas un entier")
            ChoixWindow.destroy()
            quit()


    ChoixWindow.title("ALMANAX HELPER " + version)
    ChoixWindow.geometry("600x150")
    textInputUser= Label(ChoixWindow, text="Entrez le nombre de jours : ", font=("Cute Letters", 22))
    InputUser = Entry(ChoixWindow)
    buttonChoice = Button(ChoixWindow, text="Valider", cursor="dotbox", font=("Cute Letters", 22), command=button_choice_pressed)

    textInputUser.pack(pady=10)
    InputUser.pack(pady=10)
    buttonChoice.pack(pady=10)

    ChoixWindow.mainloop()


def button_autre():
    print("Choix = Autre")
    FirstWindow.destroy()
    ChoixInput()



# FIN PREMIERE FENETRE -------------------------------------------------------------------------------------------------------

# FENETRE ATTENTE -------------------

def AttenteTelechargement():



    fichier_offrande = open('data_almanax.csv', 'r')
    text = fichier_offrande.readlines()
    NumberOfLine = len(text)
    if NumberOfLine < NBOFFRANDE:
        print("Liste des offrandes en téléchargement... "+str(NumberOfLine)+"/"+str(NBOFFRANDE))
        affichage.config(text="Téléchargement des offrandes... \n"+str(NumberOfLine)+"/"+str(NBOFFRANDE))
        affichage.after(1000, AttenteTelechargement)
    else:
        WindowAttente.destroy()


# FIN FENETRE ATTENTE ---------------



# -------------- VARIABLES -------------
couleur_fond_ressource = '#c8e6bc'
couleur_fond_equipement = '#c4f7fa'
couleur_fond_consommable = "#c7afd6"
couleur_fond_autre = "#ede996"

# -------------- Script -------------


FirstWindow = Tk() #Fenetre d'accueil pour choix nb jour
FirstWindow.title("ALMANAX HELPER "+version)
FirstWindow.geometry("600x200")
frame1 = Frame(FirstWindow)
frame1.pack()

Run() # lance le scrapping
ScriptDemarrage() # fais gagner du temps

Accueil() #choix du nombre de jour dans variable global NBOFFRANDE



WindowAttente = Tk() #Fenetre d'attente
WindowAttente.title("ALMANAX HELPER "+version)
WindowAttente.geometry("600x150")
frame1 = Frame(WindowAttente)
frame1.pack()
if NBOFFRANDE == 999: #signifie que l'utilisateur n'a pas pu choisir le nb de jour d'offrande
    print("Extinction du logiciel.")
    quit()
else:
    print("Début du téléchargement des offrandes.")
affichage = Label(frame1, text="En attente du téléchargement des offrandes ...", font=("Cute Letters", 22), fg="#0f0503")
affichage.pack(pady=40)
AttenteTelechargement()
WindowAttente.mainloop()



liste_offrande = offrande_voulu()

#--------------------- GUI --------------------


window = Tk()
window.wm_attributes("-topmost", 1)

font_button = ""
font_all = ""
jour_actuel = tkinter.IntVar()
jour_actuel.set(0)



print("Offrande sur " + str(len(liste_offrande)) + " jours")
time.sleep(0.05)
print("Taille de la liste : " + str(len(liste_offrande)))
time.sleep(0.05)
print("Mise en cache du presse-papier : ", end = "", flush=True)
time.sleep(0.05)
print(PressePapierOffrande(liste_offrande[jour_actuel.get()][2]))
time.sleep(0.05)
print("Jour actuel : "+str(jour_actuel.get()+1))
time.sleep(0.05)
print(liste_offrande[jour_actuel.get()])
texte_etat = str(liste_offrande[jour_actuel.get()][1]) + " x " + str(liste_offrande[jour_actuel.get()][2]) #texte de base
type_offrande= liste_offrande[jour_actuel.get()][3]


window.title("ALMANAX HELPER "+version)
window.geometry("600x200")
window.minsize(200,75)
window.maxsize(700,475)
window['bg']=couleur_fond_ressource

frame1=Frame(window, bg=couleur_fond_ressource)
frame2=Frame(window, bg=couleur_fond_ressource)

# FRAME 1 -----------------------------------

label_title = Label(frame1, text="Almanax Helper "+version, font=("Cute Letters", 35), bg=couleur_fond_ressource, fg="#0f0503")
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


