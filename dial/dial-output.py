import vlc
import socket
import serial
import time
import sys
import pygame

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
mediaList["onlyhaveeyes"] = "./media/onlyhaveeyes.mp3"

audioIndex = {}
mediaClip={}
audioClip={}

audioIndex["00"] = mediaList["aeolian"]
audioIndex["01"] = mediaList["donttalk"]
audioIndex["02"] = mediaList["onlyhaveeyes"]


playerInstance = vlc.Instance("--input-repeat=65545","--no-video-title-show")
#audioInstance = vlc.Instance("--input-repeat=65545","--no-video-title-show")
player = playerInstance.media_player_new()
player.set_fullscreen(True)
#audioPlayer = audioInstance.media_player_new()
attractClip = playerInstance.media_new(mediaList["media"])
shoulderClip = playerInstance.media_new(mediaList["shoulder"])
eyesClip = playerInstance.media_new(mediaList["eyes"])
fantasyClip = playerInstance.media_new(mediaList["fantasy"])
#aeolianClip = audioInstance.media_new(mediaList["aeolian"])
#donttalkClip = audioInstance.media_new(mediaList["donttalk"])
#onlyhaveeyesClip = audioInstance.media_new(mediaList["onlyhaveeyes"])


pygame.mixer.init()
pygame.mixer.music.load(audioIndex["00"])

mediaClip["00"] = attractClip
mediaClip["01"] = shoulderClip
mediaClip["02"] = eyesClip
mediaClip["03"] = fantasyClip
"""
audioClip["00"] = aeolianClip
audioClip["01"] = donttalkClip
audioClip["02"] = onlyhaveeyesClip
"""

time.sleep(2)
pygame.mixer.music.play()
player.set_media(mediaClip["00"])
#audioPlayer.set_media(mediaClip["00"])
time.sleep(1)
player.play()
#audioPlayer.play()
time.sleep(0.2)


def getNumber(ser):
	line = ser.readline().decode('utf-8').rstrip()
	number = line
	return number

def playClip(number):
	print("Playing " + number)
	player.set_media(mediaClip[number])
	#audioPlayer.set_media(audioClip[number])
	pygame.mixer.music.load(audioIndex[number])
	pygame.mixer.music.play()
	time.sleep(1)
	player.play()
	pygame.mixer.music.play()
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
			try:
				playClip(numberDialed)
			except:
				playClip("00")
			numberDialed = ""
