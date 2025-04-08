import numpy as np
from scipy.special import pi, exp
import pickle

def get_potential(distances, nom_dict) : #positions est du format [(nx,ny,nz),...] (n>0) et dict_pot est le nom d'un fichier pickle
    with open(f'{nom_dict}.pkl') as f:
        dict_pot = pickle.load(f)
    f.close()
    pot_total = 0
    for d in distances :
        pot_for_d = dict_pot.get(sorted(d))
        pot_total += pot_for_d if pot_for_d is not None else 0
    return pot_total