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


def playClip(clip):
	print("Playing " + clipName)
	player.set_media(clip)
	time.sleep(1)
	player.play()
	time.sleep(0.2)

vlcInstance = vlc.Instance("--input-repeat=65545","--no-video-title-show","--fullscreen")
player = vlcInstance.media_player_new()
player.set_fullscreen(True)
attractClip = vlcInstance.media_new(mediaList["media"])
shoulderClip = vlcInstance.media_new(mediaList["shoulder"])
eyesClip = vlcInstance.media_new(mediaList["eyes"])

time.sleep(2)
player.set_media(attractClip)
time.sleep(1)
player.play()
time.sleep(0.2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 10001))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(4096)
    conn.close()
    print(data.decode())
    clipName = data.decode() + "Clip"
    playClip(clipName)
