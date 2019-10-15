from __future__ import print_function
from __future__ import division
from builtins import input
import time

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *
from numpy import median

move = Movement()
rampUp = 15
wheels = 1
YDist = 0
def winVerseny(BP, Matrix, startX, startY):							#Lefordit egy kapott utvonalat parancssorozatta, start x,y a kovetkezo szin megallapitasa miatt kell, azzal ter vissza.
	global wheels
	print("WHEEELS IN WIN: ", wheels)
	prevDir = -10	#elozo irany ha megegyezik nem kell rampUp
	whereTo = -9
	pathString, color = calculatePath(Matrix, startX, startY)
	print(pathString)
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
			if(prevDir == whereTo):
				rampUp = 0
			else:
				rampUp = 15
			if(whereTo == -2):
				if(wheels == 1):
					print("Le")
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
				else:
					time.sleep(0.2)
					move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
					time.sleep(0.2)
					wheels = 1
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
			elif(whereTo == 2):
				print("Fel")
				if(wheels == 1):
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
				else:
					time.sleep(0.2)
					move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
					time.sleep(0.2)
					wheels = 1
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)

			elif(whereTo == 1):
				print("Jobbra")
				if(wheels == 0):
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
				else:
					time.sleep(0.2)
					move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
					time.sleep(0.2)
					wheels = 0
					move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
			elif(whereTo == -1):
				print("Balra")
				if(wheels == 0):
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
				else:
					time.sleep(0.2)
					move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
					time.sleep(0.2)
					wheels = 0
					move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
			elif(whereTo == 0):
				print("Poharboi")
				move.stopMotors(BP)
				time.sleep(0.2)
				wheels = findGlass(BP, wheels)
			prevDir = whereTo
			newStartX = int(pathString[i][0])					#kovetkezo start pont
			newStartY = int(pathString[i][1])
			print("nX: %d nY: %d" %(newStartX, newStartY))
			print("Kerekek: ", wheels)
		move.stopMotors(BP)
		time.sleep(0.5)
		if(wheels == 0):
			move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
			wheels = 1;
		move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
		move.stopMotors(BP)
		enslaveOrFreePohar(BP, 65, 0.6)
		time.sleep(0.2)
		move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
		move.stopMotors(BP)
		time.sleep(0.2)
		enslaveOrFreePohar(BP, -65, 0.6)
		move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
		move.stopMotors(BP)
		enslaveOrFreePohar(BP, 65, 0.6)
		#if(value < 15):																					#ha nem esett le a pohar kicsit nekimegy majd vissza
		#	move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, 300, -40, BP, 0)
		#	time.sleep(0.2)
		#	move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, 300, -40, BP, 0)
		#	move.stopMotors(BP)
		move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP, rampUp)
		move.stopMotors(BP)
			
	except KeyboardInterrupt:
		BP.reset_all()
	return newStartX, newStartY, color
#power: +/-65, seconds: 0.6
#power: -:up, +:downg

def enslaveOrFreePohar(BP, power, seconds): 			#forklift mozgatas
	print("pohar come at me")
	startTime = time.time()
	timeToRun = seconds
	BP.reset_motor_encoder(BP.PORT_D)
	BP.set_motor_power(BP.PORT_D, -power)
	while(time.time() - startTime < timeToRun):
		pass
	BP.set_motor_power(BP.PORT_D, 0)


def findGlass(BP, wheels):						#objektum kereso, a wheels-t parameterkent kapja, hogy biztosan megylegyen az aktualis irany
	print("wheels in find: ", wheels)
	move.resetMotors(BP)
	time.sleep(0.2)
	value = getSensorMedian(BP, sampleRate * 3)
	if(value > 200):
		print("far far away")
		wheels = trace(-30, proxMin, BP, wheels, False)
	elif(value > proxMax):						#ha nagyon messze van nagy tavban kezd el tracelni
		print("30-nal messzebb")
		wheels = trace(-30, 30, BP, wheels, True)
	elif(value < proxMax and value > proxMin):	#ha 10-30cm kozott van kozeledik amig ele nem kerul vagy melle es elveszti a jelet 
		print("30-10 belul")
		if(wheels == 0):
			move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
			wheels = 1;
		move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, 300, -30, BP, 0)
		while(value > proxMin - 3 and value < proxMax + 10 ):
			BP.set_motor_power(BP.PORT_A, -20)
			BP.set_motor_power(BP.PORT_B, -20)
			value = getSensorMedian(BP, sampleRate)
			print("in 3010 while")
		move.stopMotors(BP)
		YDist = BP.get_motor_encoder(BP.PORT_A)
		print("YDist: ", YDist)
		if(value < proxMin - 3):				#ha kozeledik hozza, nagyon kozel van (-3 range, hogy ne legyen pontatlan es hamar engedje le)
			print("elore fele megtalaltam")
			enslaveOrFreePohar(BP, -65, 0.6)
		else:									#ha elvesztette mert melle ert, el kell kezdeni tracelni kozelre
			print("elvesztettem, tracing")
			wheels = trace(-30, proxMin, BP, wheels, False)
		if(wheels == 0):
			move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
			wheels = 1;
		move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, abs(YDist), -30, BP, 15) #delta Y kompenzacio
	elif(value < proxMin):						#ha egybol ott van elotte
		print("egybol meglett")
		enslaveOrFreePohar(BP, -65, 0.6)
	else:
		pass
	move.stopMotors(BP)
	time.sleep(0.2)
	return wheels


def trace(power, proximity, BP, wheels, distant): #jobbra-balra valo oldalazas, ha megtalalja a poharat lecsap
	move.stopMotors(BP)
	time.sleep(0.2)
	tempEncoder = 0
	count = 0
	print("wheels on trace: ", wheels)
	if(wheels == 1):
		move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
		wheels = 0;
	move.resetMotors(BP)
	print("megindultam jobbra")
	value = getSensorMedian(BP, sampleRate)
	while(abs(BP.get_motor_encoder(BP.PORT_A)) < glassTrace and abs(BP.get_motor_encoder(BP.PORT_B)) < glassTrace and count < 3):  #eloszor jobbra meg glassTrace fokot
		BP.set_motor_power(BP.PORT_A, -30)
		BP.set_motor_power(BP.PORT_B, -30)
		print("A: ", BP.get_motor_encoder(BP.PORT_A))
		print("B: ", BP.get_motor_encoder(BP.PORT_B))
		value = getSensorMedian(BP, sampleRate)
		if(value < proximity):
			count += 1
		else:
			count = 0
	move.stopMotors(BP)
	time.sleep(0.2)
	if(value <= proximity):					#ha a porximity miatt lett vege a ciklusnak megvan az objektum es lecsap
		print("jobbra meglett")
		tempEncoder = abs(BP.get_motor_encoder(BP.PORT_A))
		#move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, glassTrace / 2, -30, BP, 0) #egy kis pozicionalas, meg tesztelni kell
		move.stopMotors(BP)
		time.sleep(0.2)
		if(distant):
			move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
			move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, glassTrace * 1.5, -30, BP, 0)
			enslaveOrFreePohar(BP, -65, 0.6)
			move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, glassTrace * 1.5, -30, BP, 0)
			move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
		else:		
			enslaveOrFreePohar(BP, -65, 0.6)
		move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, tempEncoder + abs(BP.get_motor_encoder(BP.PORT_A)), -30, BP, 0) #vissza a matrixra
	else:
		count = 0
		print("megindultam balra (mert nem lett jobbra)")			#ha nem volt jobbra akkor ketszer annyit probal visszajonni balrafele
		value = getSensorMedian(BP, sampleRate)
		while(BP.get_motor_encoder(BP.PORT_A) < glassTrace and BP.get_motor_encoder(BP.PORT_B) < glassTrace and count < 3):
			BP.set_motor_power(BP.PORT_A, 30)
			BP.set_motor_power(BP.PORT_B, 30)
			print("A: ", BP.get_motor_encoder(BP.PORT_A))
			print("B: ", BP.get_motor_encoder(BP.PORT_B))
			value = getSensorMedian(BP, sampleRate)
			if(value < proximity):
				count += 1
			else:
				count = 0
		move.stopMotors(BP)
		time.sleep(0.2)
		if(value <= proximity):			#ha proximity miatt lett vege akkor lecsap
			print("balra meglett")
			tempEncoder = BP.get_motor_encoder(BP.PORT_A)
			#move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, glassTrace / 2, -30, BP, 0)
			move.stopMotors(BP)
			time.sleep(0.2)
			if(distant):
				move.centralTurnSec(BP.PORT_C, turnTime, turnSpeed, BP)
				move.motorRotateDegreeNewF(BP.PORT_A, BP.PORT_B, glassTrace * 1.5, -30, BP, 0)
				enslaveOrFreePohar(BP, -65, 0.6)
				move.motorRotateDegreeNewB(BP.PORT_A, BP.PORT_B, glassTrace * 1.5, -30, BP, 0)
				move.centralTurnSec(BP.PORT_C, turnTime, -turnSpeed, BP)
				move.resetMotors(BP)
				if(tempEncoder > 0):
					BP.set_motor_power(BP.PORT_A, -30)
					BP.set_motor_power(BP.PORT_B, -30)
					while(abs(BP.get_motor_encoder(BP.PORT_A)) < abs(tempEncoder) and abs(BP.get_motor_encoder(BP.PORT_B)) < abs(tempEncoder)):
						pass
					move.stopMotors(BP)
				else:
					BP.set_motor_power(BP.PORT_A, 30)
					BP.set_motor_power(BP.PORT_B, 30)
					while(abs(BP.get_motor_encoder(BP.PORT_A)) < abs(tempEncoder) and abs(BP.get_motor_encoder(BP.PORT_B)) < abs(tempEncoder)):
						pass
					move.stopMotors(BP)	#kompenzacio

			else:		
				enslaveOrFreePohar(BP, -65, 0.6)
				if(BP.get_motor_encoder(BP.PORT_A) > 0):
					BP.set_motor_power(BP.PORT_A, -30)
					BP.set_motor_power(BP.PORT_B, -30)
					while(BP.get_motor_encoder(BP.PORT_A) > 0 and BP.get_motor_encoder(BP.PORT_B) > 0):
						pass
					move.stopMotors(BP)
				else:
					BP.set_motor_power(BP.PORT_A, 30)
					BP.set_motor_power(BP.PORT_B, 30)
					while(BP.get_motor_encoder(BP.PORT_A) < 0 and BP.get_motor_encoder(BP.PORT_B) < 0):
						pass
					move.stopMotors(BP)	#kompenzacio
		else:
			while(BP.get_motor_encoder(BP.PORT_A) < 0 and BP.get_motor_encoder(BP.PORT_B) < 0):			#ha nem lett meg vissza 0 fokra, de ez pontatlan, meg dolgozni kell rajta(ritka)
				BP.set_motor_power(BP.PORT_A, speed)
				BP.set_motor_power(BP.PORT_B, speed)
			move.stopMotors(BP)
			print("couldnt enslave :(")
	move.stopMotors(BP)
	time.sleep(0.2)
	return wheels

def getSensorMedian(BP, samples): #fog samples szamu szenzoradatot es visszaadja a medianjat. Error spike-ok kiszuresere tokeletes.
	sensorData = []
	for i in range(samples):
		try:
			value = BP.get_sensor(BP.PORT_4)
			sensorData.append(value)													
		except brickpi3.SensorError as error:
			print(error)
	print("Median: ", median(sensorData))
	return median(sensorData)
