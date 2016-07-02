from gpiozero import RGBLED, Button
from time import sleep
from signal import pause

led = RGBLED(red=4, green=26, blue=19)

button = Button(23)
button2 = Button(18)



def someColor():
	led.color = (1,1,0)
#	print str(button.values)

button.when_pressed = someColor
button.when_released = led.off


def red():
	led.color = (1,0,0)

button2.when_pressed = red
button2.when_released = led.off

pause()
