import numpy as np
import domain_3D
import fake_KMC
import interpreter
# from KMC import KMC2D_Laurent

# Definition du substrat
x = 5
y = 5
z = 10


grid = np.full([x,y,z],None)     # [hauteur, largeur]
# Initialisation de la première ranger (Na -> 1, Cl -> 0)

grid[::2, ::2, 0] = 1
grid[1::2, 1::2, 0] = 1

grid[::2, 1::2, 0] = 0
grid[1::2,::2,0] = 0


# print(grid)
iteration = 5

# grid = fake_KMC.KMC_3D(grid,iteration=50)
# interpreter.plot_3D_growth(grid)


# grid, deltatemps_reel = KMC2D_Laurent(grid, deltaE=1, kT=0.6, deltamu=-0.5,pas_temps=2)
print(grid)


grid






