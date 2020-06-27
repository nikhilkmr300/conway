import numpy as np

import sys
sys.path.append('../')

from conway import *

grid = -np.ones((10, 20))
grid[1, 2] = 1
grid[2, 3] = 1
grid[3, 1:4] = 1

# Period = 80
saveAnimation(animate(grid, 80, title='Glider', figtext='Nikhil Kumar'), '../animations/glider.mp4')
