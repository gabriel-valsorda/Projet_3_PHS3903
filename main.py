import numpy as np
import domain
from KMC import KMC2D_Laurent

# Definition du substrat

x = 5
y = 10

grid = np.full([x,y],None)     # [hauteur, largeur]

# Initialisation de la première rangée (Na -> 1, Cl -> 0)
grid[::2, 0] = 1
grid[1::2, 0] = 0


iteration = 5
saved_grid = np.zeros([iteration,x,y])


#KMC2D_Laurent renvoie : config, positions_surface, deltatemps_reel
#Paramètres : config, deltaE, kT, deltamu, nb_pas_temps
grid,positions_surface,deltatemps_reel = KMC2D_Laurent(grid, deltaE=1, kT=0.6, deltamu=-0.5,nb_pas_temps=2)
print(grid)

# print(saved_grid[-1])
# print(domain.find_surface(grid))


# interpreter.plot_growth(grid)


# print(grid)
# a,b = domain.interatomic_distance(grid,2)
# print(a)