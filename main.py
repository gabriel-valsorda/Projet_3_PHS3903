import numpy as np
import interpreter
import domain
import fake_KMC

# Definition du substrat

x = 5
y = 10

grid = np.full([x,y],None)     # [hauteur, largeur]

# Initialisation de la première ranger (Na -> 1, Cl -> 0)
grid[::2, 0] = 1
grid[1::2, 0] = 0


iteration = 5
saved_grid = np.zeros([iteration,x,y])

grid = fake_KMC.KMC_2D(grid,iteration=10)
print(grid)

# print(saved_grid[-1])
# print(domain.find_surface(grid))


# interpreter.plot_growth(grid)


# print(grid)
# a,b = domain.interatomic_distance(grid,2)
# print(a)

