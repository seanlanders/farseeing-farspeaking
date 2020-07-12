import serial
import time
import sys

time_start = time.time()
seconds = 0
minutes = 0
phoneNumber = ""

def getNumber(ser):
	line = ser.readline().decode('utf-8').rstrip()
	number = line
	return number

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', '9600', timeout=1)
	ser.flush()

	while True:
		if ser.in_waiting > 0 :
			rotaryOutput = getNumber(ser)
			print(rotaryOutput)
			phoneNumber = phoneNumber + rotaryOutput
		if len(phoneNumber) == 7:
			print(phoneNumber)
			phoneNumber = ""
