from gpiozero import RGBLED, Button
from time import sleep
from signal import pause

led = RGBLED(red=4, green=26, blue=19)

button = Button(23)
button2 = Button(18)

led.color = (0,0,0)

addRed = True
def moreRed():
	global addRed

	if addRed:
		led.red += 0.1
	else:
		led.red -= 0.1

	if led.red>=0.99:
		addRed = False
	if led.red<=0.01:
		addRed = True

button.when_pressed = moreRed

addBlue = True
def moreBlue():
	global addBlue

	if addBlue:
		led.blue += 0.1
	else:
		led.blue -= 0.1

	if led.blue>=0.99:
		addBlue = False
	if led.blue<=0.01:
		addBlue = True

button2.when_pressed = moreBlue

pause()
