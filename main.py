# import numpy as np
import interpreter
import domain
from KMC import KMC2D

# Definition du substrat
x = 30
y = 30
grid = domain.create_grid(x,y)     # [hauteur, largeur]

temperature = 300
deltamu = 5e-15
nb_pas_temps = 100
gif = False

deltaE=[1e15 for i in range(len(grid))]

grid, positions_surface, deltatemps_reel, Gamma = KMC2D(grid, deltaE, temperature, deltamu, nb_pas_temps,gif)

interpreter.plot_growth_2d(grid)


print(grid)