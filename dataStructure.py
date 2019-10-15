from __future__ import print_function

from enum import Enum


class Color(Enum):
	DEFAULT = -1
	WHITE = 0
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4



w = 120																															#width
h = 10																													#height
bigMatrix = [[0 for x in range(w + 1)] for y in range(h + 1)]
Matrix = [[0 for x in range(11)] for y in range(11)]																	# matrix initialization 