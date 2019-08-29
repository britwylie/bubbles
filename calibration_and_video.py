'''
calibration_and_video.py: use to calibrate the video in a loop and retrieve a video for machine learning
on loop until satisfied
'''
__author__  =   "Brit W"
__project__ =   "bubbles"
__status__  =   "Published"


import numpy as np
from picamera.array import PiRGBArray
import picamera
import time
import sys
import imutils



# Edit this time length (in s) to give time to calibrate. 
# Program will NOT continue until this finishes. BE REASONABLE
PICTURE_WAIT = 5

# Save image to this file 
IMAG_LOC = '/home/pi/Documents/bubbles/imag.jpg'

# Edit this variable to set length of video
VIDEO_TIME = 30
FRAMERATE = 24
RESOLUTION = (640, 480)

# Save video to this file
VIDEO_LOC = 'test_video1.h264'


# Loop initialization
a = 1
camera = picamera.PiCamera()

while a == 1:
	# Take a picture
	camera.start_preview(fullscreen=False, window = (100, 20,640,480))
	time.sleep(PICTURE_WAIT)
	camera.capture(IMAG_LOC)
	camera.stop_preview()

	print("Picture taken")
	a = input("Press 1 to retake, 2 to take video, or any other key to quit: ")
	print("You typed: ", a)

	while a == 2:
		# Take a video for custom dataset
		camera.start_preview(fullscreen=False, window=(100,20,640,480))
		camera.resolution = RESOLUTION
		camera.framerate = FRAMERATE
		raw
		camera.start_recording('test_video1.h264')
		camera.wait_recording(VIDEO_TIME)
		camera.stop_recording()
		camera.stop_preview()
	
		print("Video taken")

		# Choose what to do next
		a = input("Retake? Press 1 for  pic, 2 for video, or any other key to exit: ")
		print("You typed: ", a)
	
	if a != 1:
		break

print('Done')