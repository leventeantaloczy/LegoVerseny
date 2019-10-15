from __future__ import print_function
from __future__ import division
from builtins import input
import time

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *
from movementSolve import *
import sys
import constans as con
import matrixCalc

options = sys.argv
print(options)
con.init()
matrixCalc.setZones(options)

BP = brickpi3.BrickPi3()
rampUp = 0
move = Movement()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)																#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
	
time.sleep(3)

try:																								#EZ EGY TESZT MAIN, HA CSAK AZ UTVONALTERVEZEST KELL TESZTELNI FAJLBOL BEOLVASOTT MATRIXXAL
	testMatrix = readMatrixFromFile(11, 121)
	printMatrix(testMatrix)
	Matrix = matrixMedian(testMatrix, 11)
	Matrix = processRawMatrix(Matrix)
	Matrix = removeBelow(Matrix)
	startX, startY, color = winVerseny(BP, Matrix, 0, h)
	printMatrix(Matrix)
	print("End Color1: ", color)
	Matrix = deleteColorFromMatrix(Matrix, color)
	startX, startY, color = winVerseny(BP, Matrix, startX, startY)
	print("End Color2: ", color)
	Matrix = deleteColorFromMatrix(Matrix, color)
	startX, startY, color = winVerseny(BP, Matrix, startX, startY)

except KeyboardInterrupt:
	BP.reset_all()

BP.reset_all()



#move.centralTurnSec(BP.PORT_C, 1.3, -50, BP)