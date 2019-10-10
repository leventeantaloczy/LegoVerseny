from __future__ import print_function
from __future__ import division
from builtins import input
import time

from dataStructure import *
from mappingMovement import *
from constans import *
from matrixCalc import *
from movementSolve import *
from PID import *

BP = brickpi3.BrickPi3()
rampUp = False
move = Movement()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)															#A - bal, D - jobb motor
color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

for i in range(h + 1):
	for j in range(w + 1):
			Matrix[i][j] = 6
	
time.sleep(3)

p = PID()

try:
	p.go(BP.PORT_A, BP.PORT_B, wheelRotateDegree, speed, BP)
except KeyboardInterrupt:
	BP.reset_all()

BP.reset_all()



#move.centralTurnSec(BP.PORT_C, 1.3, -50, BP) 