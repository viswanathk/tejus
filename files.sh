echo "Welcome. I will help you with your session today"
if [ `date +%H` -gt 12 ] && [ `date +%H` -lt 20 ]; then
	echo "Good afternoon" | festival --tts
elif [ `date +%H` -lt 12 ]; then
	echo "Good morning" | festival --tts
else
	echo "Good night" | festival --tts
fi
while true; do
read inp

#code
if [ "$inp" = "code" ]; then
	echo "Started your coding session" | festival --tts
	terminator -f --working-directory=~/code > /dev/null &
	clear
	key=`ps -e|grep rhythmbox`
	echo $key
	if [ -z "$key" ]; then
	 	rhythmbox-client --play
	fi
fi
#code

#system management
key=`echo $inp|grep "install"`
if [ -n "$key" ]; then
	echo "Application is installing. Please wait." | festival --tts
	sudo apt-get $inp
	echo "Installed." | festival --tts
fi
key=`echo $inp|grep "bye"`
if [ -n "$key" ]; then
	echo "Bye sir. I am locking the computer" | festival --tts
	gnome-screensaver-command -l
fi
key=`echo $inp|grep "sleepy"`
if [ -n "$key" ]; then
	echo "Do you want me to shutdown the computer sir" | festival --tts
	read ans
	if [ "$ans" = "ok" ] || [ "$ans" = "yes" ]; then
		echo "Please save your work sir. I will shutdown the computer in 10 seconds" | festival --tts
		sleep 10
		echo "System going down" | festival --tts
		poweroff
	else
		echo "Should I lock the computer sir" | festival --tts
		read ans
		if [ "$ans" = "ok" ] || [ "$ans" = "yes" ]; then
			gnome-screensaver-command -l
		else
			echo "Drink some water and continue your work sir" | festival --tts
		fi
	fi
fi
if [ "$inp" = "sysinfo" ]; then
key=`apt-get --no-act upgrade|grep -e "[0-9][0-9] upgraded"`
if [ -n "$key" ]; then
	echo $key|festival --tts
fi
fi
if [ "$inp" = "clean my desktop" ]; then
	echo "Cleaning your desktop" | festival --tts
	mv ~/Desktop/* ~/random/
	echo "moved the contents to random folder" | festival --tts
fi
#system management

#utilities
if [ "$inp" = "clear" ]; then
	clear
	echo "Cleared the screen" | festival --tts
fi
if [ "$inp" = "timenow" ]; then
	echo "Time is `date +%H` `date +%M`"|festival --tts
fi
if [ "$inp" = "day" ]; then
	echo "Today is `date +%A` sir."|festival --tts
fi
if [ "$inp" = "dude?" ]; then
	echo "Tell me"|festival --tts
fi
if [ "$inp" = "cleanup" ]; then
	echo "Cleaning up some ram"|festival --tts
	sudo killall apache2
	sudo killall vlc
	sudo killall firefox
	sudo killall virtualbox
	sudo killall rhythmbox
fi
#utilities ending

#file manager
if [ "$inp" = "explore" ]; then
	nautilus
	echo "Start exploring."|festival --tts
fi
if [ "$inp" = "data" ]; then
	nautilus /media/Data
	echo "Start exploring."|festival --tts
fi
if [ "$inp" = "private" ]; then
	nautilus /etc/notifs
	echo "Is no one around you?."|festival --tts
fi
if [ "$inp" = "movies" ]; then
	nautilus /media/Data/Videos/Movies
	echo "Opening movies. You wont practise programming?"|festival --tts
fi
#filemanager

#fun
if [ "$inp" = "hide" ]; then
	animate ~/Pictures/*.jpg
fi
key=`echo $inp | grep "bored"`
if [ -n "$key" ]; then
	echo "Do you want to play some games?" | festival --tts
	read response
	if [ "$response" = "y" ] || [ "$response" = "yes" ]; then
		games=`ls /usr/games`
		echo "You have the following games" | festival --tts
		for game in `ls /usr/games`; do
			echo $game | festival --tts
		done
	else
		echo "How about some movies?" | festival --tts
		read response
		if [ "$response" = "y" ] || [ "$response" = "yes" ] || [ "$response" = "ok" ]; then
		nautilus /media/Data/Videos/Movies

		else
			echo "How about series?" | festival --tts
			read response
			if [ "$response" = "y" ] || [ "$response" = "yes" ] || [ "$response" = "ok" ]; then
				nautilus /media/Data/Series
			else
				echo "I am sorry. I don't have anything else to offer you." | festival --tts
			fi

		fi
		
	fi
fi


#/fun


#internet 
if [ "$inp" = "facebook" ]; then
	firefox www.facebook.com
	echo "Facebook is a waste of your time" | festival --tts
fi
if [ "$inp" = "gmail" ]; then
	firefox www.gmail.com
	echo "Opening gmail" | festival --tts
fi
if [ "$inp" = "google" ]; then
	echo "What do you want to search sir?"|festival --tts
	read search
	search=`echo $search|sed s/\ /+/`
	firefox www.google.com/search?q=$search
	echo "Is this what you are looking for?"|festival --tts
fi
if [ "$inp" = "checkmail" ]; then
	echo "Opening gmail" | festival --tts
	python imap.py | festival --tts
fi
if [ "$inp" = "ffprivate" ]; then
	firefox -private &
	echo "Watching porn are we sir?" | festival --tts
fi

#/internet

#this part is for the media control

if [ "$inp" = "nextsong" ]; then
	rhythmbox-client --next
	echo  "Playing song `rhythmbox-client --print-playing-format=%tt`"|festival --tts
fi
if [ "$inp" = "nextsongs" ]; then
	iter=1
	while [ $iter -le 6 ]; do
		rhythmbox-client --next
		iter=`expr "$iter" "+" 1`
	done
	echo "Skipping 6 songs..." | festival --tts
fi
if [ "$inp" = "prevsong" ]; then
	rhythmbox-client --previous
	rhythmbox-client --previous
	echo "Playing the last song..." | festival --tts
fi
if [ "$inp" = "pause" ]; then
	rhythmbox-client --pause
	echo "Playlist paused..." | festival --tts
fi
if [ "$inp" = "play" ]; then
	rhythmbox-client --play
	echo "Playlist started..." | festival --tts
fi
if [ "$inp" = "fullvolume" ]; then
	echo "Full volume!"|festival --tts
	rhythmbox-client --set-volume 1
fi
if [ "$inp" = "down" ]; then
	echo  "Reducing volume"|festival --tts
	rhythmbox-client --volume-down 
fi
if [ "$inp" = "down!" ]; then
	echo  "Reducing volume"|festival --tts
	down=1
	while [ "$down" -le 3 ]; do
		rhythmbox-client --volume-down
		down=`expr "$down" "+" 1`
	done
fi
if [ "$inp" = "up" ]; then
	echo  "Increasing volume"|festival --tts
	rhythmbox-client --volume-up
fi
if [ "$inp" = "up!" ]; then
	echo  "Increasing volume"|festival --tts
	up=1
	while [ "$up" -le 3 ]; do
		rhythmbox-client --volume-up
		up=`expr "$up" "+" 1`
	done
fi
if [ "$inp" = "songinfo" ]; then
	rhythmbox-client --pause
	echo  "`rhythmbox-client --print-playing-format=%tt`"|festival --tts
	rhythmbox-client --play
fi
if [ "$inp" = "mute" ]; then
	echo  "Muting volume"|festival --tts
	down=1
	while [ "$down" -le 10 ]; do
		rhythmbox-client --volume-down
		down=`expr "$down" "+" 1`
	done
	echo  "Muted"|festival --tts
fi

#media finished
done
