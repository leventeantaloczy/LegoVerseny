from __future__ import print_function
from __future__ import division
from builtins import input

from dataStructure import *
from mappingMovement import *
from constans import *

BP = brickpi3.BrickPi3()

move = Movement()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)		#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

for i in range(h):
	for j in range(w):
			Matrix[y][x] = -1
	
time.sleep(2)

try:
	for y in range(h):
		for x in range(w):				
			move.motorRotateDegree(BP.PORT_D, BP.PORT_A, wheelRotateDegree, speed, BP)										#forward 10cm with 230 degree
			try:
				value = BP.get_sensor(BP.PORT_1)																	#TODO: szinszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = color[value]
				print(Matrix[y][x])
			except brickpi3.SensorError as error:
				print(error)
		if(y % 2 == 0):
			print("in if 0")
			move.oneMotorTurn(BP.PORT_D, BP.PORT_A, ninetyDegreeTurn, turnSpeed, BP)
		else:
			print("in if 1")
			move.oneMotorTurn(BP.PORT_A, BP.PORT_D, ninetyDegreeTurn, turnSpeed, BP)

except KeyboardInterrupt:																								#TODO forduljon az x iteracio utan
	BP.reset_all()

f = open("mx.txt", "w+")


for y in range(h):
	for x in range(w):
			f.write(Matrix[y][x])
	f.write("\r\n")
	
f.close()
BP.reset_all()