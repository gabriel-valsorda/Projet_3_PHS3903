import numpy as np

import MonteCarlo as mc

# Definition du substrat
N = 5 # Dimension
L = N # Largeur
H = 2*L # Hauteur


cristal = np.full([H,L],None)     # [hauteur, largeur]

# Initialisation de la première ranger (Na -> 1, Cl -> 0)
cristal[0, ::2] = 1
cristal[0, 1::2] = 0

'''Est ce qu'on fait la croissance épitaxial à partir du bas ou du haut 
(est ce qu'on considère l'indice 0 comme le "sol" ou c'est l'indice -1)?'''

print(cristal)

new = mc.method(cristal)
print(new)

