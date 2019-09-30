from __future__ import print_function
from __future__ import division
from builtins import input

from dataStructure import *
from mappingMovement import *
from constans import *

BP = brickpi3.BrickPi3()

move = Movement()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]


time.sleep(2)

try:
	for y in range(h):
		for x in range(w):				
			move.motorRotateDegree(BP.PORT_D, BP.PORT_A, wheelRotateDegree, speed, BP)										#forward 10cm with 230 degree
			try:
				value = BP.get_sensor(BP.PORT_1)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = color[value]
			except brickpi3.SensorError as error:
				print(error)
		if(y % 2 == 0):
			time.sleep(0.2)
			move.degreeTurnLeft(BP.PORT_D, BP.PORT_A, ninetyDegreeTurn, turnSpeed, BP)
			time.sleep(0.2)
			move.motorRotateDegree(BP.PORT_D, BP.PORT_A, wheelRotateDegree, speed, BP)
			time.sleep(0.2)
			move.degreeTurnLeft(BP.PORT_D, BP.PORT_A, ninetyDegreeTurn, turnSpeed, BP)
			time.sleep(0.2)
		else:
			time.sleep(0.2)
			move.degreeTurnRight(BP.PORT_D, BP.PORT_A, ninetyDegreeTurn, turnSpeed, BP)
			time.sleep(0.2)
			move.motorRotateDegree(BP.PORT_D, BP.PORT_A, wheelRotateDegree, speed, BP)
			time.sleep(0.2)
			move.degreeTurnRight(BP.PORT_D, BP.PORT_A, ninetyDegreeTurn, turnSpeed, BP)
			time.sleep(0.2)

except KeyboardInterrupt:																								#TODO forduljon az x iteracio utan
	BP.reset_all()

for i in range(h):
	for j in range(w):
		print("X: ", i, "Y: ", j, " | ", Matrix[i][j])
	

BP.reset_all()