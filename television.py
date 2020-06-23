import vlc
import time
import socket

def handledata(data):
	data = data.decode()
	return data

mediaList={}
mediaList["media"] = "./media/media.mov"
mediaList["shoulder"] = "./media/shoulder.mov"
mediaList["eyes"] = "./media/eyes.mov"
mediaList["fantasy"] = "https://olive-wren-8959.twil.io/assets/CR-2006-04_512kb.mp4"

mediaClip={}

vlcInstance = vlc.Instance("--input-repeat=65545","--no-video-title-show","--fullscreen")
player = vlcInstance.media_player_new()
player.set_fullscreen(True)
attractClip = vlcInstance.media_new(mediaList["media"])
shoulderClip = vlcInstance.media_new(mediaList["shoulder"])
eyesClip = vlcInstance.media_new(mediaList["eyes"])
fantasyClip = vlcInstance.media_new(mediaList["fantasy"])

mediaClip["attract"] = attractClip
mediaClip["shoulder"] = shoulderClip
mediaClip["eyes"] = eyesClip
mediaClip["fantasy"] = fantasyClip

time.sleep(2)
player.set_media(mediaClip["attract"])
time.sleep(1)
player.play()
time.sleep(0.2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 10001))
s.listen(1)

def playClip(clip):
	print("Playing " + clip)
	player.set_media(mediaClip[clip])
	time.sleep(1)
	player.play()
	time.sleep(0.2)

while True:
    print("Waiting for data")
    conn, addr = s.accept()
    data = conn.recv(4096)
    print("data recieved")
    conn.close()
    print(data.decode())
    clipName = data.decode()
    print(clipName)
    playClip(clipName)
"""    time.sleep(2)
    player.set_media(mediaClip[clipName])
    time.sleep(1)
    player.play()
    time.sleep(0.2)"""