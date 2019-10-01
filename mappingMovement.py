from __future__ import print_function
from __future__ import division
from builtins import input

from dataStructure import *

import time
import brickpi3


class Movement:

	def motorRotateDegree(self, motorPort_1, motorPort_2, degrees, power, BP, rampUpBoolean):															#egyenseben tarto fuggveny

		power_1 = power
		power_2 = power
		powerInc = power / 5

		BP.reset_motor_encoder(motorPort_1)
		BP.reset_motor_encoder(motorPort_2)
		if(rampUpBoolean):
			power /= 5
			for i in range(4):
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

	def oneMotorTurn(self, motorPort, motorPort_stop, turnDegree, power, BP):
		BP.reset_motor_encoder(motorPort)
		BP.reset_motor_encoder(motorPort_stop)

		powerInc = power / 5
		BP.set_motor_power(motorPort_stop, 0)
		power /= 5
		for i in range(4):
			BP.set_motor_power(motorPort, power)
			time.sleep(0.05)
			power += powerInc


		while  abs(BP.get_motor_encoder(motorPort)) <= turnDegree:
			BP.set_motor_power(motorPort, power)
			BP.set_motor_power(motorPort_stop, 0)

		BP.set_motor_power(motorPort, 0)
		time.sleep(0.1)



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

