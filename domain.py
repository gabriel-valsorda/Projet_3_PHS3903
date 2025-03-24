import numpy as np

def find_surface(grid):
    """
    Identify the first None site below each column's occupied site.
    Returns an array of surface site indices.
    """
    Nx, Ny = grid.shape
    surface_sites = []  # Store the row index of surface sites
    
    for j in range(Ny):  # Iterate over columns
        for i in range(Nx):
            if grid[i, j] is None:
                surface_sites.append([i,j])
                break  # Stop at the first None in the column
    
    return surface_sites

# def kinetic_monte_carlo_step(grid, P_a=0.8, P_e=0.1):
#     """
#     Perform one kinetic Monte Carlo step on the surface layer.
    
#     Parameters:
#     - grid: NxN numpy array where None represents empty sites.
#     - P_a: Probability of adsorption (0 to 1).
#     - P_e: Probability of evaporation (0 to 1).
    
#     Returns:
#     - Updated grid after one KMC step.
#     """
#     surface_sites = find_surface(grid)
#     new_grid = grid.copy()
    
#     for el in surface_sites:
#         i, j = el
#         if i == -1:  # Column is fully occupied, skip
#             continue
        
#         above = new_grid[i - 1, j] if i > 0 else None  # Atom above
        
#         # Adsorption step (only if there is an atom above)
#         if above is not None and np.random.rand() < P_a:
#             if above == 1:
#                 new_grid[i,j] = 0
#             else:
#                 new_grid[i, j] = 1  # Copy the type (1 or 0)
        
#         # Evaporation step (only affects surface sites)
#         if i > 0 and new_grid[i - 1, j] in [0, 1] and np.random.rand() < P_e:
#             new_grid[i - 1, j] = None  # Evaporate the atom
        
#     return new_grid

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def interatomic_distance(grid,periodicity=0):
    '''
    Calcul des distances des ions de la configuration pour chaque site vacant de surface
    '''
    surface = np.array(find_surface(grid))
    Na_ions, Cl_ions = find_ions(grid)
    Na_ions, Cl_ions = np.array(Na_ions), np.array(Cl_ions)

    for vacant in surface:
        Na_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Na_ions]
        Cl_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Cl_ions]

    
    if periodicity != 0:


        for vacant in surface:
            Na_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Na_ions]
            Cl_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Cl_ions]