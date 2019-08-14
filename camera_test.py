
'''camera_test.py: first test of camera on Raspberry Pi to determine focal length

__author__  =   "Brit W"
__project__ =   "bubbles"
__status__  =   "Practice only"


'''

import numpy as np
import cv2
from picamera.array import PiRGBArray
import picamera
import time
import sys
import imutils

a = "1"
camera = picamera.PiCamera()

while a == "1":
	# Take a picture
	camera.start_preview()
	time.sleep(30)
	camera.capture('/home/pi/Documents/bubbles/imag.jpg')
	camera.stop_preview()
	a = input("Press 1 to retake, 2 to take video, or any other key to quit: ")

	while a == "2":
		# Take a video for custom dataset
		camera.resolution = (640, 480)
		camera.start_recording('test_video.h264')
		camera.wait_recording(5)
		camera.stop_recording()

		# Choose what to do next
		a = input("Retake? Press 1 to take a picture, 2 to retake a video, or any other key to exit: ")

	else if a != "1":
		break

print('Done')




