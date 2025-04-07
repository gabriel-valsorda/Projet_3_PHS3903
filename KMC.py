import numpy as np
import scipy as sp
import random as rand
import os
from domain import find_surface
import matplotlib.pyplot as plt
from interpreter import save_graph
from interpreter import creer_gif

import numpy as np

def find_surface(grid):
    """
    Identify the first None site below each column's occupied site.
    Returns an array of surface site indices.
    """
    Nx, Ny = grid.shape
    surface_sites = []  # Store the row index of surface sites
    
    for i in range(Nx):
        for j in range(Ny):
            if grid[i, j] is None:
                surface_sites.append([i,j])
                break  # Stop at the first None in the column
    
    return surface_sites


def KMC_2D(grid, P_a=0.8, P_e=0.1,iteration=5):
    """
    Perform one kinetic Monte Carlo step on the surface layer.
    
    Parameters:
    - grid: NxN numpy array where None represents empty sites.
    - P_a: Probability of adsorption (0 to 1).
    - P_e: Probability of evaporation (0 to 1).
    
    Returns:
    - Updated grid after one KMC step.
    """
    new_grid = grid.copy()
    for i in range(iteration):
        surface_sites = find_surface(new_grid)

        site_choisit = surface_sites[np.random.randint(0, len(surface_sites))]

        i, j = site_choisit
        if new_grid[i, j-1] == 0:
            new_grid[i, j] = 1
        elif new_grid[i, j-1] == 1:
            new_grid[i, j] = 0

    return new_grid

x = 5
y = 10

grid = np.full([x,y],None)     # [hauteur, largeur]

# Initialisation de la première ranger (Na -> 1, Cl -> 0)
grid[::2, 0] = 1
grid[1::2, 0] = 0

grid = KMC_2D(grid, iteration = 10)




deltaE=[1 for i in range(len(grid))]

def KMC2D_Laurent(config, deltaE, kT, deltamu, nb_pas_temps):
    os.makedirs("frames", exist_ok=True)
    N=len(config)
    T=295
    kb=1.380649e-23
    kbT=kb*T
    positions_surface=find_surface(config)

    for iteration in range(nb_pas_temps):
        # Étape 1 : Générer la liste des 2N événements possibles
        #(site,0 = désorption ou 1 = adsorption)
        typeEvnt=[0,1]
        listeEvnt=[]

        for site in range(N):
            for adOuDes in typeEvnt:
                listeEvnt.append((site,adOuDes))

        # Étape 2 : Calcul des w de chaque événement
        deltamu=-0.5
        kT=0.6


        w_liste=[]
        for i in listeEvnt:
            if i[1]==0:
                w=np.exp(deltamu/kT)
                w_liste.append(w)
            if i[1]==1:
                w=np.exp(-deltaE[i[0]]/kT)
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
        evnt=listeEvnt[compteur]
        if evnt[1]==1:
            print(f"L'événement est une adsorption au site {evnt[0]}")
        if evnt[1]==0:
            print(f"L'événement est une désorption au site {evnt[0]}")
        

        # Étape 5 : Nouvelle configuration
        site_changement=evnt[0]

        # Cas désorption
        if evnt[1]==0:
            if config[site_changement][positions_surface[site_changement][1]-1]==None:
                continue
            config[site_changement][positions_surface[site_changement][1]-1]=None
            positions_surface[site_changement][1]-=1
        
        # Cas adsorption
        if evnt[1]==1:
            # Si somme de position de surface et site changement et paire, alors le prochain est un 0
            if (positions_surface[site_changement][1]+site_changement)%2==0:
                config[site_changement][positions_surface[site_changement][1]]=1
                positions_surface[site_changement][1]+=1
            else:
                config[site_changement][positions_surface[site_changement][1]]=0
                positions_surface[site_changement][1]+=1



        # Étape 6  : Assigner un temps
        nombre_r_temps=np.random.rand()
        deltatemps_reel=-1/(W*np.log(nombre_r_temps))

        print(config)
        save_graph(config,iteration)
        
        
    return config, positions_surface, deltatemps_reel


KMC2D_Laurent(grid, deltaE, kT=0.6, deltamu=-0.5,nb_pas_temps=15)
creer_gif("frames")
