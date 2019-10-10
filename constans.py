 #--------------------------------------------------------------------------------------#
#                                                                                      #
#                                                                                      #
#                                                                                      #
#                                                                                      #
#                                  Konstans ertekek                                    #
#                                                                                      #
#                                                                                      #
#                                                                                      #
#                                                                                      #
#--------------------------------------------------------------------------------------#
from dataStructure import *

redZoneX = 3	#piros ledobo zona X koordinata
greenZoneX = 6		#zold -||-
blueZoneX = 9		#kek -||-

speed = -65
turnSpeed = 80
wheelRotateDegree = 910 
turnTime = 0.8			#800 - 6.4 cm #850 az ideal
waitSecs = 0.4
rampDown = 150
glassTrace = 400
closeDist = 12

KP = 0.01
KI = 0.0001
KD = 0.01
SAMPLETIME = 0.5
TARGET = 255