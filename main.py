import numpy as np
import interpreter
import domain

# Definition du substrat
N = 5 # Dimension
L = N # Largeur
H = 2*L # Hauteur


grid = np.full([H,L],None)     # [hauteur, largeur]

# Initialisation de la première ranger (Na -> 1, Cl -> 0)
grid[0, ::2] = 1
grid[0, 1::2] = 0


iteration = 5
saved_grid = np.zeros([iteration,H,L])

for i in range(iteration):
    saved_grid[i] = grid
    grid = domain.kinetic_monte_carlo_step(grid)



# print(saved_grid[-1])
# print(domain.find_surface(grid))


# interpreter.plot_growth(grid)


# print(grid)
a,b = domain.interatomic_distance(grid,2)
print(a)

