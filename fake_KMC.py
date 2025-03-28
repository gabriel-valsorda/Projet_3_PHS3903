import numpy as np
from domain import find_surface
from domain_3D import find_surface as find_surface_3D


def kinetic_monte_carlo_step(grid, P_a=0.8, P_e=0.1):
    """
    Perform one kinetic Monte Carlo step on the surface layer.
    
    Parameters:
    - grid: NxN numpy array where None represents empty sites.
    - P_a: Probability of adsorption (0 to 1).
    - P_e: Probability of evaporation (0 to 1).
    
    Returns:
    - Updated grid after one KMC step.
    """
    surface_sites = find_surface(grid)
    new_grid = grid.copy()
    
    for el in surface_sites:
        i, j = el
        if i == -1:  # Column is fully occupied, skip
            continue
        
        above = new_grid[i - 1, j] if i > 0 else None  # Atom above
        
        # Adsorption step (only if there is an atom above)
        if above is not None and np.random.rand() < P_a:
            if above == 1:
                new_grid[i,j] = 0
            else:
                new_grid[i, j] = 1  # Copy the type (1 or 0)
        
        # Evaporation step (only affects surface sites)
        if i > 0 and new_grid[i - 1, j] in [0, 1] and np.random.rand() < P_e:
            new_grid[i - 1, j] = None  # Evaporate the atom
        
    return new_grid

def KMC_3D(grid, P_a=0.8, P_e=0.1,iteration=5):
    """
    Perform one kinetic Monte Carlo step on the surface layer.
    
    Parameters:
    - grid: NxN numpy array where None represents empty sites.
    - P_a: Probability of adsorption (0 to 1).
    - P_e: Probability of evaporation (0 to 1).
    
    Returns:
    - Updated grid after one KMC step.
    """
    new_grid = grid.copy()
    # Nx, Ny, Nz = grid.shape
    for i in range(iteration):
        surface_sites = find_surface_3D(new_grid)

        site_choisit = surface_sites[np.random.randint(0, len(surface_sites))]

        i, j, k = site_choisit
        if new_grid[i, j, k-1] == 0:
            new_grid[i, j, k] = 1
        elif new_grid[i, j, k-1] == 1:
            new_grid[i, j, k] = 0

    return new_grid
