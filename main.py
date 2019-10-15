from __future__ import print_function
from __future__ import division
from builtins import input
import time
import sys

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *
from movementSolve import *

import dataStructure as data
import constans as con
import matrixCalc

options = sys.argv
print(options)
con.init()
matrixCalc.setZones(options)

BP = brickpi3.BrickPi3()
rampUp = 0
move = Movement()

print("Red: ", con.redZoneX, " Green: ", con.greenZoneX, " Blue: ", con.blueZoneX)

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)																#A - bal, B - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

for i in range(h + 1):
	for j in range(w + 1):
			bigMatrix[i][j] = 6
	
time.sleep(3)

try:
	for y in range(h):

		if(y % 2 == 0):
			bigMatrix[y] = move.forwardTracking((wheelRotateDegree * 10), speed, BP, 1)
			#move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)

		else:
			bigMatrix[y] = move.backwardTracking((wheelRotateDegree * 10), speed, BP, 1)
			#move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
		rampUp = 0
		if(y < h):
			if(y % 2 == 0):												#paros-paratlan sorok, a cikk-cakk miatt
				try:
					value = BP.get_sensor(BP.PORT_2)																	 															
					bigMatrix[y].append(value)
				except brickpi3.SensorError as error:
					print(error)
				move.stopMotors(BP)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
				time.sleep(waitSecs)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree - rampDown, speed, BP, 15)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
				move.stopMotors(BP)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP) #1.3 @50
				time.sleep(waitSecs)

			else:
				try:
					value = BP.get_sensor(BP.PORT_2)																	 															
					bigMatrix[y].append(value)
				except brickpi3.SensorError as error:
					print(error)
				move.stopMotors(BP)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
				time.sleep(waitSecs)
				if(y < 9):
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree - rampDown, speed, BP, 15)
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
				move.stopMotors(BP)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
				time.sleep(waitSecs)

except KeyboardInterrupt:
	BP.reset_all()

f = open("bigmatrix.txt", "w+")

for y in range(h + 1):
	for x in range(w + 1):
		f.write("%d " %bigMatrix[y][x])
	f.write("\r\n")
	
f.close()

var = raw_input()
Matrix = matrixMedian(bigMatrix, 11)
Matrix = processRawMatrix(Matrix)
Matrix = removeBelow(Matrix)
startX, startY, color = winVerseny(BP, Matrix, 0, h) #startX, Y es color kell a kovetkezo szin kikeresesehez, globalissal valamiert nem mukodott
printMatrix(Matrix)
print("End Color1: ", color) 						#az elso kitorlendo szin
Matrix = deleteColorFromMatrix(Matrix, color)		#szinkitorles -> 6
startX, startY, color = winVerseny(BP, Matrix, startX, startY)	#tovabblepes a kovi szinre
print("End Color2: ", color)						#masodik kitorlendo szin
Matrix = deleteColorFromMatrix(Matrix, color)		
startX, startY, color = winVerseny(BP, Matrix, startX, startY) #csak egy maradt, vege.


BP.reset_all()



#move.centralTurnSec(BP.PORT_C, 1.3, -50, BP)