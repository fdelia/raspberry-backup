import json
import urllib2
import sys
from math import sin, cos, atan2, sqrt, radians, degrees
from gpiozero import LED
from time import sleep

led = {}
led[2] = LED(17)
led[3] = LED(24)
led[4] = LED(5)
led[5] = LED(13)
led[6] = LED(12)
led[7] = LED(25)
led[0] = LED(16) # should point to north
led[1] = LED(20)
ledC = LED(6)


# where I am
with open('ISSwhere_mycoords.json') as data_file:
	data = json.load(data_file)
LAT = data[0]
LON = data[1]

def get_distance_and_bearing():
	data = json.load(urllib2.urlopen("http://api.open-notify.org/iss-now.json"))
	iss_lat = data[u'iss_position'][u'latitude']
	iss_lon = data[u'iss_position'][u'longitude']
	message = data[u'message']
	print('iss position: ' + str(iss_lat) + ' , '+ str(iss_lon))
	# print (json.load(urllib2.urlopen("http://api.open-notify.org/iss-now.json"))[u'iss_position'])

	if not message == 'success':
		print("Server didn't respond with success")
		print("Data received:")
		print(data)
		sys.exit(0)

	# distance with haversine formula
	R = 6371 # approx radius of earth in kilometers

	lat1 = radians(LAT)
	lon1 = radians(LON)
	lat2 = radians(iss_lat)
	lon2 = radians(iss_lon)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	dist = R * c

	# bearing
	y = sin(lon2 - lon1) * cos(lat2)
	x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1)
	bear = degrees(atan2(y, x))

	print("bearing: " + str(bear))
	print("distance: " + str(dist))
	return bear, dist

# diection from 0 to 7, intensity from 0 to 5
def draw_leds(direction, intensity):
	# turn all leds off
	for i in range(0, 8):
		led[i].off()
	ledC.off()

	if intensity <= 0:
		# directional LED blinks slowly
		
		pass
	elif intensity == 1:
		# directional LED blinks normal
		pass
	elif intensity == 2: 
		# directional LED steady, center LED blinks slowly
		pass
	elif intensity == 3:
		# directional LED steady, center LED blinks normal
		pass
	elif intensity == 4:
		# directional and center LED steady
		pass
	elif intensity >= 5:
		# center LED steady
		pass


bear, dist = get_distance_and_bearing()

#bear -= 30 # leds north = east
bear = bear + 360 % 360
led_bear = (bear/45)

# 3000km = 5, 2400km = 4, etc.
led_dist = max(0, min(5, (dist / 600)))

print("LED bear: " + str(led_bear))
print("LED dist: " + str(led_dist))
# draw_leds(led_bear, 5 - led_dist)

