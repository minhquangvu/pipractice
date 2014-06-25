import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Red=17
Green=18
Blue=22
LED=[Red,Green,Blue]

for port in LED:
	GPIO.setup(port,GPIO.OUT)

for port in LED:	
	GPIO.output(port,False)
		
colorcode={
	'r':'1',
	'g':'3',
	'b':'4',
}

def red():
	GPIO.output(Red,True)
	time.sleep(1)
	GPIO.output(Red,False)
	time.sleep(1)
	
def green():
	GPIO.output(Green,True)
	time.sleep(1)
	GPIO.output(Green,False)
	time.sleep(1)

def blue():
	GPIO.output(Blue,True)
	time.sleep(1)
	GPIO.output(Blue,False)
	time.sleep(1)
	
def resolve_colorcode(char):
	"code light"
	sequence=colorcode[char]
	for light in sequence:
		if light is '1':
			red()
		elif light is '3':
			green()
		elif light is '4':
			blue()
			
def resolve_lightup(string):
	"read string"
	for one in string:
			resolve_colorcode[one]
			
if __name__ == "__main__":	
	print 'running LED'
	string=raw_input('Enter your string: ')
	resolve_lightup(string)			
