import numpy as np
from scipy.special import pi, exp
import pickle
from domain import find_surface, find_ions
from scipy import constants as sp_const

def get_potential(distances, nom_dict='energie_directe.pkl') : #positions est du format [(nx,ny,nz),...] (n>0) et dict_pot est le nom d'un fichier pickle
    with open(f'{nom_dict}.pkl') as f:
        dict_pot = pickle.load(f)
    f.close()
    pot_total = 0
    for d in distances :
        pot_for_d = dict_pot.get(sorted(d))
        pot_total += pot_for_d if pot_for_d is not None else 0
    return pot_total

a = 5.64e-10  # Lattice constant in meters (example value, adjust as needed)

def potentielEvnt(grille, Evnt, positions_surface):
    nx = Evnt[0]
    ny = positions_surface[nx][1]-1
    signe = (-1)**(nx+ny) 
    posNa, posCL = find_ions(grille)

    # On calcule Delta E dans le réseau direct pour les atomes dans un rayon plus petit que 100*a/2
    potentiel_total = 0
    for l in range(-10,10):
        for pos in posNa:
            r = np.sqrt((pos[0]+l*len(positions_surface)-nx)**2 + (pos[1]+l*len(positions_surface)-ny)**2)*a/2
            if r == 0 or r > 100*a/2 : continue
            potentiel_Na = (1/4*np.pi*sp_const.epsilon_0)*sp_const.e**2*(-1)**(signe)/r
            potentiel_total += potentiel_Na
        for pos in posCL:
            r = np.sqrt((pos[0]+l*len(positions_surface)-nx)**2 + (pos[1]+l*len(positions_surface)-ny)**2)*a/2
            if r == 0 or r > 100*a/2 : continue
            potentiel_Cl = (1/4*np.pi*sp_const.epsilon_0)*sp_const.e**2*(-1)*(-1)**(signe)/r
            potentiel_total += potentiel_Cl

    return potentiel_total