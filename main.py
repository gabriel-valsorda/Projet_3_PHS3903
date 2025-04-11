# import numpy as np
import interpreter
import domain
from KMC import KMC2D

# Definition du substrat
x = 10
y = 10
grid = domain.create_grid(x,y)     # [hauteur, largeur]

temperature = 300
deltamu = -0.05
nb_pas_temps = 50
gif = False

config, positions_surface, deltatemps_reel = KMC2D(grid, temperature, deltamu, nb_pas_temps,gif)

interpreter.plot_growth_2d(grid)


print(grid)