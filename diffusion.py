import numpy as np
import domain


def probabilite_diffusion(l, l_max, E_l, kT, kT_iso):
    alpha = E_l * (1/kT - 1/kT_iso)

    # Probabilite
    if l_max > 1000000:
        P_l = (2**l - 1) * (1 - np.exp(-alpha)) * (1 - 2*np.exp(-alpha)) / (np.exp(alpha * (l - 1)))
    else:    
        P__l = (2**l - 1) * np.exp(-alpha*(l-1)) * (1-np.exp(-alpha)) * (1-2*np.exp(-alpha)) / (1 - np.exp(-alpha*l_max)*(2**(l_max+1)*(1 - np.exp(-alpha)) - (1 - 2*np.exp(-alpha))))


def Diffusion(surface, Evnt, gamma_0):
    # ajout des cotes
    surface = [surface[-1]] + surface + [surface[0]]
    
    position = Evnt[0]
    norm = np.linalg.norm(position)
    largeur = len(surface)
    N = int(1000/largeur)
    nx = position[0]
    ny = surface[nx][1]-1
    
    
    # Liste des sites disponible pour la diffustion
    if sum(position)%2 == 0: # pair (Na)
        site_dispo = [site for site in surface if sum(site)%2 == 0]
    elif sum(position)%2 != 0: # impair (Cl)
        site_dispo = [site for site in surface if sum(site)%2 != 0]
    '''
    Implementation de la periodicite?
    Pas sur de l'implemente, car la probabilite prend compte des chemins de meme longueur
    Aussi, il faut considerer que puisqu'on repete le cristal periodiquement, une etape de diffusion implique un diffusion periodique...  
    '''

    print(site_dispo)
    distance_possible = []
    for site in site_dispo:
        if site == position:
            continue
        distance = (site[0]-position[0]) + (site[1]-position[1])
        
        if distance not in distance_possible:
            distance_possible.append(distance)
    print(distance_possible)

    new_dist = []
    for n in range(N):
        for dist in distance_possible:
            new_dist.append(dist + n*largeur)

    print(len(new_dist))

    E_l = 1
    kT = 0.5
    kT_iso = 0.6
    prob = []
    alpha = E_l * (1/kT - 1/kT_iso)
    l_max = distance_possible[-1]

    for l in distance_possible:    
        prob.append( (2**l - 1) * np.exp(-alpha*(l-1)) * (1-np.exp(-alpha)) * (1-2*np.exp(-alpha)) / (1 - np.exp(-alpha*l_max)*(2**(l_max+1)*(1 - np.exp(-alpha)) - (1 - 2*np.exp(-alpha)))))
    print(prob)


import interpreter

x = 10
y = 20
grid = domain.create_grid(x, y, 3)
grid[3,3] = 1
grid[2,4] = 1
grid[5,3] = 1
grid[8,4] = 1

grid[2,3] = 0
grid[8,3] = 0


surface = domain.find_surface(grid)

Diffusion(surface, ([0,3],1),0)



interpreter.plot_growth_2d(grid)





