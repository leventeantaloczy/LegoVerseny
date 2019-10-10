import time
import brickpi3
from constans import *
from mappingMovement import *


class PID:

	def go(self, motortPort_1, motortPort_2, degree, speed, BP):
		BP.reset_motor_encoder(BP.PORT_A)
		BP.reset_motor_encoder(BP.PORT_B)

		



		e1_prev_error = 0
		e2_prev_error = 0

		e1_sum_error = 0
		e2_sum_error = 0

		motor_1_sum = 0
		motor_2_sum = 0

		try:
			while(motor_1_sum <= degree and motor_2_sum <= degree):
				e1 = abs(BP.get_motor_encoder(motortPort_1))
				e2 = abs(BP.get_motor_encoder(motortPort_2))

				motor_1_sum += e1
				motor_2_sum += e2

				e1_error = TARGET - e1
				e2_error = TARGET - e2

				power_1 += (e1_error * KP) + (e1_prev_error * KD) + (e1_sum_error * KI)
				power_2 += (e2_error * KP) + (e2_prev_error * KD) + (e1_sum_error * KI)

				power_1 = max(min(100, power_1), 0)
				power_2 = max(min(100, power_2), 0)


				BP.set_motor_power(motortPort_1, -power_1 if power < 0 else power_1)
				BP.set_motor_power(motortPort_2, power_2 if power < 0 else power_1)

				print("e1 {} e2 {}".format(e1, e2))
				print("m1 {} m2 {}".format(power_1, power_2))


				BP.reset_motor_encoder(BP.PORT_A)
				BP.reset_motor_encoder(BP.PORT_B)

				time.sleep(SAMPLETIME)

				e1_prev_error = e1_error
				e2_prev_error = e2_error

				e1_sum_error += e1_error
				e2_sum_error += e2_error
			move.stopMotors(BP)
		except KeyboardInterrupt:
			BP.reset_all() 