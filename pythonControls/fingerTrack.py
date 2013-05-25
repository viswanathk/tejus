#! /usr/bin/env python 
 
import cv2.cv as cv 
import os
import subprocess
 
color_tracker_window = "Color Tracker" 
 
class ColorTracker: 
	def __init__(self): 
		cv.NamedWindow( color_tracker_window, 1 ) 
		self.capture = cv.CaptureFromCAM(0) 
        
	def run(self): 
		lastx = lasty = -1
		left = right = 0
		while True: 
			img = cv.QueryFrame( self.capture ) 
			cv.Smooth(img, img, cv.CV_BLUR, 3); 
            
			hsv_img = cv.CreateImage(cv.GetSize(img), 8, 3) 
			cv.CvtColor(img, hsv_img, cv.CV_BGR2HSV) 
            
			thresholded_img =  cv.CreateImage(cv.GetSize(hsv_img), 8, 1) 
			cv.InRangeS(hsv_img, (35, 80, 80), (50, 255, 255), thresholded_img) 
			thresholded_img = cv.GetMat(thresholded_img)

            
			moments = cv.Moments(thresholded_img, 0) 
			area = cv.GetCentralMoment(moments, 0, 0) 
            
			if(area > 100000):
				x = int(round(cv.GetSpatialMoment(moments, 1, 0)/area ))
				y = int(round(cv.GetSpatialMoment(moments, 0, 1)/area ))
				if(lastx == -1):
					lastx = x
					lasty = y
				if( x - lastx < 0):
					os.system("totem --seek-fwd")
				elif(x - lastx > 0):
					os.system("totem --seek-bwd")
				lastx = x
				overlay = cv.CreateImage(cv.GetSize(img), 8, 3) 
				cv.Circle(overlay, (x, y), 2, (255, 255, 255), 20) 
				cv.Add(img, overlay, img) 
				cv.Merge(thresholded_img, None, None, None, img) 
			if cv.WaitKey(10) == 27: 
				break 
			cv.ShowImage(color_tracker_window, img) 
                
if __name__=="__main__": 
    color_tracker = ColorTracker() 
    color_tracker.run() 
