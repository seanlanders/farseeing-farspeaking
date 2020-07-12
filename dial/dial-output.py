import serial

def getNumber(ser):
	line = ser.readline().decode('utf-8').rstrip()
	number = line
	return number

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', '9600', timeout=1)
	ser.flush()

	while True:
		if ser.in_waiting > 0 :
			getNumber(ser)