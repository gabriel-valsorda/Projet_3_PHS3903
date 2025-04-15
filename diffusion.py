import numpy as np


def diffusion(grid, surface_positions, jump_energie, ):
    """
    Simulate the diffusion of atoms on a 2D grid.

    Parameters:
    - grid: 2D numpy array representing the grid.
    - surface_positions: List of tuples representing the positions of atoms on the surface.
    - delta_t: Time step for the simulation.
    - diffusion_constant: Diffusion constant for the atoms.

    Returns:
    - Probability of diffusion
    """
    
    nx, ny = grid.shape

    # Create a copy of the grid to store new positions
    new_grid = np.copy(grid)


    return 
