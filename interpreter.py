import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_growth_2d(grid):
    """Draw a 2D square grid with different colors for 0, 1 and nothing for None."""
    nrows, ncols = len(grid), len(grid[0])
    fig, ax = plt.subplots(figsize=(6, 6))
    
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_aspect('equal')
    # ax.invert_yaxis()  # Optional: flip so row 0 is at the top
    # ax.axis('off')

    for i in range(nrows):
        for j in range(ncols):
            val = grid[i][j]
            if val == 0:
                color = 'red'
            elif val == 1:
                color = 'blue'
            else:
                continue  # Skip None
            
            # Add square at position (j, i)
            square = Rectangle((i, j), 1, 1, facecolor=color, edgecolor='black')
            ax.add_patch(square)
    plt.gca().invert_xaxis()
    plt.title("Epitaxial Growth (2D Tiles)")
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
