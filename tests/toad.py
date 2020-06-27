import numpy as np

import sys
sys.path.append('../')

from conway import *

grid = -np.ones((6, 6))
grid[2, 2:5] = 1
grid[3, 1:4] = 1

# Period = 2
saveAnimation(animate(grid, 100, title='Toad', figtext='Nikhil Kumar'), '../animations/toad.mp4')
