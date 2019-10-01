from __future__ import print_function
from __future__ import division
from builtins import input

from dataStructure import *
from mappingMovement import *
from constans import *

BP = brickpi3.BrickPi3()
rampUp = False
move = Movement()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)														#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

for i in range(h + 1):
	for j in range(w + 1):
			Matrix[i][j] = -1
	
time.sleep(3)

try:
	for y in range(h):
		for x in range(w):
			if(x == 0):
				rampUp = True										#forward 10cm with 230 degree
			try:
				value = BP.get_sensor(BP.PORT_1)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = color[value]
				print(Matrix[y][x])
			except brickpi3.SensorError as error:
				print(error)
			move.motorRotateDegree(BP.PORT_D, BP.PORT_A, wheelRotateDegree, speed, BP, rampUp)
			rampUp = False
		if(y % 2 == 0):
			print("in if 0")
			try:
				value = BP.get_sensor(BP.PORT_1)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x + 1] = color[value]
				print(Matrix[y][x + 1])
			except brickpi3.SensorError as error:
				print(error)
			move.oneMotorTurn(BP.PORT_D, BP.PORT_A, ninetyDegreeTurn, turnSpeed, BP)
		else:
			print("in if 1")
			try:
				value = BP.get_sensor(BP.PORT_1)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x + 1] = color[value]
				print(Matrix[y][x + 1])
			except brickpi3.SensorError as error:
				print(error)
			move.oneMotorTurn(BP.PORT_A, BP.PORT_D, ninetyDegreeTurn, turnSpeed, BP)

except KeyboardInterrupt:																								#TODO forduljon az x iteracio utan
	BP.reset_all()

f = open("mx.txt", "w+")


for y in range(h + 1):
	for x in range(w + 1):
		f.write("%s " %Matrix[y][x])
	f.write("\r\n")
	
f.close()
BP.reset_all()