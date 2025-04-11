import numpy as np
import interpreter
import domain
from KMC import KMC2D_Laurent

# Definition du substrat
x = 10
y = 10

grid = domain.create_grid(x,y,5)     # [hauteur, largeur]

# KMC2D_Laurent(grid, deltaE=1, kT=0.6, deltamu=-0.5,pas_temps=2)
interpreter.plot_growth_2d(grid)
# domain.interatomic_distance_2d(grid,0)

ion = domain.find_ions(grid)
print(grid)
print(ion[1])
# domain.save_grid(grid)