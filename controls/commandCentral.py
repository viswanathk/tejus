import api
import os
from lxml import etree

while True:
	tree = etree.parse("config.xml")
	for element in tree.iter():
		if element.tag == "status":
			xmlspeech = element.text
		elif element.tag == "videoPause":
			xmlvideopause = element.text
		elif element.tag == "videoControl":
			xmlvideocontrol = element.text
		elif element.tag == "brightnessControl":
			xmlbrightnesscontrol = element.text
		elif element.tag == "systemLock":
			xmlsystemlock = element.text
	if xmlspeech == "on":
		os.system("./startSpeechRecognition")
	elif xmlspeech == "off":
		os.system("killall julius")
	if xmlvideopause == "on":
		
