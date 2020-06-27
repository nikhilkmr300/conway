import numpy as np

import sys
sys.path.append('../')

from conway import *

grid = -np.ones((17, 17))
grid[4:7, [2, 7, 9, 14]] = 1
grid[10:13, [2, 7, 9, 14]] = 1
grid[[2, 7, 9, 14], 4:7] = 1
grid[[2, 7, 9, 14], 10:13] = 1

# Period = 3
saveAnimation(animate(grid, 99, title='Pulsar', figtext='Nikhil Kumar'), '../animations/pulsar.mp4')
