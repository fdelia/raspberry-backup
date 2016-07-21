import forecastio
import datetime

from gpiozero import RGBLED, Button
from time import sleep
from signal import pause
from math import pow

# https://developer.forecast.io/docs/v2#forecast_call

led = RGBLED(red=4, green=26, blue=19)
#led2 = RGBLED(red=13, green=6, blue=5)

button = Button(18)
button2 = Button(23)
led.off()

api_key = "9c09fe99666a61bbd85aa2743387cd31"
lat = 47.3769
lng = 8.5417


def nextHours(hours):
	if led.is_lit:
		led.off()
		led2.off()
		return

	# till the forecast is loaded
	led.color = (0.2,0.2,0.2)
	led2.color = (0.2,0.2,0.2)

	forecast = forecastio.load_forecast(api_key, lat, lng)
	hourly_data = forecast.hourly().data
	print "next " + str(hours) + " hours"
	now = datetime.datetime.now()

	avg_temp = 0
	max_precip = 0
	for d in hourly_data:
		if d.time - now > datetime.timedelta(0, 0, 0) and d.time - now < datetime.timedelta(0, hours*60*60, 0):
			print str(d.time) + ' : '+str(d.apparentTemperature) + ' / ' +str(d.temperature) +'  ,  ' + str(d.precipProbability)
			avg_temp += d.apparentTemperature
			max_precip = max(d.precipProbability, max_precip)

	avg_temp /= hours

	print "avg temp: " + str(avg_temp)
	print "max precip: " + str(max_precip)

	# the temp is colder than swiss meteo, correct:
	avg_temp += 1

	# 15 deg is cold, 27 is warm -- for now, add monthly averages later
	avg_temp -= 15
	avg_temp /= 12
	avg_temp = max(0, min(1, avg_temp))
	# the red color is too weak, make it a bit exponential
	#avg_temp = pow(avg_temp, 0.75)

	max_precip = max(0, min(1, max_precip))
	# make it a bit exponential, else the color shows too early
	max_precip = pow(max_precip, 1.5)	

	print "temp indicator: " + str(avg_temp)	
	print "precip indicator: " + str(max_precip)

	led.color = (avg_temp, max_precip, 1-avg_temp)
	led2.color = (avg_temp, max_precip, 1-avg_temp)

def sixHours():
	nextHours(6)

def twelfeHours():
	nextHours(12)


button.when_pressed = sixHours
button2.when_pressed = twelfeHours


pause()
