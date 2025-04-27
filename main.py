import domain
from KMC import KMC2D2 as KMC2D
import matplotlib.pyplot as plt
import numpy as np
import time

# Definition du substrat
x = 50
y = 50
grid = domain.create_grid(x,y)     # [hauteur, largeur]

liste_kT = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
liste_deltamu = np.linspace(-1.0, 1.0, 11)

nb_pas_temps = 1
gif = False

kT = liste_kT[3]
deltamu = liste_deltamu[5]

nb_iterations = 2






