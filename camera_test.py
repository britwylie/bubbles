
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

camera = picamera.PiCamera()

camera.start_preview()
time.sleep(500)
camera.capture('/home/pi/Documents/bubbles/imag.jpg')
camera.stop_preview()

camera.resolution = (640, 480)
camera.start_recording('test_video.h264')
camera.wait_recording(5)
camera.stop_recording()

print('Done')




