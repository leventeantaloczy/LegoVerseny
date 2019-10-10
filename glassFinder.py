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
rampUp = 0
move = Movement()
wheels = 1

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

time.sleep(5)

try:

	try:
		valueLeft = BP.get_sensor(BP.PORT_4)
		valueRight = BP.get_sensor(BP.PORT_3)
		print(valueLeft, " ", valueRight)																#TODO: szinszenzor itt olvasson be a mx-ba 
	except brickpi3.SensorError as error:
		print(error)
	if((valueLeft < 35 and valueLeft > 10) or (valueRight < 35 and valueRight > 10)):
		print("something far away!")
		if(wheels == 0):
			move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
			wheels = 1
			time.sleep(1)
		BP.reset_motor_encoder(BP.PORT_A)
		BP.reset_motor_encoder(BP.PORT_B)
		BP.set_motor_power(BP.PORT_A, -30) #Hatra pluszminusz, elore minuszplusz
		BP.set_motor_power(BP.PORT_B, 30)
		while((valueLeft > 10 and valueLeft < 50) or (valueRight > 10 and valueRight < 50)):
			try:
				print("going far away!")
				valueLeft = BP.get_sensor(BP.PORT_4)
				valueRight = BP.get_sensor(BP.PORT_3)
				print(valueLeft, " ", valueRight)																#TODO: szinszenzor itt olvasson be a mx-ba 
			except brickpi3.SensorError as error:
				print(error)
		move.stopMotors(BP)
		deltaY = BP.get_motor_encoder(BP.PORT_A)
	BP.reset_motor_encoder(BP.PORT_A)
	BP.reset_motor_encoder(BP.PORT_B)
	if(wheels == 1):
		move.stopMotors(BP)
		move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
		wheels = 0
	BP.set_motor_power(BP.PORT_A, 20)
	BP.set_motor_power(BP.PORT_B, -20)
	notfound = False
	foundLeft = False
	foundRight = False
	while(not notfound and not foundLeft and not foundRight):
		try:
			valueLeft = BP.get_sensor(BP.PORT_4)
			#print("ValL: ", valueLeft)																	#TODO: szinszenzor itt olvasson be a mx-ba 
		except brickpi3.SensorError as error:
			print(error)
		if(valueLeft < closeDist and valueLeft > 1):
			foundLeft = True
			print("found left!")
		try:
			valueRight = BP.get_sensor(BP.PORT_3)
			#print("ValR: ", valueRight)																	#TODO: szinszenzor itt olvasson be a mx-ba 
		except brickpi3.SensorError as error:
			print(error)
		if(valueRight < closeDist and valueRight > 1):
			foundRight = True
			print("found right!")
		elif(abs(BP.get_motor_encoder(BP.PORT_A)) >= glassTrace):
			BP.set_motor_power(BP.PORT_A, 0)
			notfound = True
			print("NotfoundA")
		elif(abs(BP.get_motor_encoder(BP.PORT_B)) >= glassTrace):
			print("NotfoundB")
			BP.set_motor_power(BP.PORT_B, 0)
			notfound = True
	print("out1")
	move.stopMotors(BP)
	if(foundLeft):
		BP.set_motor_power(BP.PORT_A, 20)
		BP.set_motor_power(BP.PORT_B, -20)
		while(not foundRight):
			try:
				valueRight = BP.get_sensor(BP.PORT_3)
				#print("ValR: ", valueRight)																	#TODO: szinszenzor itt olvasson be a mx-ba 
			except brickpi3.SensorError as error:
				print(error)
			if(valueRight < closeDist and valueRight > 1):
				foundRight = True
				print("found right too!")
		move.stopMotors(BP)
		time.sleep(1)
		move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, 100, -20, BP, 0)
		move.stopMotors(BP)
		enslaveOrFreePohar(BP, 65, 0.6)
	elif(foundRight):
		BP.set_motor_power(BP.PORT_A, -20)
		BP.set_motor_power(BP.PORT_B, 20)
		while(not foundLeft):
			try:
				valueLeft = BP.get_sensor(BP.PORT_4)
				#print("ValL: ", valueLeft)																	#TODO: szinszenzor itt olvasson be a mx-ba 
			except brickpi3.SensorError as error:
				print(error)
			if(valueLeft < closeDist and valueLeft > 1):
				foundLeft = True
				print("found left too!")
		move.stopMotors(BP)
		time.sleep(1)
		move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, 250, -20, BP, 0)
		move.stopMotors(BP)
		enslaveOrFreePohar(BP, 65, 0.6)
	else:
		notfound = False
		foundLeft = False
		foundRight = False
		BP.set_motor_power(BP.PORT_A, -20)
		BP.set_motor_power(BP.PORT_B, 20)
		BP.reset_motor_encoder(BP.PORT_A)
		BP.reset_motor_encoder(BP.PORT_B)
		while(not notfound and not foundLeft and not foundRight):
			print(BP.get_motor_encoder(BP.PORT_A))
			try:
				valueLeft = BP.get_sensor(BP.PORT_4)
				#print("ValL: ", valueLeft)																	#TODO: szinszenzor itt olvasson be a mx-ba 
			except brickpi3.SensorError as error:
				print(error)
			if(valueLeft < closeDist and valueLeft > 1):
				foundLeft = True
				print("found left!")
			try:
				valueRight = BP.get_sensor(BP.PORT_3)
				#print("ValR: ", valueRight)																	#TODO: szinszenzor itt olvasson be a mx-ba 
			except brickpi3.SensorError as error:
				print(error)
			if(valueRight < closeDist and valueRight > 1):
				foundRight = True
				print("found right!")
			elif(abs(BP.get_motor_encoder(BP.PORT_A)) >= glassTrace * 2):
				BP.set_motor_power(BP.PORT_A, 0)
				notfound = True
				print("NotfoundAcant")
			elif(abs(BP.get_motor_encoder(BP.PORT_B)) >= glassTrace * 2):
				print("NotfoundBcant")
				BP.set_motor_power(BP.PORT_B, 0)
				notfound = True
		move.stopMotors(BP)
		if(foundRight):
			BP.set_motor_power(BP.PORT_A, -20)
			BP.set_motor_power(BP.PORT_B, 20)
			while(not foundLeft):
				try:
					valueLeft = BP.get_sensor(BP.PORT_4)
					#print("ValL: ", valueLeft)																	#TODO: szinszenzor itt olvasson be a mx-ba 
				except brickpi3.SensorError as error:
					print(error)
				if(valueLeft < closeDist and valueLeft > 1):
					foundLeft = True
					print("found left too!")
			time.sleep(1)
			move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, 100, -20, BP, 0)
			move.stopMotors(BP)
			enslaveOrFreePohar(BP, 65, 0.6)
		elif(foundLeft):
			BP.set_motor_power(BP.PORT_A, 20)
			BP.set_motor_power(BP.PORT_B, -20)
			while(not foundRight):
				try:
					valueRight = BP.get_sensor(BP.PORT_3)
					#print("ValR: ", valueRight)																	#TODO: szinszenzor itt olvasson be a mx-ba 
				except brickpi3.SensorError as error:
					print(error)
				if(valueRight < closeDist and valueRight > 1):
					foundRight = True
					print("found right too!")
			time.sleep(1)
			move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, 250, -20, BP, 0)
			move.stopMotors(BP)
			enslaveOrFreePohar(BP, 65, 0.6)

		move.stopMotors(BP)
		time.sleep(1)
		move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, abs(BP.get_motor_encoder(BP.PORT_A))-glassTrace, -20, BP, 0)
		move.stopMotors(BP)
	time.sleep(2)
	enslaveOrFreePohar(BP, -65, 0.6)
	move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
	move.stopMotors(BP)
	#power: +/-65, seconds: 0.6
	#power: -:up, +:down
except KeyboardInterrupt:
	BP.reset_all()

def enslaveOrFreePohar(BP, power, seconds):
	print("pohar come at me")
	startTime = time.time()
	timeToRun = seconds
	BP.reset_motor_encoder(BP.PORT_D)
	BP.set_motor_power(BP.PORT_D, power)
	while(time.time() - startTime < timeToRun):
		pass
	BP.set_motor_power(BP.PORT_D, 0)