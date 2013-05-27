#!/usr/bin/python
import sys
import api
from lxml import etree
from api import Data



def command(speech_object):
	while(True):
		tree = etree.parse("config.xml")
		for element in tree.iter():
			if element.tag == "status":
				xmlspeech = element.text
			elif element.tag == "songControl":
				xmlsong = element.text
			elif element.tag == "videoControl":
				xmlvideo = element.text
			elif element.tag == "systemControl":
				xmlsystem = element.text
			elif element.tag == "internetControl":
				xmlinternet = element.text
			elif element.tag == "brightnessControl":
				xmlbrightness = element.text
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			print com
			if xmlspeech == "on":
				if xmlsong == "on":
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
					if(com == "COMPLETE VOLUME"):
						userin = Data(["rhythmbox-client", "--set-volume", "1"],"Volume 100%")
						userin.interact()
					if(com == "ZERO VOLUME"):
						userin = Data(["rhythmbox-client", "--set-volume", "0"],"Volume 0%")
						userin.interact()

	
				if xmlvideo == "on":
					if(com == "RESUME VIDEO"):
						userin = Data(["totem","--play"],"Video play resumed")
						userin.interact()
					if(com == "STOP VIDEO"):
						userin = Data(["totem","--pause"],"Video play stopped")
						userin.interact()



				if xmlinternet == "on":
					if(com == "OPEN FOX"):
						userin = Data(["firefox"],"Opening firefox")
						userin.interact()
					if(com == "CHECK EMAIL"):
						userin = Data(["python", "/home/viswanath/dla/julius-grammer/imap.py"])
						userin.interact()


				if xmlbrightness == "on":
					if(com == "COMPLETE BRIGHTNESS"):
						userin = Data(["xbacklight", "-set", "100"],"Maximum brightness")
						userin.interact()
					if(com == "HALF BRIGHTNESS"):
						userin = Data(["/usr/bin/xbacklight", "-set", "50"],"Partial brightness")
						userin.interact()
					if(com == "ZERO BRIGHTNESS"):
						userin = Data(["/usr/bin/xbacklight","-set", "0"],"Minimal brightness")
						userin.interact()


				if xmlsystem == "on":
					if(com == "LOCK COMPUTER"):
						userin = Data(["gnome-screensaver-command","-l"],"Computer Locked",True)
						userin.interact()
					if(com == "TELL ME ABOUT"):
						userin = Data(["notify-send", "'Working progress'"],"Starting web service")
						userin.interact()

			if(com == "RESPOND"):
				currentstate = "Listening"
				if xmlspeech == "off":
					currentstate = "Not listening"
				userin = Data("",currentstate,True)
				userin.interact()
			if(com == "STOP LISTENING"):
				userin = Data("","Paused listening", True)
				userin.interact()
				xmlspeech = "off"
			if(com == "RESUME LISTENING"):
				userin = Data("","Started listening", True)
				userin.interact()
				xmlspeech = "on"

if __name__ == '__main__':
	try:
		command(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
