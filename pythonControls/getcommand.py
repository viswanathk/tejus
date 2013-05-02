#!/usr/bin/python
import sys
import api
from api import Data
def command(speech_object):
	listen = 1
	while(True):
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			print com
			if listen == 1:
				if(com == "RESUME SONG" or com == "OPEN SONG"):
					userin = Data(["rhythmbox-client","--play"],"Song playback resumed")
					userin.interact()
					api.songRunning = True
				if(com == "STOP SONG"):
					userin = Data(["rhythmbox-client","--pause"],"Song playback paused")
					userin.interact()
					api.songRunning = False
				if(com == "NEXT SONG"):
					userin = Data(["rhythmbox-client","--next"],"Playing next song")
					userin.interact()
				if(com == "PREVIOUS SONG"):
					userin = Data(["rhythmbox-client","--previous"],"Playing previous song")
					userin.interact()


				if(com == "RESUME VIDEO"):
					userin = Data(["totem","--play"],"Video play resumed")
					userin.interact()
				if(com == "STOP VIDEO"):
					userin = Data(["totem","--pause"],"Video play stopped")
					userin.interact()
				if(com == "FULLSCREEN VIDEO"):
					userin = Data(["totem","--fullscreen"],"Video made fullscreen")
					userin.interact()
				if(com == "COMPLETE VOLUME"):
					userin = Data(["rhythmbox-client", "--set-volume", "1"],"Volume 100%")
					userin.interact()
				if(com == "ZERO VOLUME"):
					userin = Data(["rhythmbox-client", "--set-volume", "0"],"Volume 0%")
					userin.interact()




				#if(com == "SHOW WINDOWS"):
					#userin.command("xte 'keydown Super_L' 'key w' 'keyup Super_L'")
					#userin.command("echo 'Displayed all windows'| festival --tts")
				#if(com == "CLOSE WINDOW"):
					#userin.command("wmctrl -c :ACTIVE:")


				#if(com == "OPEN MOVIES"):
					#userin.command = ["nautilus","/media/Data/Videos/Movies"]
					#userin.message = "opening movies"

				#if(com == "OPEN DOWNLOADS"):
					#userin.command= ["nautilus","/home/viswanath/Downloads"]

				#if(com == "OPEN SERIES"):
					#userin.command = ["nautilus", "/media/Data/Series"]




				if(com == "OPEN FOX"):
					userin = Data(["firefox"],"Opening firefox")
					userin.interact()
				if(com == "CHECK EMAIL"):
					userin = Data(["python", "/home/viswanath/dla/julius-grammer/imap.py"])
					userin.interact()
				if(com == "COMPLETE BRIGHTNESS"):
					userin = Data(["xbacklight", "-set", "100"],"Maximum brightness")
					userin.interact()
				if(com == "HALF BRIGHTNESS"):
					userin = Data(["/usr/bin/xbacklight", "-set", "50"],"Partial brightness")
					userin.interact()
				if(com == "ZERO BRIGHTNESS"):
					userin = Data(["/usr/bin/xbacklight","-set", "0"],"Minimal brightness")
					userin.interact()



				if(com == "LOCK COMPUTER"):
					userin = Data(["gnome-screensaver-command","-l"],"Computer Locked",True)
					userin.interact()
				if(com == "TELL ME ABOUT"):
					userin = Data(["notify-send", "'Working progress'"],"Starting web service")
					userin.interact()

			if(com == "RESPOND"):
				currentstate = "Listening"
				if listen == 0:
					currentstate = "Not listening"
				userin = Data("",currentstate,True)
				userin.interact()
			if(com == "STOP LISTENING"):
				userin = Data("","Paused listening", True)
				userin.interact()
				listen = 0
			if(com == "RESUME LISTENING"):
				userin = Data("","Started listening", True)
				userin.interact()
				listen = 1
command(sys.stdin)
