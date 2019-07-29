#! usr/bin/env python

'''
 tracking.py: 
 Code run on Raspberry Pi to track bubbles

 '''

__author__ = "Brit Wylie"
__version__ = "0.0.1"
__maintainer__ = "Brit Wylie"
__email__ = "bwylie@caltech.edu"
__status__ = "Started"

# packages
import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

# cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.namedWindow('image')
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3,3))

# detect circles in the image
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT, 1,15, param1 = 130, param2 = 20, minRadius = 2, maxRadius =50 )
 
ret, thresh = cv2.threshold(gray, 127, 255, 0)
image, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

imag = cv2.drawContours(imag, contours, -1, (0, 255, 0), 3)
cv2.imshow("imag", imag)

cv2.waitKey(0)


if circles is not None:
	circles = np.round(circles[0, :]).astype("int")

	# loop over (x,y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectabgle
		# corresponding to the center of the circle
		#cv2.circle(output, (x, y), r, (0, 255, 0), 1)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), 1)
 
	# show the output image
	cv2.imshow("output", np.hstack([img, output]))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

cv2.destroyAllWindows()
'''
while(1):
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF

	if(k == 27):
		break
'''