# import numpy as np
import interpreter
import domain
from KMC import KMC2D

# Definition du substrat
x = 10
y = 10
grid = domain.create_grid(x,y,5)     # [hauteur, largeur]


# interpreter.plot_growth_2d(grid)  

ion = domain.find_ions(grid)
print(grid)
print(ion[1])
# domain.save_grid(grid)