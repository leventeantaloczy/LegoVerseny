from __future__ import print_function
from __future__ import division
from builtins import input
import time

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *

move = Movement()
rampUp = 15
def winVerseny(BP, Matrix):
		pathString = calculatePath(Matrix)
		print(pathString)
		wheels = 1
		try:
								#kerekek allasa 0 ha x 1 ha y
			for i in range(1, len(pathString)):
				print(pathString[i][0], "x")
				print(pathString[i-1][0], "x-1")
				print(pathString[i][1], "y")
				print(pathString[i-1][1], "y-1")
				if(pathString[i][0] != pathString[i-1][0]):
					if((pathString[i][0] - pathString[i-1][0]) > 0):
						whereTo = 1
					else:
						whereTo = -1
				elif(pathString[i][1] != pathString[i-1][1]):
					if((pathString[i][1] - pathString[i-1][1]) > 0):
						whereTo = -2
					else:
						whereTo = 2
				else:
					whereTo = 0
				print(whereTo, "whereTo")
				if(whereTo == -2):
					if(wheels == 1): #le
						move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
						print("#TODO: hatra mozog a robot")
					else:
						move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
						print("#TODO: kerekek 90fokot fordulnak")
						wheels = 1
						move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
						print("#TODO: hatra mozog a robot")
				elif(whereTo == 2): #fel
					if(wheels == 1):
						move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

						print("#TODO: elore mozog a robot")
					else:
						move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)

						print("#TODO kerekek 90fokot fordulnak")
						wheels = 1
						move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

						print("#TODO elore mozog a robot")
				elif(whereTo == 1): #jobbra
					if(wheels == 0):
						move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

						print("#TODO: elore mozog a robot")
					else:
						move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)

						print("#TODO: kerekek 90fokot fordulnak")
						wheels = 0
						move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

						print("#TODO: elore mozog a robot")
				elif(whereTo == -1): #balra
					if(wheels == 0):
						move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

						print("#TODO: hatra mozog a robot")
					else:
						move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)

						print("#TODO kerekek 90fokot fordulnak")
						wheels = 0
						move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

						print("#TODO hatra mozog a robot")
				elif(whereTo == 0):
					if(wheels == 1):
						move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
						wheels = 0
					BP.reset_motor_encoder(BP.PORT_A)
					BP.reset_motor_encoder(BP.PORT_B)
					BP.set_motor_power(BP.PORT_A, 20)
					BP.set_motor_power(BP.PORT_B, -20)
					notfound = False
					found = False
					while(not notfound and not found):
						try:
							value = BP.get_sensor(BP.PORT_4)																	#TODO: szinszenzor itt olvasson be a mx-ba 
						except brickpi3.SensorError as error:
							print(error)
						if(value < 20):
							found = True
						elif(abs(BP.get_motor_encoder(BP.PORT_A)) >= glassTrace):
							BP.set_motor_power(BP.PORT_A, 0)
							notfound = True
						elif(abs(BP.get_motor_encoder(BP.PORT_B)) >= glassTrace):
							BP.set_motor_power(BP.PORT_B, 0)
					move.stopMotors(BP)
					if(found):
						enslaveOrFreePohar(BP, 65, 0.6)
						move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, abs(BP.get_motor_encoder(BP.PORT_A)), -20, BP, 0)
					else:
						notfound = False
						found = False
						BP.set_motor_power(BP.PORT_A, -20)
						BP.set_motor_power(BP.PORT_B, 20)
						while(not notfound and not found):
							try:
								value = BP.get_sensor(BP.PORT_4)																	#TODO: szinszenzor itt olvasson be a mx-ba 
							except brickpi3.SensorError as error:
								print(error)
							if(value < 20):
								found = True
							elif(abs(BP.get_motor_encoder(BP.PORT_A)) >= glassTrace * 2):
								BP.set_motor_power(BP.PORT_A, 0)
								notfound = True
							elif(abs(BP.get_motor_encoder(BP.PORT_B)) >= glassTrace * 2):
								BP.set_motor_power(BP.PORT_B, 0)
						move.stopMotors(BP)
						enslaveOrFreePohar(BP, 65, 0.6)
						move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, abs(BP.get_motor_encoder(BP.PORT_A)) - glassTrace, -20, BP, 0)
			enslaveOrFreePohar(BP, -65, 0.6)
			try:
				value = BP.get_sensor(BP.PORT_4)																	#TODO: szinszenzor itt olvasson be a mx-ba 
			except brickpi3.SensorError as error:
				print(error)
			if(value < 15):
				move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, 400, -20, BP, 0)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, 400, -20, BP, 0)
		except KeyboardInterrupt:
			BP.reset_all()
	#power: +/-65, seconds: 0.6
	#power: -:up, +:down

def enslaveOrFreePohar(BP, power, seconds):
	print("pohar come at me")
	startTime = time.time()
	timeToRun = seconds
	BP.reset_motor_encoder(BP.PORT_D)
	BP.set_motor_power(BP.PORT_D, power)
	while(time.time() - startTime < timeToRun):
		pass
	BP.set_motor_power(BP.PORT_D, 0)