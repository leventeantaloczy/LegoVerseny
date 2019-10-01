from __future__ import print_function
from __future__ import division
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from dataStructure import *



class Matrix:
		

	def filterMatrixByColor(self, Matrix, color):
		h = len(Matrix)
		w = len(Matrix[0])
		filteredMatrix = [[0 for x in range(w)] for y in range(h)]
		for y in range(h):
			for x in range(w):
				item = Matrix[y][x]
				if(item != color and item != 1):
					filteredMatrix[y][x] = 0
				else:
					filteredMatrix[y][x] = 1
		return filteredMatrix


	def filterMatrixToUnicolor(self, Matrix):
		h = len(Matrix)
		w = len(Matrix[0])
		filteredMatrix = [[0 for x in range(w)] for y in range(h)]
		for y in range(h):
			for x in range(w):
				item = Matrix[y][x]
				if(item > 1):
					filteredMatrix[y][x] = 2
				else:
					filteredMatrix[y][x] = Matrix[y][x]
		return filteredMatrix


	def numberOfItems(self, Matrix):
		h = len(Matrix)
		w = len(Matrix[0])
		sum = 0
		for y in range(h):
			for x in range(w):
				if(Matrix[y][x] > 1):
					sum += 1
		return sum

	def astar(self, Matrix, startX, startY, endX, endY):

		grid = Grid(Matrix = Matrix)

		start = grid.node(startX, startY)
		end = grid.node(endX, endY)

		finder = AStarFinder(diagonal_movement = DiagonalMovement.never)

		path, runs = finder.find_path(start, end, grid)

		return path


