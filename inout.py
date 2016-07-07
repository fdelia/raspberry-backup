import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO.setup(20, GPIO.OUT)
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#GPIO.output(20, True)
while True:
	print(GPIO.input(3))
#	time.sleep(0.3)
