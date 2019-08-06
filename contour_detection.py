#! usr/bin/env python

'''
 contour_detection.py: 
Detect contours in a static image with consistent lighting
 Preprocessing needs refine
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
import matplotlib.cm as cm
import matplotlib.image as mpimg


# cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# kernel for morphological transphormation
kernel = np.ones((3, 3), np.uint8)

img = cv2.imread(args["image"])	
cv2.namedWindow('image')
hough_output = img.copy()

# grayscale version of jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)


_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

laplac = cv2.Canny(thresh, 100, 200)
inv_laplac = cv2.bitwise_not(laplac)
erode = cv2.erode(inv_laplac, None, iterations = 1)
dilated = cv2.dilate(erode, None, iterations = 1)


closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

im_floodfill = dilated.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = dilated.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);

cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)
cv2.imshow("Threshold", thresh)

cv2.imshow("Input Image to detector", im_floodfill)
cv2.imshow("Closed holes", closed)


cv2.waitKey(0)

# contour creation

lower_bound = np.array([0,0,10])
upper_bound = np.array([255,255,195])

image = img

mask = cv2.inRange(img, lower_bound, upper_bound)

# mask = cv2.adaptiveThreshold(image_ori,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY_INV,33,2)

kernel = np.ones((3, 3), np.uint8)

# Use erosion and dilation combination to eliminate false positives. 
# In this case the text Q0X could be identified as circles but it is not.
mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=1)

closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[0]

if contours is not None:
	contours = sorted(contours, key=lambda x:cv2.contourArea(x))

	array = []
	ii = 1
	print(len(contours))
	for c in contours:
	    (x,y),r = cv2.minEnclosingCircle(c)
	    center = (int(x),int(y))
	    r = int(r)
	    if r >= 6 and r<=10:
	        cv2.circle(image,center,r,(0,255,0),2)
	        array.append(center)

	cv2.imshow("preprocessed", img)

cv2.waitKey(0)