import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import numpy as np
from datetime import datetime, timedelta
import time
import math
import os
path = os.path.dirname(os.path.realpath(__file__))

dates = []
times = []
datetimes = []
temps = []
presses = []
hums = []
inds = []


filename = '/LogTemp.log'

# getting rid of NUL bytes
fi = open(path+filename, 'rb')
data = fi.read()
fi.close()
fo = open(path+filename, 'wb')
fo.write(data.replace('\x00', ''))
fo.close()

MULTIPLE_DAYS = False



f = open(path+filename, 'rb') 
reader = csv.reader(f) 

for row in reader: 
	# print row
	date, hour, _, clock_time = 	row[0].strip().split(' ')
	temp, _, _ = row[1].strip().split(' ')
	press, _ = row[2].strip().split(' ')
	hum, _ = row[3].strip().split(' ')


	dt = time.strptime(date + ' ' + hour, '%Y.%m.%d %H:%M:%S')
	if MULTIPLE_DAYS: delta = timedelta(days=100)
	else: delta = timedelta(days=1)
	# if datetime.now() - datetime.fromtimestamp(time.mktime(dt)) < timedelta(days=100):
	if datetime.now() - datetime.fromtimestamp(time.mktime(dt)) < delta:
		dates.append(date)
		Y, M, D = date.split('.')
		h, m, s = hour.split(':')

		if MULTIPLE_DAYS: times.append(float(D) + float(h)/24 + float(m)/24/60)
		else: times.append(float(h) + float(m) / 60)

		datetimes.append(dt)
		temps.append(temp)
		presses.append(press)
		hums.append(hum)

		# measured humidity - humidity (temp, pressure)
		inds.append(float(hum)*0 + 1 / (float(temp)*9/5+32) * float(press))


if MULTIPLE_DAYS:
	xFrom = 7
	xTo = 19
else:
	xFrom = 0
	xTo = 24
xTicks = 1

fig = plt.figure(facecolor='white')
# plt.title('Measurement of temp, press and hum')
plt.subplot(311)
plt.axis([xFrom, xTo, float(min(temps)) - 0.3, float(max(temps)) + 0.3])
plt.xticks(np.arange(xFrom, xTo, xTicks))
# ax.xaxis.set_major_locator(DayLocator())
# ax.xaxis.set_minor_locator(HourLocator(arange(0, 25, 6)))
# ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.grid(True)
# plt.xlabel('Hour')
plt.ylabel('Temp [C]')
# d = matplotlib.dates.date2num(datetimes)
plt.plot(times, temps, 'r.')

plt.subplot(312)
plt.axis([xFrom, xTo, float(min(hums)) - 0.5, float(max(hums)) + 0.5])
plt.xticks(np.arange(xFrom, xTo, xTicks))
plt.grid(True)
plt.ylabel('rel. Hum [%]')
plt.plot(times, hums, 'b.')

plt.subplot(313)
plt.axis([xFrom, xTo, float(min(presses)) - 0.5, float(max(presses)) + 0.5])
plt.xticks(np.arange(xFrom, xTo, xTicks))
plt.grid(True)
# plt.xlabel('Date')
plt.ylabel('Pressure [hPa]')
plt.plot(times, presses, 'g.')

# plt.subplot(414)
# plt.axis([xFrom, xTo, float(min(inds)) - 0.1, float(max(inds)) + 0.1])
# plt.xticks(np.arange(xFrom, xTo, xTicks))
# plt.grid(True)
# plt.xlabel('Date')
# plt.ylabel('index classifier')
# plt.plot(times, inds, 'y.')


# plt.show()
plt.savefig('/home/pi/server/public/plot.png', dpi=300)
