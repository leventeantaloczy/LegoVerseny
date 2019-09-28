from __future__ import print_function
from __future__ import division
from builtins import input

from dataStructure import *
from mappingMpvement import *
from constans import *

BP = brickpi3.BrickPi3()

move = Movement()

try:
	for y in range(h):
		for x in range(w):					
			move.motorRotateDegree(BP.PORT_D, BP.PORT_A, wheelRotateDegree, speed, BP)																#forward 10cm with 230 degree
			time.sleep(0.2)
			try:
				value = BP.get_sensor(BP.PORT_1)																					#TODO: színszenzor itt olvasson be a mx-ba 															
				Matrix[y][x] = value

			except brickpi3.SensorError as error:
				print(error)
except KeyboardInterrupt:																											#TODO forduljon az x iteráció után
	BP.reset_all()

BP.reset_all()