#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:52:11 2020

@author: clementmutez
"""

#Charger les données du fichier et les stocker dans un tableau
def LireFichier():
    #ouverture fichier
    fichier = open(r"data.csv", "r")
    liste = []
    #chaque élément du fichier est stocké dans une case d'un tableau, 
    #en utilisant rstrip('\n') pour séparer les différentes lignes
    
    for ligne in fichier:
        liste.append(ligne.rstrip('\n'))
    fichier.close()
    
    liste2 = []
    #chaque élement, initialement séparé par une virgule dans le fichier,
    #est stocké dans un autre tableau, en utlisant split(';')
    #cela nous permet de créer une liste de listes
    for element in liste:
        liste2.append(element.split(';'))
    
    liste3 = liste2.copy()
    #fonction qui permet de convertir les nombres du tableau en float,
    #ce qui correspond aux quatre premiers éléments de chaque liste de la liste
    for i in range(0, len(liste2)):
        for j in range(0,len(liste2[i])):
            if j <= 3:
                liste3[i][j] = float(liste2[i][j])
            else:
                liste3[i][j] = liste2[i][j]
    
    return liste3


#Fonction qui va calculer une distance euclidienne
#Prend en parametre les 4 variables de la donnée et les 4 variables d'une 
#donnée d'apprentissage
#retourne la distance euclidienne
def DistanceEuclidienne(SpTest, SwTest, LpTest, LwTest, Sp, Sw, Lp, Lw):
    return ((SpTest-Sp)**2 + (SwTest-Sw)**2 + (LpTest-Lp)**2 + 
                (LwTest-Lw)**2)**0.5


#Fonction qui va calculer la liste des distances (non ordonnée)
#Prend en parametre la liste qui stock les données, et la donnée test
#retourne une liste qui associe chaque distance euclidienne (de chaque ligne) à 
#sa classe
def ListeDistance(ListeDonnee, SpTest, SwTest, LpTest, LwTest):
    distance = 0
    listetemp = []
    listeDistance = []
    
   #pour chaque liste de ListeFinale, on calcule la distance entre les données
   #d'apprentissage de la liste et les données test passées en paramètre
   #initialisation d'une liste de listes contenant la distance de chaque 
   #donnée d'apprentissage et le type d'iris associé
    for i in range(0, len(ListeDonnee)):
        distance = DistanceEuclidienne(SpTest, SwTest, LpTest, LwTest, 
                                       ListeDonnee[i][0], ListeDonnee[i][1], 
                                       ListeDonnee[i][2], ListeDonnee[i][3])
        listetemp = [distance, ListeDonnee[i][4]]
        listeDistance.append(listetemp)
    return listeDistance

#Fonction qui va trier la liste des distances par ordre croissant
#Prend en parametre la liste des distance
#retourne la liste des distances triée
def TriListeDistance(ListeDistance):
    #fonction qui parcourt chaque liste de la listeDistance
    #et vérifie si une distance est plus grande que son voisin supérieur
    #en ne prenant en compte que la distance euclidienne de chaque liste et non
    #le type d'iris de la liste
    for i in range(len(ListeDistance)):
        for j in range(0, len(ListeDistance)-i-1):
            if ListeDistance[j+1][0] < ListeDistance[j][0]:
                 ListeDistance[j], ListeDistance[j+1] = ListeDistance[j+1], ListeDistance[j]
    return ListeDistance

#Fonction qui prendre les top k classe trouvées
#Prend en parametre la liste trier et K
#retourne une liste de classe de taille k
def TopKTrouve(ListeTrier, k):
    listetop =[]
    for i in range(0, k):
        listetop.append(ListeTrier[i][1])
    return listetop


#Fonction qui va retourner la classe la plus fréquentée
#Prend en parametre la liste des top k trouvées
#retourne la classe la plus fréquentée
def ClasseFrequente(ListeTop):
    #initialisation de compteur pour chaque type d'iris
    NbA = 0
    NbB = 0
    NbC = 0
    NbD = 0
    NbE = 0
    NbF = 0
    NbG = 0
    NbH = 0
    NbI = 0
    NbJ = 0
    
    #en parcourant la liste Top k, on incrémente chaque compteur lorsque le
    #type concerné est rencontré
    for element in ListeTop:
        if element == "A":
            NbA += 1
        if element == "B":
            NbB += 1
        if element == "C":
            NbC += 1
        if element == "D":
            NbD += 1
        if element == "E":
            NbE += 1
        if element == "F":
            NbF += 1
        if element == "G":
            NbG += 1
        if element == "H":
            NbH += 1
        if element == "I":
            NbI += 1
        if element == "J":
            NbJ += 1
    classe = ""
    
    #détermine le nombre du type d'iris le plus représenté dans le top k,
    #en utilisant un max() sur la liste des compteurs
    listeNb = [NbA, NbB, NbC, NbD, NbE, NbF, NbG, NbH, NbI, NbJ]
    maximum = max(listeNb)
    
    #associe la nature de la donnée test, en vérifiant avec quel compteur est 
    #égal le compteur maximum
    if maximum == NbA:
        classe = "A"
    if maximum == NbB:
        classe = "B"
    if maximum == NbC:
        classe = "C"
    if maximum == NbD:
        classe = "D"
    if maximum == NbE:
        classe = "E"
    if maximum == NbF:
        classe = "F"
    if maximum == NbG:
        classe = "G"
    if maximum == NbH:
        classe = "H"
    if maximum == NbI:
        classe = "I"
    if maximum == NbJ:
        classe = "J"
    return classe


#Fonction qui va tester toutes les fonctions précédente, et surtout faire 
#fonctionner notre algorithme
#Prend en paramètre k
def ApprentissageSupervisé(k):
    ListeDonnee = LireFichier()
    print("Liste donnée :\n")
    print(ListeDonnee)
    Listedistance = ListeDistance(ListeDonnee, 5.9, 3.0, 5.0, 1.8)
    print("liste distance :\n")
    print(Listedistance)
    ListeTrier = TriListeDistance(Listedistance)
    print("Listre Trié :\n")
    print(ListeTrier)
    ListeTop = TopKTrouve(ListeTrier, k)
    print("Liste top :\n")
    print(ListeTop)
    classe = ClasseFrequente(ListeTop)
    print(classe)
    

#Fonction qui va calculer le pourcentage de precision de notre algorithme en 
#fonction de k
#Prend en paramètre k
#Retourne le pourcentage
def Pourcentage(k):
    #d'abord on lit le fichier
    ListeDonnee = LireFichier()
    #on initialise les variables
    index = 0
    CompteurBonResultat = 0
    #on va parcourir chaque element de la liste de donnée
    while (index < len(ListeDonnee)):
        #on créer une variable temporaire que l'on va modifier a chaque itération
        #mais au debut on l'initialise toujours a la liste de donnée
        ListeTemp = ListeDonnee.copy()
        #on recupere la donnée que l'on veut tester, c'est a dire savoir si 
        #avec notre algo, on obtient le bon resultat en prenant cette donnée
        #test
        DonneeTest = ListeDonnee[index]
        #ensuite on la supprime de notre liste temp, pour ne pas la prendre en
        #compte dans nos calculs
        del ListeTemp[index]
        #on effectue l'algo avec la donnée test et la liste temp
        Listedistance = ListeDistance(ListeTemp, DonneeTest[0], DonneeTest[1], 
                                      DonneeTest[2], DonneeTest[3])
        ListeTrier = TriListeDistance(Listedistance)
        ListeTop = TopKTrouve(ListeTrier, k)
        #on recupère le resultat
        classe = ClasseFrequente(ListeTop)
        #si le resultat est bon, c'est a dire si la classe récupérer est bien 
        #égal a la classe de la donnée test
        if classe == DonneeTest[4]:
            #on rajoute 1 au compteur
            CompteurBonResultat += 1
        #on ajoute 1 a l'index pour tester l'element suivant
        index += 1
    #on calcul le pourcentage
    pourcentage = (CompteurBonResultat * 100) / index
    return pourcentage

#Fonction qui va determiner quel est le meilleurs k a prendre pour avoir le 
#meilleurs pourcentage de reussite 
#Retourne le meilleurs k      
def MeilleursK():
    #on initialise k a 1
    k = 1
    #on initialise nos variables
    Kfinal = 0
    PourcentageKfinal = 0
    #on va tester les k de 1 jusqu'a 30
    while (k < 30):
        #si le pourcentage de k est supérieur au pourcentage stocké
        if (PourcentageKfinal < Pourcentage(k)):
            #on stock le nouveau pourcentage et le k qui lui correspond
            PourcentageKfinal = Pourcentage(k)
            Kfinal = k
        print("k = ", k, " avec un pourcentage = ", Pourcentage(k))
        #on ajoute 1 a k pour tester le k suivant
        k += 1
    print()
    return Kfinal


#Charger les données du fichier et les stocker dans un tableau
def LireFichierfinalTest():
    #ouverture fichier
    fichier = open(r"finalTest.csv", "r")
    liste = []
    #chaque élément du fichier est stocké dans une case d'un tableau, 
    #en utilisant rstrip('\n') pour séparer les différentes lignes
    
    for ligne in fichier:
        liste.append(ligne.rstrip('\n'))
    fichier.close()
    
    liste2 = []
    #chaque élement, initialement séparé par une virgule dans le fichier,
    #est stocké dans un autre tableau, en utlisant split(';')
    #cela nous permet de créer une liste de listes
    for element in liste:
        liste2.append(element.split(';'))
    
    liste3 = liste2.copy()
    #fonction qui permet de convertir les nombres du tableau en float,
    for i in range(0, len(liste2)):
        for j in range(0,len(liste2[i])):
            liste3[i][j] = float(liste2[i][j])
    return liste3


#Fonction qui va créer la liste de lettre a retourner a partir du fichier 
#finalTest
#Prend en parametre k
#Retourne la liste de lettre à afficher dans le fichier avec les 2 noms des 
#élèves;
def PredictionFinalTest(k):
    #d'abord on lit le fichier data
    ListeDonnee = LireFichier()
    #ensuite on lit le fichier finalTest
    ListeFinalTest = LireFichierfinalTest()
    #on initialise les variables
    index = 0
    label = ""
    listeLabel = []
    #on va parcourir chaque element de la liste de donnée
    while (index < len(ListeFinalTest)):
        #on recupere la donnée que l'on veut tester, c'est a dire savoir si 
        #avec notre algo, quelle lettre on obtient pour l'élement 
        #ListeFinalTest[index]
        DonneeTest = ListeFinalTest[index]
        #on effectue l'algo avec la donnée test et la liste de donnée
        Listedistance = ListeDistance(ListeDonnee, DonneeTest[0], DonneeTest[1], 
                                      DonneeTest[2], DonneeTest[3])
        ListeTrier = TriListeDistance(Listedistance)
        ListeTop = TopKTrouve(ListeTrier, k)
        #on recupère le resultat
        label = ClasseFrequente(ListeTop)
        #On incrémente notre liste de label final avec le label obtenue 
        listeLabel.append(label)
        #on ajoute 1 a l'index pour tester l'element suivant
        print(index)
        index += 1
    return listeLabel


#Permet de créer le fichier final
#Prend en paramètre la liste de label
def CreationFichierFinal(listeLabel):
    #ouverture fichier
    fichier = open("Mutez_Nakhlé.txt", "w")
    #Pour chaque lettre de liste, on écrit une ligne dans le tableau
    for label in listeLabel:
        fichier.write(label + "\n")
    fichier.close()
    print("Fichier créé avec succes")
    
    
def TestFichier():
    allLabels = ['A','B','C','D','E','F','G','H','I','J']
    nbLines = 2000
    fd = open("Mutez_Nakhlé.txt",'r')
    lines = fd.readlines()
    
    count=0
    for label in lines:
        if label.strip() in allLabels:
            count+=1
        else:
            if count<nbLines:
                print("Wrong label line:"+str(count+1))
                break
    if count<nbLines:
        print("Labels Check : fail!")
    else:
        print("Labels Check : Successfull!")



if __name__=='__main__' :
    '''------------------- Permet de tester les fonctions ------------------'''
    #ApprentissageSupervisé(4)
    
    '''---------------------------------------------------------------------'''
    
    '''----------------- Permet de trouver le meilleurs k ------------------'''
    '''#On initialise un k 
    k = 3
    #Ici on test le pourcentage par rapport au k
    print("Le pourcentage de bonne réponse pour k =", k, " est :", Pourcentage(k))
    print()
    
    
    ListeDonnee = LireFichier()
    print(len(ListeDonnee))
    
    #On trouve ici le meilleurs k
    print("Le meilleurs k est : ", MeilleursK())
    print()
    #On trouve que le meilleurs k est :
    #k =  4  avec un pourcentage =  85.83333333333333'''
    
    '''---------------------------------------------------------------------'''
    
    '''--------------- Permet de créer notre fichier final -----------------'''
    
    listeLabel = PredictionFinalTest(4)
    CreationFichierFinal(listeLabel)
    
    '''---------------------------------------------------------------------'''
    
    '''--------------- Permet de tester notre fichier final -----------------'''
    
    TestFichier()
    #Retourne bein successfull!
    
    '''---------------------------------------------------------------------'''
    
    
    
    