from Adafruit_BME280 import *
from time import sleep, strftime
from gpiozero import LED

led = LED(21) # red
#led2 = LED(20) # blue

# show if there is a human in the room
try:
  lines = []
  #with open("/home/pi/dev/LogTemp.log", "rb") as f:
  #  lines = f.readlines()

  inds = []
  for line in lines[-10:]:
    data = line.split(',')
    temp = data[1].strip().split(' ')[0]
    press = data[2].strip().split(' ')[0]
    hum = data[3].strip().split(' ')[0]
    #print(temp + ' ... ' + press + ' ... ' +hum)

    # measured rel. humidity - humidity (temp in F, pressure)
    ind = float(hum) - 1 / (float(temp)*9/5+32) * float(press)
    #ind = float(hum)/ float(temp)
    #print (ind)
    inds.append(ind)

  if inds[-1] > inds[-2] and inds[-2] > inds[-3] and inds[-3] > inds[-4]:
    counter = 0
    #while counter < 10:
      #led2.on()
      #sleep(0.5)
      #led2.off()
      #sleep(0.5)
      #counter += 1
except:
  pass


# print sensor data for log
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
	
except (RuntimeError, TypeError, NameError):
  counter = 0
  while counter < 50:
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.3)
    counter += 1



led.close()
#led2.close()
