# import numpy as np
import interpreter
import domain
from KMC import KMC2D
import numpy as np

# Definition du substrat
x = 30
y = 30
grid = domain.create_grid(x,y)     # [hauteur, largeur]

kT = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]

deltamu = np.linspace(-1.0, 1.0, 11)

nb_pas_temps = 500
gif = False



grid, deltatemps_reel, parametres = KMC2D(grid, kT[0], deltamu[0], nb_pas_temps,gamma=True, rugosity=True)

# print(parametres[0])


# interpreter.plot_growth_2d(grid)


import matplotlib.pyplot as plt
plt.figure()
plt.plot(np.linspace(0,nb_pas_temps,nb_pas_temps), parametres[0])
plt.show()
# print(grid)
# surface = domain.find_surface(grid)

# print(surface)