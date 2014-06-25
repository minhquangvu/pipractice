import RPi.GPIO as GPIO
import time

pin = 17
refresh_period = 0.02
frequency=50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

pwm=GPIO.PWM(pin,frequency)

clockwise=0.75 #in second
anticlockwise=2.5
initial=(anticlockwise-clockwise)/2+clockwise

position=[clockwise,initial,anticlockwise,initial]

for run in xrange(3):
	for direction in position:
		msperiod=1000/frequency
		DutyCycle=100*direction/msperiod
		print ('Direction is: '),direction
		print ('DutyCycle is: '), DutyCycle
		print (' ')
		pwm.start(DutyCycle)
		time.sleep(1)
		
pwm.stop()
GPIO.cleanup()
		




