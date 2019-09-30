from __future__ import print_function
from __future__ import division
from builtins import input

from dataStructure import *

import time
import brickpi3


class Movement:

	def motorRotateDegree(self, motorPort_1, motorPort_2, degrees, power, BP):															#egyenseben tarto fuggveny

		#BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)																				#szenzor init
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

		time.sleep(0.01)




	def degreeTurnLeft(self, motorPort_1, motorPort_2, turnDegree, power, BP):



		BP.reset_motor_encoder(motorPort_1)
		BP.reset_motor_encoder(motorPort_2)

		power_1 = power
		power_2 = power * -1


		while abs(BP.get_motor_encoder(motorPort_1)) <= turnDegree and abs(BP.get_motor_encoder(motorPort_2)) <= turnDegree:

			BP.set_motor_power(motorPort_1, power_1)
			BP.set_motor_power(motorPort_2, power_2)

			
			if(abs(BP.get_motor_encoder(motorPort_2)) - abs(BP.get_motor_encoder(motorPort_1)) > 0):									#A-D
				if(power_1 > power * 1.1):
					power_1 -= 1

			elif(abs(BP.get_motor_encoder(motorPort_1)) - abs(BP.get_motor_encoder(motorPort_2)) > 0):									#D-A
				if(power_2 < power * -1.1):
					power_2 += 1

			else:
				power_2 = power * -1
				power_1 = power

		BP.set_motor_power(motorPort_1, 0)
		BP.set_motor_power(motorPort_2, 0)

		time.sleep(0.1)

	def degreeTurnRight(self, motorPort_1, motorPort_2, turnDegree, power, BP):

		BP.reset_motor_encoder(motorPort_1)
		BP.reset_motor_encoder(motorPort_2)

		power_1 = power * -1
		power_2 = power


		while abs(BP.get_motor_encoder(motorPort_1)) <= turnDegree and abs(BP.get_motor_encoder(motorPort_2)) <= turnDegree:

			value1 = BP.get_motor_encoder(motorPort_1)
			value2 = BP.get_motor_encoder(motorPort_2)
			BP.set_motor_power(motorPort_1, power_1)
			BP.set_motor_power(motorPort_2, power_2)


			if(abs(BP.get_motor_encoder(motorPort_2)) - abs(BP.get_motor_encoder(motorPort_1)) > 0):									#A-D
				if(power_1 < power * -1.1):
					power_1 += 1

			elif(abs(BP.get_motor_encoder(motorPort_1)) - abs(BP.get_motor_encoder(motorPort_2)) > 0):									#D-A
				if(power_2 > power * 1.1):
					power_2 -= 1

			else:
				power_2 = power
				power_1 = power * -1

		BP.set_motor_power(motorPort_1, 0)
		BP.set_motor_power(motorPort_2, 0)

		time.sleep(0.1)
