from __future__ import print_function
from __future__ import division
from builtins import input
import time

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *
from movementSolve import *

BP = brickpi3.BrickPi3()
rampUp = 0
move = Movement()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)																#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
	
time.sleep(3)

try:																								#EZ EGY TESZT MAIN, HA CSAK AZ UTVONALTERVEZEST KELL TESZTELNI FAJLBOL BEOLVASOTT MATRIXXAL
	testMatrix = readMatrixFromFile(11, 11)
	testMatrix = processRawMatrix(testMatrix)
	startX, startY, color = winVerseny(BP, testMatrix, 0, h)
	printMatrix(testMatrix)
	print("End Color1: ", color)
	testMatrix = deleteColorFromMatrix(testMatrix, color)
	startX, startY, color = winVerseny(BP, testMatrix, startX, startY)
	print("End Color2: ", color)
	testMatrix = deleteColorFromMatrix(testMatrix, color)
	startX, startY, color = winVerseny(BP, testMatrix, startX, startY)

except KeyboardInterrupt:
	BP.reset_all()

BP.reset_all()



#move.centralTurnSec(BP.PORT_C, 1.3, -50, BP)