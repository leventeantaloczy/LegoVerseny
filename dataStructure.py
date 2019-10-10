from __future__ import print_function

from enum import Enum


class Color(Enum):
	DEFAULT = -1
	WHITE = 0
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4



w = 5																															#width
h = 5																															#height
Matrix = [[Color.DEFAULT.name for x in range(w + 1)] for y in range(h + 1)]																# 7x7 matrix initialization 

