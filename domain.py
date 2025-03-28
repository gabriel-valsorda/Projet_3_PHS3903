import numpy as np

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

def interatomic_distance(grid,periodicity=0):
    '''
    Calcul des distances des ions de la configuration pour chaque site vacant de surface
    '''
    surface = np.array(find_surface(grid))
    Na_ions, Cl_ions = find_ions(grid)
    Na_ions, Cl_ions = np.array(Na_ions), np.array(Cl_ions)
    
    if periodicity == 0:
        for vacant in surface:
            Na_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Na_ions]
            Cl_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Cl_ions]

    else:
        Nx, Ny = grid.shape
        Na_ions_temp = Na_ions.copy()
        Cl_ions_temp = Cl_ions.copy()

        for n in range(periodicity):
            # Periodicite en +x:
            Na_ions_temp[:,0] += Nx
            Cl_ions_temp[:,0] += Nx

            Na_ions = np.vstack((Na_ions,Na_ions_temp))
            Cl_ions = np.vstack((Cl_ions,Cl_ions_temp))

            # Periodicite en -x:
            Na_ions_temp[:,0] += Nx
            Cl_ions_temp[:,0] += Nx

            Na_ions = np.vstack((Na_ions,Na_ions_temp))
            Cl_ions = np.vstack((Cl_ions,Cl_ions_temp))
        print(Na_ions.shape)
        for vacant in surface:
            Na_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Na_ions]
            Cl_distance = [np.linalg.norm(abs(ion-vacant)) for ion in Cl_ions]

    return Na_distance, Cl_distance            