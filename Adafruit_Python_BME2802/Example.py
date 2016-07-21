from Adafruit_BME280 import *
from time import sleep
from gpiozero import RGBLED

sensor = BME280(mode=BME280_OSAMPLE_8)
led = RGBLED(red=4, green=26, blue=19)
start_temp = False
counter = 0

while True:
	degrees = sensor.read_temperature()
	pascals = sensor.read_pressure()
	hectopascals = pascals / 100
	humidity = sensor.read_humidity()

	print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
	print 'Temp      = {0:0.3f} deg C'.format(degrees)
	print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
	print 'Humidity  = {0:0.2f} %'.format(humidity)
	print ' '
	
	if not start_temp and counter>3: start_temp = degrees
        counter += 1

	diff_temp = max(0, min(1, (degrees-start_temp)))
        #print(diff_temp)
	led.color = (diff_temp, 0,1-diff_temp)

	sleep(0.02)
