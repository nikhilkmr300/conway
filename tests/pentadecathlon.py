import numpy as np

import sys
sys.path.append('../')

from conway import *

grid = -np.ones((18, 11))
grid[6:12, [3, 7]] = 1
grid[[4, 13], 5] = 1
grid[[5, 12], 4] = 1
grid[[5, 12], 6] = 1

# Period = 15
saveAnimation(animate(grid, 90, title='Pentadecathlon', figtext='Nikhil Kumar'), '../animations/pentadecathlon.mp4')
