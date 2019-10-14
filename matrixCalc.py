from __future__ import print_function
from __future__ import division
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from random import randrange

from dataStructure import *
from constans import *

import numpy as np

#class-t kivettem mert problemazott mindig a selffel, pls fix -T
		
def deleteColorFromMatrix(Matrix, color): #megadott szint alakit at jarhato utta egy matrixban.
	print("COLOR BEFORE:")
	print("Color: ", color)
	printMatrix(Matrix)
	h = len(Matrix)
	w = len(Matrix[0])
	filteredMatrix = [[0 for x in range(w)] for y in range(h)]
	for y in range(h):
		for x in range(w):
			item = Matrix[y][x]
			if(item == color):
				filteredMatrix[y][x] = 6;
			else:
				filteredMatrix[y][x] = item;
	print("COLOR DELETED:")
	printMatrix(filteredMatrix)
	return filteredMatrix


def separateMatricesByEnd(Matrix): # osmatrix a bemenet, unicolorra alakit, visszaadja az ertekes szinu matrixokat es a hozzajuk tartozo celkoordinatakat
	print("flippedMatrix")
	printMatrix(Matrix)
	h = len(Matrix)
	w = len(Matrix[0])
	coloredItemSum = 0;
	filteredMatrix = [[0 for x in range(w)] for y in range(h)]
	for y in range(h):
		for x in range(w):
				item = Matrix[y][x]
				if(item != 4 and item != 6):
					filteredMatrix[y][x] = 2
					coloredItemSum += 1
				elif(item == 4):
					filteredMatrix[y][x] = 0
				else:
					filteredMatrix[y][x] = 1
	printMatrix(filteredMatrix)
	matrixArray = [[[0 for x in range(w)] for y in range(h)] for z in range(coloredItemSum)]
	endCoords = [0 for x in range(coloredItemSum * 2)]
	for i in range(coloredItemSum):
		matrixArray[i], endCoords[i * 2], endCoords[i * 2 + 1] = leaveOneEnd(filteredMatrix, i)

	return matrixArray, endCoords

def getZoneX(Matrix, endCoords, i): #megszerzi a cel mezo szinet es visszaadja a megfelelo szinu zona X koordinatajat (pythonban nincs switch :/ )
	item = Matrix[endCoords[i * 2 + 1] - 1][endCoords[i * 2]]
	print("get Zone Matrix: ")
	printMatrix(Matrix)
	print("chosen colour: ", item)
	print("Y: %d X: %d" %(endCoords[i * 2 + 1] - 1, endCoords[i * 2]))
	if(item == 2):
		return blueZoneX
	if(item == 3):
		return greenZoneX
	if(item == 5):
		return redZoneX
	else:
		return blueZoneX #temp

def leaveOneEnd(Matrix, which): #unicolor matrixban bent hagyja a megadott sorszamu ertekes celt, a tobbit falla alakitja es visszaadja az igy kapott matrixot es a celkoordinatat
	h = len(Matrix)
	w = len(Matrix[0])
	number = 0
	outX = 0
	outY = 0
	filteredMatrix = [[0 for x in range(w)] for y in range(h)]
	for y in range(h):
		for x in range(w):
			item = Matrix[y][x]
			if(item == 2):
				if(number == which):
					filteredMatrix[y][x] = 2
					outX = x
					if(y + 1 > h - 1):
						outY = y
					else:
						outY = y + 1
				else:
					filteredMatrix[y][x] = 0
				number += 1
			else:
				filteredMatrix[y][x] = item
	return filteredMatrix, outX, outY


def numberOfItems(Matrix): #ELAVULT, nem hasznaljuk, integralva lett separateMatricesEnd-be
	h = len(Matrix)
	w = len(Matrix[0])
	sum = 0
	for y in range(h):
		for x in range(w):
			if(Matrix[y][x] > 1):
				sum += 1
	return sum

def printMatrix(Matrix):	#szimpla matrix kiiratas, szepen
	h = len(Matrix)
	w = len(Matrix[0])
	for y in range(h):
		for x in range(w):
			print(Matrix[y][x], " ", end = '')
		print("")
	print("")


def processRawMatrix(Matrix):	#robot altal beolvasott nyers matrixot valtottsoroz es flippel horizontalisan -> valos map
	print("RAW Matrix")
	printMatrix(Matrix)
	nMatrix = np.array(Matrix)
	for i in range(1, h, 2):
		nMatrix[i] = np.flip(nMatrix[i], 0)
	nMatrix = np.flipud(nMatrix)
	flippedMatrix = [[0 for x in range(len(Matrix[0]))] for y in range(len(Matrix))]
	flippedMatrix =	nMatrix.tolist()
	return flippedMatrix


def astar(Matrix, startX, startY, endX, endY): #A* legrovidebb utvonalkereso

	grid = Grid(matrix = Matrix)

	start = grid.node(startX, startY)
	end = grid.node(endX, endY)

	finder = AStarFinder(diagonal_movement = DiagonalMovement.never)

	path, runs = finder.find_path(start, end, grid)
	print(grid.grid_str(path = path, start = start, end = end)) #kirajzolast visszaraktam a szemleletesseg kedveert -T

	return path

matrix2 = [			#pelda matrix
	[1,1,1,1,1],
	[2,1,1,2,1],
	[1,3,1,4,1],
	[1,1,1,5,1],
	[1,1,2,4,1]
]

matrix = [
	[1,1,1,5,1,1,3,4,1,5,1],			#pelda matrix
	[2,1,1,2,1,1,2,3,4,1,2],
	[1,3,1,4,1,2,1,4,1,1,1],
	[1,1,1,5,1,1,3,4,1,5,1],
	[1,1,2,4,1,2,1,4,3,1,1],
	[1,1,1,1,1,1,1,1,1,1,1],
	[2,1,1,2,1,1,2,3,4,1,2],
	[1,3,1,4,1,2,1,4,1,1,1],
	[1,1,1,5,1,1,3,4,1,5,1],
	[1,1,2,4,1,2,1,4,3,1,1],
	[1,1,1,1,1,1,1,1,1,1,1]
]

def calculatePath(matrix, startX, startY): #az osmatrixban megkeresi a legrovidebb uton eljuttathato poharat. Nem koltseges, 11*11-es matrixnal egy pillanat alatt lefut.
	chosenNumber = 0	#kivalasztott matrix sorszama
	finalMatrices, endCoords = separateMatricesByEnd(matrix)	#szetszedett matrixok es a veg koordinatak
	shortestPath = [0 for x in range(h * w)]
	for i in range(len(finalMatrices)):
		currentPathStart = astar(finalMatrices[i], startX, startY, endCoords[i * 2], endCoords[i * 2 + 1])
		currentEndColor = matrix[endCoords[i * 2 + 1] - 1][endCoords[i * 2]]
		print("currentEndColor: ", currentEndColor)										#utvonal starttol poharig
		if(len(currentPathStart) > 0):
			currentPathZone = astar(finalMatrices[i], endCoords[i * 2], endCoords[i * 2 + 1], getZoneX(matrix, endCoords, i), 1) 					#utvonal pohartol zonaig
		else:
			currentPathZone = []
		if(len(currentPathStart) + len(currentPathZone) < len(shortestPath) and len(currentPathStart) != 0 and len(currentPathZone) != 0):	#ha rovidebb a teljes ut es egyik sem lehetetlen
			currentPathStart.extend(currentPathZone)
			shortestPath = currentPathStart
			print("curr end color: ", currentEndColor)
			finalEndColor = currentEndColor					#a kivalasztott utvonal vegpontjanak a szine
			chosenNumber = i
	print("CHOSEN PATH______", chosenNumber, ".")
	astar(finalMatrices[chosenNumber], startX, startY, endCoords[chosenNumber * 2], endCoords[chosenNumber * 2 + 1])	#ujra kiirja a valasztott utat, hogy szemleletes legyen
	currentPathZone = astar(finalMatrices[chosenNumber], endCoords[chosenNumber * 2], endCoords[chosenNumber * 2 + 1], getZoneX(matrix, endCoords, chosenNumber), 0)
	print("FINAL END COLOR: ", finalEndColor) 
	return shortestPath, finalEndColor			#a Start path vege es a Zone path eleje ugyan az a mezo, tehat duplikalva van benne, de nem baj, ekkor fogja tudni a robi h a poharnal van

def fillMatrixRandom(matrix):  		#feltolt egy matrixot random szinekkel, sok feherrel (csak tesztelesre)	
	h = len(Matrix)
	w = len(Matrix[0])
	generatedMatrix = [[6 for x in range(w)] for y in range(h)]
	for y in range(h - 1):
		for x in range(w):
			rnd = randrange(1000)
			generatedMatrix[y][x]
			if(rnd % 2 == 0):
				generatedMatrix[y][x] = 6
			elif(rnd % 3 == 0):
				generatedMatrix[y][x] = randrange(2,4)
			elif(rnd % 5 == 0):
				generatedMatrix[y][x] = 4
			else:
				generatedMatrix[y][x] = 6
	return generatedMatrix
#matrix = processRawMatrix(matrix)
#printMatrix(matrix)
#print(calculatePath(matrix)) #TODO: ezt kell atforditani parancssorozatta a robinak

def readMatrixFromFile(h, w):		#matrix beolvasasa fajlbol, szokozzel elvalasztva
	f = open("sample.txt", "r")
	f1 = f.readlines()
	fileMatrix = [[0 for x in range(w)] for y in range(h)]
	i = 0
	for y in f1:
		fileMatrix[i] = list(map(int, y.split()))
		i += 1
	return fileMatrix