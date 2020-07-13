import vlc
import socket
import serial
import time
import sys

# initialize timer
time_start = time.time()
seconds = 0
minutes = 0

# initialize variables related to rotary
numberDialed = ""
dialThreshold = 2

# initialize media variables
mediaList={}
mediaList["media"] = "./media/media.mov"
mediaList["shoulder"] = "./media/shoulder.mov"
mediaList["eyes"] = "./media/eyes.mov"
mediaList["fantasy"] = "https://olive-wren-8959.twil.io/assets/CR-2006-04_512kb.mp4"
mediaList["aeolian"] = "./media/Etude-Op25n1.flac"
mediaList["donttalk"] = "./media/donttalk.mp3"
mediaList[""]


mediaClip={}

vlcInstance = vlc.Instance("--input-repeat=65545","--no-video-title-show","--fullscreen")
player = vlcInstance.media_player_new()
player.set_fullscreen(True)
attractClip = vlcInstance.media_new(mediaList["media"])
shoulderClip = vlcInstance.media_new(mediaList["shoulder"])
eyesClip = vlcInstance.media_new(mediaList["eyes"])
fantasyClip = vlcInstance.media_new(mediaList["fantasy"])

mediaClip["00"] = attractClip
mediaClip["01"] = shoulderClip
mediaClip["02"] = eyesClip
mediaClip["03"] = fantasyClip

time.sleep(2)
player.set_media(mediaClip["00"])
time.sleep(1)
player.play()
time.sleep(0.2)


def getNumber(ser):
	line = ser.readline().decode('utf-8').rstrip()
	number = line
	return number

def playClip(number):
	print("Playing " + number)
	player.set_media(mediaClip[number])
	time.sleep(1)
	player.play()
	time.sleep(0.2)

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0', '9600', timeout=1)
	ser.flush()

	while True:
		if ser.in_waiting > 0 :
			rotaryOutput = getNumber(ser)
			print(rotaryOutput)
			numberDialed = numberDialed + rotaryOutput
		if len(numberDialed) == dialThreshold:
			print(numberDialed)
			playClip(numberDialed)
			numberDialed = ""