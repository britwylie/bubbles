'''
Set up for python 2.7 apparently
'''
__author__  =   "Brit W"
__project__ =   "bubbles"
__status__  =   "Practice only"


import numpy as np

from picamera.array import PiRGBArray
import picamera
import time
import sys
import imutils

a = 1
camera = picamera.PiCamera()

while a == 1:
	# Take a picture
	camera.start_preview(fullscreen=False, window = (100, 20,640,480))
	time.sleep(3)
	camera.capture('/home/pi/Documents/bubbles/imag.jpg')
	camera.stop_preview()
	print("Picture taken")
	a = input("Press 1 to retake, 2 to take video, or any other key to quit: ")
	print("You typed: ", a)
	while a == 2:
		# Take a video for custom dataset
		camera.start_preview(fullscreen=False, window=(100,20,640,480))
		camera.resolution = (640, 480)
		camera.start_recording('test_video.h264')
		camera.wait_recording(5)
		camera.stop_recording()
		camera.stop_preview()
	
		print("Video taken")

		# Choose what to do next
		a = input("Retake? Press 1 for  pic, 2 for video, or any other key to exit: ")
		print("You typed: ", a)
	
	if a != 1:
		break

print('Done')




