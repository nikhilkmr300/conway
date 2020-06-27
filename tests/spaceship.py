import numpy as np

import sys
sys.path.append('../')

from conway import *

grid = -np.ones((7, 20))
grid[1, [2, 3]] = 1
grid[2, 1:5] = 1
grid[3, [1, 2, 4, 5]] = 1
grid[4, [3, 4]] = 1

saveAnimation(animate(grid, 80, title='Spaceship', figtext='Nikhil Kumar'), '../animations/spaceship.mp4')
