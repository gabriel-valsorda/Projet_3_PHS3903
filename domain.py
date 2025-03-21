import numpy as np

def find_surface(grid):
    """
    Identify the first None site below each column's occupied site.
    Returns an array of surface site indices.
    """
    N = grid.shape[0]
    surface_sites = np.full(grid.shape[1], -1)  # Store the row index of surface sites
    
    for j in range(grid.shape[1]):  # Iterate over columns
        for i in range(N):
            if grid[i, j] is None:
                surface_sites[j] = i
                break  # Stop at the first None in the column
    
    return surface_sites

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
    
    for j, i in enumerate(surface_sites):
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

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
def plot_growth(grid):
    """Visualize the epitaxial growth with 3D cubes."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    N = grid.shape[0]
    x, y, z = [], [], []
    colors = []

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:  # Na atom
                x.append(j)
                y.append(i)
                z.append(0)
                colors.append('blue')  # Color for Na (1)
            elif grid[i, j] == 0:  # Cl atom
                x.append(j)
                y.append(i)
                z.append(0)
                colors.append('red')  # Color for Cl (0)

    ax.bar3d(x, y, z, 1, 1, 1, color=colors, shade=True)
    ax.set_xlabel('X (Lattice)')
    ax.set_ylabel('Y (Growth)')
    ax.set_zlabel('Z (Height)')
    ax.set_title("Epitaxial Growth (KMC)")
    plt.show()


def plot_3D_growth(grid):
    """Visualize a 3D epitaxial growth simulation with cubes."""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    Nx, Ny, Nz = grid.shape  # Get dimensions
    x, y, z = [], [], []
    colors = []

    # Loop through 3D grid to find occupied sites
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                if grid[i, j, k] == 1:  # Na atom
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    colors.append('blue')
                elif grid[i, j, k] == 0:  # Cl atom
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    colors.append('red')
                elif grid[i,j,k] == None:
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    colors.append((0, 0, 0, 0.0)) # Transparent pour les None


    # Plot 3D cubes using bar3d
    ax.bar3d(x, y, z, 1, 1, 1, color=colors, shade=True)

    
    ax.set_xlabel('X (Width)')
    ax.set_ylabel('Y (Depth)')
    ax.set_zlabel('Z (Height)')
    ax.set_title("3D Epitaxial Growth")

    plt.show()

