import numpy as np

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

    