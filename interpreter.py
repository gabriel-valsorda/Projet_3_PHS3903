import matplotlib.pyplot as plt

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
