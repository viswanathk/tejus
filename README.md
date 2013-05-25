1) Install git
2) Clone the project
3) Install julius, julius-voxforge
4) Command for running julius : julius -input mic -C julius.jconf | python -u getcommand.py
5) Install festival
6) Install festlex-cmu
7) Install the downloaded voice file : 
	cd /usr/share/festival/voices/english/
	sudo wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
	sudo tar jxf cmu_us_clb_arctic-0.95-release.tar.bz2 
	sudo ln -s cmu_us_slt_arctic cmu_us_slt_arctic_clunits
	sudo cp /etc/festival.scm /etc/festival.scm.backup
	sudo echo "(set! voice_default 'voice_cmu_us_slt_arctic_clunits)" >> /etc/festival.scm
8) Install xbacklight for brightness control from terminal
9) Install zenity (for dialogs and such)
10) Notify osd is shit. Installed xfce4-notifyd-config. Removed notify-osd which killed ubuntu-desktop with itself
11) Installed Tornado for the webserver stuff. The commands are 
	after unzipping the package, python setup.py build
	sudo python setup.py install
12) Installed OpenCV
13) Installed python-opencv
14) Installed python-numpy
