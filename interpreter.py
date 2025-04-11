import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import imageio
from numpy import linspace

def plot_growth_2d(grid,show=True):
    """Draw a 2D square grid with different colors for 0, 1 and nothing for None."""
    nrows, ncols = grid.shape[0], grid.shape[1]
    fig, ax = plt.subplots(figsize=(6, 6))
    
    ax.set_xlim(0, nrows)
    ax.set_ylim(0, ncols)
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
    if show:
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

def save_graph(grid,step,tempsreel):
    """Draw a 2D square grid with different colors for 0, 1 and nothing for None."""
    os.makedirs("frames", exist_ok=True)

    plot_growth_2d(grid=grid,show=False)
    
    plt.text(8.5, 0.5, f"{round(tempsreel,3)}s")
    plt.savefig(f"frames/frame_{int(step):03d}.png")
    plt.close()
    return

def creer_gif(dossier, nom_gif="evolution.gif", fps=0.5):
    fichiers = sorted(
        [f for f in os.listdir(dossier) if f.endswith(".png")]
    )
    chemin_gif = os.path.join(dossier, nom_gif)
    
    with imageio.get_writer(chemin_gif, mode='I', duration=1/fps) as writer:
        for nom in fichiers:
            image = imageio.imread(os.path.join(dossier, nom))
            writer.append_data(image)

    print(f"GIF enregistré dans : {chemin_gif}")




def gamma_dt(gamma, dim, kT, deltamu, save=False):
    """
    Calcule la valeur de gamma en fonction du nombre de pas de temps.
    """
    x = linspace(0,len(gamma),len(gamma))
    
    plt.figure()
    plt.plot(x, gamma, label='$\Gamma$')
    plt.title(f"Taux de croissance en fonction du temps pour une grille {dim[0]}x{dim[1]}\nPour kT={kT} et $\Delta\mu$={deltamu}")
    plt.xlabel("Pas de temps")
    plt.ylabel("$\Gamma$")
    plt.legend()
    plt.grid()
    if save:
        plt.savefig(f"frames/gamma_{int(kT*100)}_{int(deltamu*100)}.png")
    plt.show()

def rugosite_dt(nb_pas_temps, rugosite, dim, kT, deltamu, save=False):
    """
    Calcule la valeur de la rugosite en fonction du nombre de pas de temps.
    """
    x = linspace(0,len(rugosite),len(rugosite))
    
    plt.figure()
    plt.plot(x, rugosite, label='Rugosite')
    plt.title(f"Rugosite en fonction du temps pour une grille {dim[0]}x{dim[1]}\nPour kT={kT} et $\Delta\mu$={deltamu}")
    plt.xlabel("Pas de temps")
    plt.ylabel("Rugosite")
    plt.legend()
    plt.grid()
    if save:
        plt.savefig(f"frames/rugosite_{int(kT*100)}_{int(deltamu*100)}.png")
    plt.show()