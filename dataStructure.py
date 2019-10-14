from __future__ import print_function

from enum import Enum


class Color(Enum):
	DEFAULT = -1
	WHITE = 0
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4



w = 10																															#width
h = 10																													#height
Matrix = [[0 for x in range(w + 1)] for y in range(h + 1)]																# matrix initialization 