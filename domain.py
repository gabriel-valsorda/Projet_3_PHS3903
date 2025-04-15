import numpy as np
import time

def create_grid(x, y, hauteur_initial=None):
    """
    Create a 2D grid of size x by y, initialized with None.
    """
    grid = np.full((x, y), None)
    grid[::2, 0] = 1
    grid[1::2, 0] = 0

    if hauteur_initial is not None:
        for i in range(1,int(hauteur_initial)):
            if i%2 == 0:
                grid[::2, i] = 1
                grid[1::2, i] = 0

            else:
                grid[::2, i] = 0
                grid[1::2, i] = 1

    return grid


def find_surface(grid):
    """
    Identify the first None site below each column's occupied site.
    Returns an array of surface site indices.
    """
    Nx, Ny = grid.shape
    surface_sites = []  # Store the row index of surface sites
    
    for i in range(Nx):
        for j in range(Ny):
            if grid[i, j] is None:
                surface_sites.append([i,j])
                break  # Stop at the first None in the column
    
    return surface_sites


def find_ions(grid):
    '''
    Trouver tous les sites occupes par les ions Na et Cl 
    '''
    Nx, Ny = grid.shape

    Na_ions = []
    Cl_ions = []

    for i in range(Nx):
        for j in range(Ny):
            if grid[i,j] != None:
                if grid[i,j] == 1:
                    Na_ions.append([i,j])
                elif grid[i,j] == 0:
                    Cl_ions.append([i,j])
                else:
                    print("error")
    return Na_ions, Cl_ions



def save_grid(grid, path=''):
    import csv 
    with open(path + 'configuration.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(grid)

def fct_rugosite(position_surface):
    N = len(position_surface)
    position_rugosite=[(position[1]-1) for position in position_surface]
    position_rugosite_carre=[(position[1]-1)**2 for position in position_surface]
    rugosite=np.sqrt(1/N*sum(position_rugosite_carre)-(1/N*sum(position_rugosite))**2)
    return rugosite



def potentiel(grille, Evnt, positions_surface):

    #caractéristiques de la grille et de l'événement
    largeur = len(grille)
    N = int(500/largeur)
    nx = Evnt[0]
    ny = positions_surface[nx][1]-1
    signe = (-1)**(nx+ny) 
    a = 5.64e-10  # Lattice constant in meters (example value, adjust as needed)
    facteur = -(signe)
    posNa, posCL = find_ions(grille)

    # On calcule Delta E dans le réseau direct pour les atomes dans un rayon plus petit que 100 
    potentiel_total = []
    compteur = 0
    start_time = time.time()

    #Calcul pour les Na+
    for pos in posNa:
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

    #temps de calcul pour le potentiel total
    end_time = time.time()
    elapsed_time = end_time - start_time 
    return sum(sorted(potentiel_total, key=lambda x: abs(x)))*facteur #permet de minimiser l'erreur numérique