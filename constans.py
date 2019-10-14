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
greenZoneX = 5		#zold -||-
blueZoneX = 8		#kek -||-

speed = -65				#altalanos sebesseg, matrix beolvasaskor es utvonal kereseskor is
turnSpeed = 80			#kerekek fizkai elfordulasanak sebessege
wheelRotateDegree = 910 #egy matrix mezo oldalanak hossza
turnTime = 0.8									#800 - 6.4 cm #850 az ideal
waitSecs = 0.4		#altalanos varakozasi ido
rampDown = 150		#matrix beolvasasnal lassitas hossza
glassTrace = 400	#tracinghez hasznalt fokmennyiseg egyik ill masik oldalra
closeDist = 12

KP = 0.01			#PID P
KI = 0.0001			#PID Integral
KD = 0.01			#PID Derivalt
SAMPLETIME = 0.5	#pid mintavetelezesi ido
TARGET = 255

sampleRate = 10		#median mintavetelezesi mennyiseg
proxMin = 12		#ultrahang minimum tavolsag
proxMax = 30		#ultrahang max tavolsag