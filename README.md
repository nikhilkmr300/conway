# conway
An implementation of Conway's Game of Life.

Conway's Game of Life (CGL) is a cellular automaton created by mathematician John Conway in 1970.
A cellular automaton is a system that consists of a matrix of cells,
wherein each cell can have a set of states (CGL has two states -- on and off).
The system evolves and creates a new *generation* through a set of rules that describe how the cells change their states.
Cells are affected by the cells in their *neighbourhood*.
Commonly used neighbourhoods are the Moore neighbourhood (which CGL uses) and the Moore neighbourhood.

The rules for CGL are listed in the rules.txt file, 
and can also be found at the Wikipedia page on CGL (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

The same page also has a detailed list of CGL systems,
some of which are implemented in the tests directory.

References:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life, 
https://en.wikipedia.org/wiki/Cellular_automaton, 
