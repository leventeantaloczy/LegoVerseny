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

speed = -65				#altalanos sebesseg, matrix beolvasaskor es utvonal kereseskor is
turnSpeed = 80			#kerekek fizkai elfordulasanak sebessege
wheelRotateDegree = 910 #egy matrix mezo oldalanak hossza
turnTime = 0.65		#lemerult: 0.8-1.0	feltoltve 0.65-0.75
waitSecs = 0.4		#altalanos varakozasi ido
rampDown = 150		#matrix beolvasasnal lassitas hossza
glassTrace = 400	#tracinghez hasznalt fokmennyiseg egyik ill masik oldalra
closeDist = 12

def init():
	global redZoneX
	redZoneX = 0
	global greenZoneX
	greenZoneX = 0
	global blueZoneX
	blueZoneX = 0

KP = 0.01			#PID P
KI = 0.0001			#PID Integral
KD = 0.01			#PID Derivalt
SAMPLETIME = 0.5	#pid mintavetelezesi ido
TARGET = 255

sampleRate = 10		#median mintavetelezesi mennyiseg
proxMin = 12		#ultrahang minimum tavolsag
proxMax = 30		#ultrahang max tavolsag