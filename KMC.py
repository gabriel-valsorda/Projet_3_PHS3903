import numpy as np
import scipy as sp
import random as rand


def KMC(config, deltaE, kT, deltamu):
    N=5
    deltamu=5
    T=295
    kb=1.380649e-23
    kbT=kb*T

    # Étape 1 : Générer la liste des 2N événements possibles
    typeEvnt=[0,1]
    listeEvnt=[]

    for site in range(N):
        for adOuDes in typeEvnt:
            listeEvnt.append((site,adOuDes))

    # Étape 2 : Calcul des w de chaque événement
    deltamu=-0.5
    kT=0.6
    deltaE=1

    w_liste=[]
    for i in listeEvnt:
        if i[1]==0:
            w=np.exp(deltamu/kT)
            w_liste.append(w)
        if i[1]==1:
            w=np.exp(-deltaE/kT)
            w_liste.append(w)
    W=np.sum(w_liste)

    # Étape 3 : Normalisation
    w_normalisee=[w/W for w in w_liste]

    # Étape 4 : On génère un nombre aléatoire en 0 et 1 et on choisit le premier événement qui a une proba cumulée supérieure à r.
    nombre_r=np.random.rand()
    somme=0
    compteur=0
    proba_cumulée=[]
    for i in w_normalisee:
        somme+=i
        proba_cumulée.append(somme)
        if somme>nombre_r:
            break
        compteur+=1
    print(f"L'événement est donc {listeEvnt[compteur]}")

    # Étape 5 : Nouvelle configuration

    # Étape 6  : Assigner un temps
    nombre_r_temps=np.random.rand()
    deltatemps_reel=-1/(W*np.log(nombre_r_temps))
    
    return config, deltatemps_reel


KMC(config, deltaE=1, kT=0.6, deltamu=-0.5)