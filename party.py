from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=4, green=26, blue=19)
led2 = RGBLED(red=13, green=6, blue=5)
#led.red=1

time_delay = 0.01

def party():
  for n in range(100):
      #led.blue = n/100
      update((n/float(100), 1-n/float(100), 0))
      #led.color = color
      #led2.color = color
      sleep(time_delay)

  for n in range(100):
     update((1-n/float(100), 0, n/float(100)))
     sleep(time_delay)

  for n in range(100):
     update((0, n/float(100), 1-n/float(100)))
     sleep(time_delay)

def update(color):
     led.color = color
     led2.color = color

while True:
  party()
