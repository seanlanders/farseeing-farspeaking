import vlc
import time
import socket

def handledata(data):
	data = data.decode() 
	return data

mediaList["media"] = "./media.mov"
mediaList["shoulder"] = "./shoulder.mov"
mediaList["eyes"] = "./eyes.mov"


def playClip(clip):
	player.set_media(clip)
	player.play()
	time.sleep(0.2)


attractMedia = "./media.mov"
shoulderMedia = "./shoulder.mov"
eyesMedia = "./eyes.mov"
vlcInstance = vlc.Instance("--input-repeat=65545","--no-video-title-show","--fullscreen")
player = vlcInstance.media_player_new()
player.set_fullscreen(True)
attractClip = vlcInstance.media_new(attractMedia)
shoulderClip = vlcInstance.media_new(shoulderMedia)
eyesClip = vlcInstance.media_new(eyesMedia)

time.sleep(2)
player.set_media(attractClip)
time.sleep(1)
player.play()
time.sleep(0.2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(4096)
    conn.close()
    playClip((data.decode()+"Clip"))