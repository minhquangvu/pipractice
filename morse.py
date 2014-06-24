import RPi.GPIO as GPIO, time

MPORT = 4
time_scale = 0.1


def initialize():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(MPORT, GPIO.OUT)

MorseTable = {
	'a' : '01',
	'b' : '1000',
	'c' : '1010',
	'd' : '011',
	'e' : '0',
	'f' : '1101',
	'u' : '001',
	'k' : '101',
	'l' : '1001'

}

def tit():
	GPIO.output(MPORT, True)
	time.sleep(time_scale)
	GPIO.output(MPORT, False)
	time.sleep(time_scale)

def te():
	GPIO.output(MPORT, True)
	time.sleep(2 * time_scale)
	GPIO.output(MPORT, False)
	time.sleep(time_scale)

def space():
	time.sleep(0.4)

def resolve_char(char):
	if char not in MorseTable:
		raise Exception ('Invalid character')
	sound_string = MorseTable[char]
	for one in sound_string:
		if one == '0':
			te()
		elif one == '1':
			tit()
		else:
			raise Exception('Invalid input')
	time.sleep(2 * time_scale)

def resolve_string(string):
	for one_char in string:
		resolve_char(one_char)

if __name__ == "__main__":	
	print 'running morse.py'
	initialize()
	string = 'fuck' + 'u'
	resolve_string(string)
