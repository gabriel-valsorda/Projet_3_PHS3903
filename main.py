# import numpy as np
import interpreter
import domain
from KMC import KMC2D
import numpy as np

# Definition du substrat
x = 50
y = 50
grid = domain.create_grid(x,y)     # [hauteur, largeur]

kT = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]

deltamu = np.linspace(-1.0, 1.0, 11)

nb_pas_temps = 1000
gif = False

kT = kT[2]
deltamu = deltamu[0]

grid, deltatemps_reel, parametres = KMC2D(grid, kT, deltamu, nb_pas_temps,gamma=True, rugosity=True)

# interpreter.gamma_dt(parametres[0], (x,y), kT, deltamu)
# interpreter.rugosite_dt(nb_pas_temps, parametres[1], (x,y), kT[0], deltamu[0])


# interpreter.plot_growth_2d(grid, show=True)