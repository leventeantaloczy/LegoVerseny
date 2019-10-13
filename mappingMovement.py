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

	def motorRotateDegreeNewB(self, motorPort_1, motorPort_2, degrees, power, BP, rampUpSteps):															#egyenseben tarto fuggveny

			power_1 = -power
			power_2 = -power

			BP.reset_motor_encoder(motorPort_1)
			BP.reset_motor_encoder(motorPort_2)
			if(rampUpSteps > 1):
				powerInc1 = power_1 / rampUpSteps
				powerInc2 = power_2 / rampUpSteps
				power_1 /= rampUpSteps
				power_2 /= rampUpSteps
				for i in range(rampUpSteps - 1):
					BP.set_motor_power(motorPort_1, power_1)
					BP.set_motor_power(motorPort_2, power_2)
					time.sleep(0.05)
					power_1 += powerInc1
					power_2 += powerInc2

			while abs(BP.get_motor_encoder(motorPort_1)) <= degrees and abs(BP.get_motor_encoder(motorPort_2)) <= degrees:

				BP.set_motor_power(motorPort_1, power_1)
				BP.set_motor_power(motorPort_2, power_2)
				#print("Encoder1 ", BP.get_motor_encoder(motorPort_1), "Encoder2: ", BP.get_motor_encoder(motorPort_2))
				#print("Power1 ", power_1, "Power2: ", power_2)	

				if(abs(BP.get_motor_encoder(motorPort_2)) - abs(BP.get_motor_encoder(motorPort_1)) > 0):									#A-D
					if(abs(power_1) < abs(power * 1.1)):
						power_1 += 1

				elif(abs(BP.get_motor_encoder(motorPort_1)) - abs(BP.get_motor_encoder(motorPort_2)) > 0):									#D-A
					if(abs(power_2) < abs(power * 1.1)):
						power_2 += 1

				else:
					power_1 = -power
					power_2 = -power

			time.sleep(0.01)

	def motorRotateDegreeNewF(self, motorPort_1, motorPort_2, degrees, power, BP, rampUpSteps):															#egyenseben tarto fuggveny

				power_1 = power
				power_2 = power
				BP.reset_motor_encoder(motorPort_1)
				BP.reset_motor_encoder(motorPort_2)
				if(rampUpSteps > 0):
					powerInc1 = power_1 / rampUpSteps
					powerInc2 = power_2 / rampUpSteps
					power_1 /= rampUpSteps
					power_2 /= rampUpSteps
					for i in range(rampUpSteps - 1):
						#print("Pow1: ", power_1, "Pow2: ", power_2)
						BP.set_motor_power(motorPort_1, power_1)
						BP.set_motor_power(motorPort_2, power_2)
						time.sleep(0.05)
						power_1 += powerInc1
						power_2 += powerInc2

				print("Forward \n\r __________________________")


				while abs(BP.get_motor_encoder(motorPort_1)) <= degrees and abs(BP.get_motor_encoder(motorPort_2)) <= degrees:

					BP.set_motor_power(motorPort_1, power_1)
					BP.set_motor_power(motorPort_2, power_2)
					#print("Encoder1 % 3d Encoder2 % 3d power_1 % 3d power_2 % 3d" %(BP.get_motor_encoder(motorPort_1), BP.get_motor_encoder(motorPort_2), power_1, power_2))

					if(abs(BP.get_motor_encoder(motorPort_2)) - abs(BP.get_motor_encoder(motorPort_1)) > 0):
																						#A-D
						if(abs(power_1) < abs(power * 1.1)):
							power_1 -= 1

					elif(abs(BP.get_motor_encoder(motorPort_1)) - abs(BP.get_motor_encoder(motorPort_2)) > 0):									#D-A
						if(abs(power_2) < abs(power * 1.1)):
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


	def centralTurnSec(self, Port, seconds, power, BP):
		BP.set_motor_power(BP.PORT_A, 0)
		BP.set_motor_power(BP.PORT_B, 0)

		BP.reset_motor_encoder(BP.PORT_A)
		BP.reset_motor_encoder(BP.PORT_B)
		BP.set_motor_power(Port, power)
		if(power < 0):
			bigPower = 19
		else:
			bigPower = -19
		BP.set_motor_power(BP.PORT_A, bigPower)
		BP.set_motor_power(BP.PORT_B, bigPower)
		startTime = time.time()

		while(abs(BP.get_motor_encoder(BP.PORT_A)) <= 90 or abs(BP.get_motor_encoder(BP.PORT_B)) <= 90 or (time.time() - startTime <= seconds)):
			#print(BP.get_motor_encoder(BP.PORT_A))
			#print(time.time()- startTime)
			if(time.time() - startTime >= seconds):
				#print("behatoltam kozepesen")
				BP.set_motor_power(Port, 0)
			if(abs(BP.get_motor_encoder(BP.PORT_A)) >= 180):
				#print("behatoltam nagyonA")
				BP.set_motor_power(BP.PORT_A, 0)
			if(abs(BP.get_motor_encoder(BP.PORT_B)) >= 90):
				#print("behatoltam nagyonB")
				BP.set_motor_power(BP.PORT_B, 0)
		BP.set_motor_power(BP.PORT_A, 0)
		BP.set_motor_power(BP.PORT_B, 0)
		BP.set_motor_power(Port, 0)
		time.sleep(0.1)

	def stopMotors(self, BP):
		BP.set_motor_power(BP.PORT_B, 0)
		BP.set_motor_power(BP.PORT_A, 0)
		BP.set_motor_power(BP.PORT_C, 0)

