from __future__ import print_function
from __future__ import division
from builtins import input

import time
import brickpi3
from enum import Enum


class Color(Enum):
	DEFAULT = -1
	WHITE = 0
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4


BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)																				#szenzor init


w = 3																															#width
h = 3																															#height
Matrix = [[Color.DEFAULT.name for x in range(w)] for y in range(h)]																# 7x7 matrix initialization 





def motorRotateDegree(motorPort_1, motorPort_2, degrees, power):																#egyenseben tartó függvény

	power_1 = power
	power_2 = power
	powerInc = power / 5

	BP.reset_motor_encoder(motorPort_1)
	BP.reset_motor_encoder(motorPort_2)

	power = power / 5

	for i in range(5):
		BP.set_motor_power(motorPort_1, power)
		BP.set_motor_power(motorPort_2, power)
		time.sleep(0.05)
		power += powerInc



	while abs(BP.get_motor_encoder(motorPort_1)) <= degrees and abs(BP.get_motor_encoder(motorPort_2)) <= degrees:

		BP.set_motor_power(motorPort_1, power_1)
		BP.set_motor_power(motorPort_2, power_2)

		if(abs(BP.get_motor_encoder(motorPort_2)) - abs(BP.get_motor_encoder(motorPort_1)) > 0):									#A-D
			if(power_1 > power * 1.1):
				power_1 -= 1

		elif(abs(BP.get_motor_encoder(motorPort_1)) - abs(BP.get_motor_encoder(motorPort_2)) > 0):									#D-A
			if(power_2 > power * 1.1):
				power_2 -= 1

		else:
			power_2 = power
			power_1 = power


	BP.set_motor_power(motorPort_1, 0)
	BP.set_motor_power(motorPort_2, 0)

try:
	for y in range(h):
		for x in range(w):					
			motorRotateDegree(BP.PORT_D, BP.PORT_A, 230, -50)																		#forward 10cm with 230 degree
			time.sleep(0.2)
			try:
				value = BP.get_sensor(BP.PORT_1)																					#TODO: színszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = value
				print("X: ", x)
				print("Y:_", y)
				print("Matrix elemei: ", Matrix[y][x])
			except brickpi3.SensorError as error:
				print(error)
except KeyboardInterrupt:																											#TODO forduljon az x iteráció után
	BP.reset_all()

BP.reset_all()






