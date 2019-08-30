'''
lights.py: basic picture with three types of lighting

__author__ = "Brit W"
__email__ = "bwylie@caltech.edu"

'''

import time
import board
import neopixel
import numpy as np
import picamera
import sys
from picamera.array import PiRGBArray


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 29

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
ORDER = neopixel.GRB
PICTURE_WAIT = 5
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PICTURE_WAIT = 5
bright = 0.75

# Save image to this file 
IMAG_LOC = '/home/pi/Documents/bubbles/Images/blue.jpg'

# Edit this variable to set length of video
VIDEO_TIME = 30
FRAMERATE = 24
RESOLUTION = (640, 480)

# Save video to this file
VIDEO_LOC = 'Images/video.h264'


pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


def clear(num):
    pixels[num] = (0,0,0)
    pixels.show()
    print("Pixel ", num + 1, " has been cleared")
    
def clearAll():
    pixels.fill((0,0,0))
    pixels.show()
    print("All pixels cleared")
    
a = 1
camera = picamera.PiCamera()

try:
    while a == 1 :
        clearAll()

        color = WHITE
        #for i in range(8, 14):
        #    pixels[i] = color
        for i in range(27, 28):
            pixels[i] = tuple([int(bright*i) for i in color])
        #for i in range(16, 19):
        #    pixels[i] = tuple([int(bright*i) for i in color])
        pixels.show()
        
        camera.start_preview(fullscreen=False, window = (100, 20,640,480))
        time.sleep(PICTURE_WAIT)
        camera.capture(IMAG_LOC)
        camera.stop_preview()
        
        print("Picture taken")
        
        camera.start_preview(fullscreen=False, window=(100,20,640,480))
        camera.resolution = RESOLUTION
        camera.framerate = FRAMERATE
        
        camera.start_recording('test_video1.h264')
        camera.wait_recording(VIDEO_TIME)
        camera.stop_recording()
        camera.stop_preview()
        print("Video taken")

		# 
except KeyboardInterrupt:
    clearAll()

