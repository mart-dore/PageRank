#Projet de big data
#Auteurs : Augustin MAILLE, Martin DORE

import scipy.linalg as nla

import numpy as np
import pandas as pd


#-----------QUESTION 1-------------

def sumColumn(m, column):
    total = 0
    for row in range(m.shape[0]):
        total += m[row][column]
    return total

def normalise_column(m):
    matrice = m.copy()
    for j in range (matrice.shape[1]):
        som = sumColumn(matrice, j)
        if som != 0:
            for i in range(matrice.shape[0]):
                elem = matrice[i,j]
                matrice[i,j] = elem / som
    return matrice

#page rank algorithm for a given adjency matric A
def page_rank(A,beta):
    At = np.transpose(A)
    P = normalise_column(At) #stochastic matrix
    n = P.shape[0]
    q = np.repeat(1/n, n)
    q_next = np.zeros(n)
    betaP = beta*P
    it = 0
    d = nla.norm(q_next - q)
    #methode de la puissance
    while (d > 0.0001):
        it += 1


        q_next = np.dot(betaP,q)
        s = sum(q)
        q_next += np.transpose(np.repeat(((1-beta)/n)*s, n))
        q_next = q_next/sum(q_next)
        d = nla.norm(q_next - q)
        q = q_next
    return q_next,it



#------------QUESTION 2-------------


Sommets = [] #Sommets de l'arborescence des pages (chaque sommet
#est une page différente)

#--remplissage des sommets--
#Trouver toutes les pages disponibles



#--création de la matrice d'adjacence--

def contains_chev(list):
    try :
        list.index('<')
        return True
    except:
        return False
#f = open("test.csv", "r")
#Add paths_unfinished.csv to paths_finished.csv

finished = open("paths_finished.csv", "r")
unfinished = open("paths_unfinished.csv","r")
all_paths = open("all_paths.csv","w")
for l in finished.readlines():
    all_paths.write(l)
for li in unfinished.readlines():
    all_paths.write(li)
finished.close()
unfinished.close()
all_paths.close()


f = open("all_paths.csv", "r")
for line in f.readlines():
    chemin = line.split(";")
    if (chemin[len(chemin) - 1] == "restart" or "timeout"):
        del chemin[len(chemin)- 2:len(chemin)] #On enleve le dernier et la target si c'est restart ou timeout
    #preprocess : on eleve les '<' avec le nombre de pages correspondantes
    while (contains_chev(chemin) == True):
         i = chemin.index('<')
         del chemin[i - 1 : i + 1]
    for page in chemin:
        page = page.replace('\n','')#page de fin de ligne
        try:
            Sommets.index(page) #on regarde si la page est déjà connue
        except:
            Sommets.append(page) #sinon on l'ajoute
    #remplissage de la matrice d'Adjacence
nbSommets = len(Sommets)
Graphe = np.zeros((nbSommets, nbSommets))
#print(Sommets)
f.close()
#f = open("test.csv", "r")

f = open("all_paths.csv", "r")
for line in f.readlines():
    chemin = line.split(";")
    if (chemin[len(chemin)-1] == "restart" or "timeout"):
        del chemin[len(chemin)- 2:len(chemin)] #On enleve le dernier et la target si c'est restart ou timeout
    #preprocess : on eleve les '<' avec le nombre de pages correspondantes
    while (contains_chev(chemin) == True):
         i = chemin.index('<')
         del chemin[i - 1 : i + 1]
    for n in range(len(chemin)-1):
        chemin[n] = chemin[n].replace('\n','')
        chemin[n + 1] = chemin[n + 1].replace('\n','')
        index_of_page = Sommets.index(chemin[n])
        index_of_next = Sommets.index(chemin[n + 1])
        Graphe[index_of_page][index_of_next] += 1

f.close()

#Page la plus visitee
#print(PG)
#10 pages les plus visitées avec leur scores
def dix_plus_vu():
    dict = two_lists_to_dico(Sommets,PG)
    dict_sorted = sorted(dict.items(),key = lambda x:x[1],reverse = True)
    #out = dict(list(dict_sorted.items())[0:10])
    print(" Les dix premieres pages\n")
    for i in range(10):
        print(dict_sorted[i])

def two_lists_to_dico(keys , value):
    res = dict(zip(keys,value))
    return res

#--------------- page rank perso -------------
def personalized_page_rank(A,beta,nodes_indexes):#nodes_indexes est la liste des indexs des noeuds à personalisés
    At = np.transpose(A)
    P = normalise_column(At) #stochastic matrix
    n = P.shape[0]
    v = np.zeros(n)
    for i in nodes_indexes:
        v[i] = 1/len(nodes_indexes)#On initialize le vecteur v en mettant zero
        #partout sauf aux noeuds personnalisés où l'on met 1/(nombre de noeud perso)
    q = np.repeat(1/n, n)
    q_next = np.zeros(n)
    betaP = beta*P
    it = 0
    d = nla.norm(q_next - q)
    #methode de la puissance
    while (d > 0.0001):
        it += 1


        q_next = np.dot(betaP,q)
        s = sum(q)
        q_next += np.transpose(np.repeat(((1-beta))*s, n)*v)
        q_next = q_next/sum(q_next)
        d = nla.norm(q_next - q)
        q = q_next
    return q_next,it

#--------Q6 Choisir un ensemble de noeud à perso et comparer avec pr
# teste différents noeuds et compare.


#------- Code pour transformer ce fichier en veritable programme


def get_index_w_name(names):
    list_indexes = []
    for name in names:
        list_indexes.append(Sommets.index(name))
    return list_indexes

q1 = input("Que voulez vous faire ?\n Répondre par le numero de la réponse.\n1. Calcul de Page Rank\n2. Calcul de page rank personalisé\n")
if (int(q1) == 1):
    B = float(input("Veuillez choisir une valeur de beta (Valeur entre 0 et 1)\n"))
    print("Calcul en cour\n")
    PG,n_iter = page_rank(Graphe, B)
    print("Nombre d'itération : "+str(n_iter)+"\n")
    dix_plus_vu()
if (int(q1) == 2):
    noms = input("Donnez le nom des noeuds à personalisé, il doivent être exact et séparés par un espace\n")
    list_of_names = noms.split(" ")
    B = float(input("Veuillez choisir une valeur de beta (Valeur entre 0 et 1)\n"))
    print("Calcul en cour\n")
    PG, n_iter = personalized_page_rank(Graphe,B,get_index_w_name(list_of_names))
    print("Nombre d'itération : "+str(n_iter)+"\n")
    dix_plus_vu()
