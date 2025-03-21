import numpy as np

import domain

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


print(grid)
iteration = 5
domain.plot_3D_growth(grid)

# saved_grid = np.zeros([iteration,H,L])

# for i in range(iteration):
#     saved_grid[i] = grid
#     grid = domain.kinetic_monte_carlo_step(grid)


# print(saved_grid)

# domain.plot_growth(grid)





