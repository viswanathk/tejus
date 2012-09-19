import sys
import os
from subprocess import Popen, PIPE
def command(file_object):
	listen = 1
	while(True):
		line = file_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			print com
			# print len(com)
			if listen == 1:
				if(com == "VOLUME MUTE"):
					os.system("rhythmbox-client --set-volume 0")
					os.system("echo 'volume reduced' | festival --tts")
				if(com == "VOLUME FULL"):
					os.system("rhythmbox-client --set-volume 1")
					os.system("echo 'full volume' | festival --tts")
				if(com == "PLAY SONG"):
					os.system("rhythmbox-client --play")
					os.system("echo 'Playing songs' | festival --tts")
				if(com == "PAUSE SONG"):
					os.system("rhythmbox-client --pause")
					os.system("echo 'paused playing songs' | festival --tts")
				if(com == "NEXT SONG"):
					os.system("rhythmbox-client --next")
					os.system("echo 'playing next song' | festival --tts")
				if(com == "PREVIOUS SONG"):
					os.system("rhythmbox-client --previous")
					os.system("rhythmbox-client --previous")
					os.system("echo 'playing previous song' | festival --tts")
				if(com == "VOLUME DECREASE"):
					os.system("rhythmbox-client --volume-down")
					os.system("echo 'paused playing songs' | festival --tts")
				if(com == "VOLUME INCREASE"):
					os.system("rhythmbox-client --volume-up")
					os.system("echo 'paused playing songs' | festival --tts")
				if(com == "START VIDEO"):
					os.system("xte 'key Space'")
					os.system("echo 'started video' | festival --tts")
				if(com == "STOP VIDEO"):
					os.system("xte 'key Space'")
					os.system("echo 'paused video' | festival --tts")


				if(com == "LOCK COMPUTER"):
					os.system("gnome-screensaver-command -l")
					os.system("echo 'Bye sir i locked the computer' | festival --tts")
				if(com == "SHOW WINDOWS"):
					os.system("xte 'keydown Super_L' 'key w' 'keyup Super_L'")
					os.system("echo 'Displayed all windows'| festival --tts")
				if(com == "CLOSE WINDOW"):
					os.system("wmctrl -c :ACTIVE:")
				if(com == "OPEN COMPUTER"):
					os.system("gnome-screensaver-command -d")
					os.system("echo 'Unlocked the computer' | festival --tts")
				if(com == "OPEN MOVIES"):
					os.system("nautilus /media/Data/Videos/Movies")
					os.system("echo 'Opened movies' | festival --tts")
				if(com == "OPEN DOWNLOADS"):
					os.system("nautilus /home/viswanath/Downloads")
					os.system("echo 'Opened downloads' | festival --tts")
				if(com == "OPEN SERIES"):
					os.system("nautilus /media/Data/Series")
					os.system("echo 'Opened series' | festival --tts")
				if(com == "OPEN SHELL"):
					os.system("gnome-terminal")
					os.system("echo 'Opened terminal' | festival --tts")
				if(com == "OPEN FOX"):
					os.system("firefox &")
					os.system("echo 'Opened firefox' | festival --tts")
				if(com == "CHECK EMAIL"):
					os.system("python /home/viswanath/dla/julius-grammer/imap.py")
			if(com == "YOU RUNNING"):
				os.system("echo 'Yes sir i am running' | festival --tts")
			if(com == "STOP LISTENING"):
				listen = 0
				os.system("echo 'I wont listen anymore' | festival --tts")
			if(com == "RESUME LISTENING"):
				os.system("echo 'Started listening' | festival --tts")
				listen = 1
				
command(sys.stdin)
