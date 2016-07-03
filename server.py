#!/usr/bin/python
from flask import Flask, render_template
from gpiozero import RGBLED
from time import sleep
import subprocess
import os, signal

#led = RGBLED(red=4, green=26, blue=19)
#led2 = RGBLED(red=13, green=6, blue=5)

app = Flask(__name__)
process = None

@app.route("/") 
def mypysite(name=None):
	return render_template("index.html")

@app.route("/party")
def party():
	global process
	#os.system("party.py")
	process = subprocess.Popen("python /home/pi/dev/party.py", shell=True)
	#process = Popen(['python', '/home/pi/dev/party.py'], stdout=PIPE, stderr=PIPE)
	return mypysite()

@app.route("/red")
def red():
#	led.red = 1
#	led2.red = 1
	return mypysite()

@app.route("/off")
def off():
	global process
#	led.off()
#	led2.off()
#	os.killpg(os.getpgid(process.pid), signel.SIGTERM)
	print ("off")
	print process
	process.terminate()
	os.kill(process.pid, signal.SIGINT)
	return mypysite()

if __name__ == "__main__":
	app.run(host="0.0.0.0")
