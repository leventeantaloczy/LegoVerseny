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
rampUp = False
move = Movement()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)															#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

for i in range(h + 1):
	for j in range(w + 1):
			Matrix[i][j] = 6
	
time.sleep(3)

try:
	for y in range(h + 1):
		for x in range(w):
			if(x == 0):
				rampUp = True

			try:
				value = BP.get_sensor(BP.PORT_2)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = value
				print(Matrix[y][x])
			except brickpi3.SensorError as error:
				print(error)

			if(y % 2 == 0):
				move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
			else:
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
			rampUp = False
		if(y % 2 == 0):
			try:
				value = BP.get_sensor(BP.PORT_2)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = value
				print(Matrix[y][x + 1])
			except brickpi3.SensorError as error:
				print(error)
			move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
			time.sleep(0.2)
			move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, True)
			move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP) #1.3 @50
			time.sleep(0.2)

		else:
			try:
				value = BP.get_sensor(BP.PORT_2)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = value
				print(Matrix[y][x + 1])
			except brickpi3.SensorError as error:
				print(error)
			move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
			time.sleep(0.2)
			move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, True)
			move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
			time.sleep(0.2)

except KeyboardInterrupt:
	BP.reset_all()

var = raw_input()


winVerseny(BP, processRawMatrix(Matrix))

f = open("mx.txt", "w+")

for y in range(h + 1):
	for x in range(w + 1):
		f.write("%s " %color[Matrix[y][x]])
	f.write("\r\n")
	
f.close()

BP.reset_all()



#move.centralTurnSec(BP.PORT_C, 1.3, -50, BP)