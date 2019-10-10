from __future__ import print_function
from __future__ import division
from builtins import input
import time

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *
from movementSolve import *
from PID import *

BP = brickpi3.BrickPi3()
rampUp = 0
move = Movement()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)																#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

for i in range(h + 1):
	for j in range(w + 1):
			Matrix[i][j] = 6
	
time.sleep(3)

<<<<<<< HEAD
p = PID()
=======
try:
	for y in range(h):
		for x in range(w):
			if(x == 0):
				rampUp = 15

			try:
				value = BP.get_sensor(BP.PORT_2)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = value
				print(Matrix[y][x])
			except brickpi3.SensorError as error:
				print(error)

			if(y % 2 == 0):
				if(x >= w - 1):
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree -rampDown, speed, BP, 0)
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
				else:
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

			else:
				if(x >= w - 1):
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree -rampDown, speed, BP, 0)
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
				else:
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
			rampUp = 0
		if(y < h):
			if(y % 2 == 0):
				try:
					value = BP.get_sensor(BP.PORT_2)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
					Matrix[y][x] = value
					print(Matrix[y][x + 1])
				except brickpi3.SensorError as error:
					print(error)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
				time.sleep(waitSecs)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree - rampDown, speed, BP, 15)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP) #1.3 @50
				time.sleep(waitSecs)

			else:
				try:
					value = BP.get_sensor(BP.PORT_2)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
					Matrix[y][x] = value
					print(Matrix[y][x + 1])
				except brickpi3.SensorError as error:
					print(error)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
				time.sleep(waitSecs)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree - rampDown, speed, BP, 15)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, rampDown, -20, BP, 0)
				time.sleep(waitSecs)
				move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
				time.sleep(waitSecs)
>>>>>>> 9f9553f3cf2e265519e6b3d1c2f7c04cdac6060

try:
	p.go(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP)
except KeyboardInterrupt:
	BP.reset_all()

<<<<<<< HEAD
=======
var = raw_input()


winVerseny(BP, processRawMatrix(Matrix))

f = open("mx.txt", "w+")

for y in range(h + 1):
	for x in range(w + 1):
		f.write("%d " %Matrix[y][x])
	f.write("\r\n")
	
f.close()

>>>>>>> 9f9553f3cf2e265519e6b3d1c2f7c04cdac60609
BP.reset_all()



#move.centralTurnSec(BP.PORT_C, 1.3, -50, BP) 