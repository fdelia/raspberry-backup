from Adafruit_BME280 import *
from time import sleep, strftime
from gpiozero import LED

led = LED(21)


try:
  sensor = BME280(mode=BME280_OSAMPLE_8)

  degrees = sensor.read_temperature()
  pascals = sensor.read_pressure()
  hectopascals = pascals / 100
  humidity = sensor.read_humidity()

  print strftime("%Y.%m.%d %H:%M:%S") + '  {0:0.3f} , {1:0.3f} deg C , {2:0.2f} hPa , {3:0.2f} %'.format(sensor.t_fine, degrees, hectopascals, humidity)

#print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
#print 'Temp      = {0:0.3f} deg C'.format(degrees)
#print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
#print 'Humidity  = {0:0.2f} %'.format(humidity)
#print ' '
	
except:
  counter = 0
  while counter < 50:
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.3)
    counter += 1
