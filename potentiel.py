from domain import find_ions
import numpy as np
import time


import pickle
def get_potential(distances, nom_dict='energie_directe.pkl') : #positions est du format [(nx,ny,nz),...] (n>0) et dict_pot est le nom d'un fichier pickle
    with open(f'{nom_dict}.pkl') as f:
        dict_pot = pickle.load(f)
    f.close()
    pot_total = 0
    for d in distances :
        pot_for_d = dict_pot.get(sorted(d))
        pot_total += pot_for_d if pot_for_d is not None else 0
    return pot_total


def potentielEvnt(grille, Evnt, positions_surface):
    start_time = time.time()
    #caractéristiques de la grille et de l'événement
    largeur = len(grille)
    N = int(1000/largeur)
    nx = Evnt[0]
    ny = positions_surface[nx][1]-1
    signe = (-1)**(nx+ny) 
    a = 5.64e-10  # Lattice constant in meters (example value, adjust as needed)
    facteur = -(signe)
    posNa, posCL = find_ions(grille)

    # On calcule Delta E dans le réseau direct pour les atomes dans un rayon plus petit que 100 
    potentiel_total = []
    compteur = 0

    #Calcul pour les Na+
    for pos in posNa:
        # if pos == [0,10] : print('Na!')
        for l in range(-N,N):
            compteur += 1
            x = pos[0]+l*largeur
            y = pos[1]
            r = np.sqrt((x-nx)**2 + (y-ny)**2)
            if r == 0 or r > 200: continue
            potentiel_Na = 1/r
            potentiel_total.append(potentiel_Na)
    #Calcul pour les Cl-
    for pos in posCL:
        for l in range(-N,N):
            compteur += 1
            x = pos[0]+l*largeur
            y = pos[1]
            r = np.sqrt((x-nx)**2 + (y-ny)**2)
            if r == 0 or r > 200: continue
            potentiel_Cl = -1/r
            potentiel_total.append(potentiel_Cl)

    
    # print(f"Temps de calcul pour le potentiel total: {elapsed_time:.4f} secondes")
    return sum(sorted(potentiel_total, key=lambda x: abs(x)))*facteur #permet de minimiser l'erreur numérique




def temps_potentiel(x,y,hauteur):
    import domain
    start_time = time.time()
    grid = domain.create_grid(x,y,hauteur)
    positions_surface = domain.find_surface(grid)
    Evnt = (0,[25,hauteur])
    potentielEvnt(grid, Evnt, positions_surface)


    #temps de calcul pour le potentiel total
    end_time = time.time()
    elapsed_time = end_time - start_time 
    # print(f"Temps de calcul pour le potentiel total: {elapsed_time/hauteur:.4f} secondes")
    return elapsed_time

def calcul_de_temps(x,y,iteration):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    

    hauteurs = np.arange(1, y-int(y/10), 5)
    mean_times = []
    std_times = []

    for h in hauteurs:
        temps = []
        for i in range(iteration):
            temps.append(temps_potentiel(x,y,h))
        mean_times.append(np.mean(temps))
        std_times.append(np.std(temps))  # Erreur absolue ici (écart-type)

    # Ton modèle linéaire : y = a*x + b
    def linear_model(x, a, b):
        return a * x + b
    popt, pcov = curve_fit(linear_model, hauteurs, mean_times, sigma=std_times, absolute_sigma=True)
    a_fit, b_fit = popt
    a_err, b_err = np.sqrt(np.diag(pcov))  # incertitudes

    # Affichage
    plt.figure()
    plt.title(f'Temps de calcul pour l\'énergie électrostatique \npour un substrats de {x}x{y} ({iteration} itération{"s" if iteration > 1 else ""})', fontsize=16)
    plt.errorbar(hauteurs, mean_times, yerr=std_times, fmt='.', markersize=10, capsize=5, label='Temps moyen ± écart-type')
    plt.plot(hauteurs, linear_model(hauteurs, *popt), 'r-', linewidth=1, label=f'Régression linéaire')
    plt.xlabel('Hauteur (pixels)', fontsize=16)
    plt.ylabel('Temps moyen (s)', fontsize=16)
    plt.grid()
    plt.legend()
    plt.savefig(f'temps_potentiel_{x}x{y}.png', dpi=300)
    plt.show()
    

# calcul_de_temps(100,200, 20)