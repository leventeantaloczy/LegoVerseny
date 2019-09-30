from __future__ import print_function

from enum import Enum


class Color(Enum):
	DEFAULT = -1
	WHITE = 0
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4



w = 14																															#width
h = 14																															#height
Matrix = [[Color.DEFAULT.name for x in range(w)] for y in range(h)]																# 7x7 matrix initialization 











