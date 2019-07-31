#! usr/bin/env python

'''
 blob_detection.py: 
 Get blobs for min circles from a static image

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


# function definitions

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

# cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.namedWindow('image')
hough_output = img.copy()
contour_output = img.copy()
# grayscale version of jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
_, thresh = cv2.threshold(blur, 5, 255, cv2.THRESH_BINARY_INV)
dilated = cv2.dilate(thresh, None, iterations = 3)


# canny edge
edges = auto_canny(blur)

# detect circles in the image
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT, 1, 15, param1 = 130, param2 = 20, minRadius = 2, maxRadius =50 )
 
# detect contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



if circles is not None:
	circles = np.round(circles[0, :]).astype("int")

	# loop over (x,y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectabgle
		# corresponding to the center of the circle
		#cv2.circle(output, (x, y), r, (0, 255, 0), 1)
		cv2.rectangle(hough_output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), 1)
 
	# show the output image
	cv2.imshow("output", np.hstack([img, hough_output]))
	cv2.waitKey(0)
	cv2.destroyAllWindows()
if contours is not None:

	# min enclosing circle for contours
	contour_list = []
	for contour in contours:
		# (x, y), radius = cv2.minEnclosingCircle(contour)
		if cv2.contourArea(contour) < 10:
			continue
		
		contour_list.append(contour)
		
		# cv2.circle(contour_output, (int(x), int(y)), int(radius), (0, 0, 255), 1)

	# add contours to copy of img
	cv2.drawContours(contour_output, contour_list, -1, (0,255, 0), 1)
	cv2.imshow("contours", np.hstack([img, contour_output]))
	cv2.waitKey(0)
cv2.destroyAllWindows()
'''
while(1):
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF

	if(k == 27):
		break
'''