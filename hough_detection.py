#! usr/bin/env python

'''
 hough_detection.py: 
 Locate bubbles from a static image using the hough circle algorithm

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
hough_output = img.copy()

# grayscale version of jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
dilated = cv2.dilate(thresh, None, iterations = 3)



# detect circles in the image
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT, 1, 15,\
 param1 = 130, param2 = 20, minRadius = 2, maxRadius =50 )


if circles is not None:
	circles = np.round(circles[0, :]).astype("int")

	# loop over (x,y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectabgle
		# corresponding to the center of the circle
		cv2.circle(hough_output, (x,  y), r, (0, 255, 0), 1)
		cv2.rectangle(hough_output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), 1)

	# show the output image
	cv2.imshow("output", np.hstack([img, hough_output]))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

cv2.destroyAllWindows()