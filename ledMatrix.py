from gpiozero import LED
from time import sleep

led = {}
led[2] = LED(17)
led[3] = LED(24)
led[4] = LED(5)
led[5] = LED(13)
led[6] = LED(12)
led[7] = LED(25)
led[0] = LED(16)
led[1] = LED(20)
ledC = LED(6)

while True:
	for i in range(0, 8):
		if i%2 == 0: ledC.on()
		else: ledC.off()
		led[i].on()
		sleep(1)
		led[i].off()
		
