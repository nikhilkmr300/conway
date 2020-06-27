import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import itertools

def takeStep(grid):
    """
    Takes one step of Conway's Game of Life on grid.

    Parameters:
    grid (NumPy ndarray): State of the grid before taking a step.

    Returns:
    NumPy ndarray: State of the grid after taking the step.
    """

    newGrid = np.empty(grid.shape)

    # Iterating over rows and columns of grid
    for row, col in list(itertools.product(range(grid.shape[0]), range(grid.shape[1]))):
        # If live cell (+1)
        if(grid[row, col] == 1):
            # If number of live neighbours is < 2 or > 3, dies
            if(findLiveNeighbourCount(grid, row, col) < 2 or findLiveNeighbourCount(grid, row, col) > 3):
                newGrid[row, col] = -1
            # Else if number of live neighbours is 2 or 3, lives
            elif(findLiveNeighbourCount(grid, row, col) in {2, 3}):
                newGrid[row, col] = 1
        # If dead cell
        elif(grid[row, col] == -1):
            # If number of live neighbours is 3, becomes alive
            if(findLiveNeighbourCount(grid, row, col) == 3):
                newGrid[row, col] = 1
            # Else stays dead
            else:
                newGrid[row, col] = -1

    return newGrid

def findLiveNeighbourCount(grid, row, col):
    """
    Finds the number of live neighbours in the Moore neighbourhood of a cell.

    Parameters:
    grid (NumPy ndarray): Grid on which the game is being played.
    row (int): Row of the cell of interest in the grid.
    col (int): Column of the cell of interest in the grid.

    Returns:
    int: Number of live neighbours around the cell grid[row, col].
    """

    if(grid.shape[0] <= 3 or grid.shape[1] <= 3):
        print('grid must be of shape at least 4x4 to avoid overlap of neighbours at corners')
        return None

    numRows, numCols = grid.shape
    # Indices of 8 nearest neighbours as a list of 2-tuples
    neighbourIndices = list(itertools.product([(row-1)%numRows, row, (row+1)%numRows], [(col-1)%numCols, col, (col+1)%numCols]))
    neighbourIndices.remove((row, col))

    count = 0   # Counter for live (+1) neighbours
    for i, j in neighbourIndices:
        if(grid[i, j] == 1):
            count += 1

    return count

def animate(initialGrid, numSteps=100, repeat_delay=3000, cmap='gray_r', title='', figtext=''):
    """
    Creates an animation of Conway's Game of Life, given an intial grid.

    Parameters:
    initialGrid (NumPy ndarray): Initial state of the grid.
    numSteps (int, optional): Number of steps/generations in the game.
    repeat_delay (int, optional): Time in ms to wait before looping the animation.
    cmap (str or matplotlib.colors.Colormap object, optional): Colormap to be
        used.
    title (str, optional): Title for the animation.
    figtext (str, optional): Text placed before figure.

    Returns:
    matplotlib.animation.ArtistAnimation object: Contains the animation.
    """

    grid = initialGrid
    images = [[plt.imshow(grid, cmap=cmap)]]

    for i in range(numSteps):
        grid = takeStep(grid)
        image = plt.imshow(grid, cmap=cmap)
        images.append([image])

    fig = plt.figure(1)
    axes = plt.gca()
    axes.set_xticks([])
    axes.set_yticks([])
    plt.title(title)
    plt.figtext(0.5, 0.02, figtext, ha='center')
    animatedGame = ArtistAnimation(fig, images, blit=True, repeat_delay=repeat_delay)
    plt.show()

    return animatedGame

def saveAnimation(animatedGame, filePath):
    """
    Saves animation as returned by animate.

    Parameters:
    animatedGame (matplotlib.animation.ArtistAnimation objec): Animation to be
        saved.
    filePath (str): File path to where the animation will be saved.
    """

    print(f'Saving animation to {filePath} ...')
    animatedGame.save(filePath)
