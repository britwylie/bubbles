#! usr/bin/env python

'''
 hough_detection.py: 
 Locate bubbles from a static image using the hough circle detection algorithm
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

img = cv2.imread(args["image"])	
cv2.namedWindow('image')
hough_output = img.copy()

# grayscale version of jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)


_, thresh = cv2.threshold(gray, 145, 255, cv2.THRESH_BINARY_INV)
#test = cv2.equalizeHist(thresh)
laplac = cv2.Canny(thresh, 100, 200)
inv_laplac = cv2.bitwise_not(laplac)
erode = cv2.erode(inv_laplac, None, iterations = 1)
dilated = cv2.dilate(erode, None, iterations = 1)

im_floodfill = dilated.copy()
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = dilated.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);

cv2.imshow("Input Image to detector", im_floodfill)

cv2.imshow("Blurred", blur)
cv2.imshow("Dilated", dilated)
#cv2.imshow("test", test)
cv2.imshow("Threshold", thresh)
cv2.imshow("Laplacian", inv_laplac)
'''
# plot preprocessed images
fig, ax = plt.subplots(2, 2)
fig.subplots_adjust(hspace=0, wspace=0)

ax[0,0].imshow(blur, cmap = 'gray')
ax[0,0].set_title("Blurred")
ax[0,0].axis('off')

ax[0,1].imshow(gray, cmap = 'gray')
ax[0,1].set_title("Grayscale")
ax[0,1].axis('off')

ax[1,0].imshow(thresh, cmap = 'gray')
ax[1,0].set_title("Threshold")
ax[1,0].axis('off')

ax[1,1].imshow(dilated, cmap = 'gray')
ax[1,1].set_title("Dilated")
ax[1,1].axis('off')

plt.show()
'''
cv2.waitKey(0)

# detect circles in the image
circles = cv2.HoughCircles(im_floodfill,cv2.HOUGH_GRADIENT, 0.5, 5,\
 param1 = 70, param2 = 30, minRadius = 2, maxRadius = 10)


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