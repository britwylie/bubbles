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
blur = cv2.GaussianBlur(gray, (5, 5), 0)
erode = cv2.erode(blur, None, iterations = 3)
dilated = cv2.dilate(erode, None, iterations = 3)
test = cv2.equalizeHist(dilated)



_, thresh = cv2.threshold(dilated, 127, 255, cv2.THRESH_BINARY)
laplac = cv2.Canny(gray, 100, 200)

cv2.imshow("Blurred", blur)
cv2.imshow("Dilated", dilated)
cv2.imshow("test", test)
cv2.imshow("Laplacian", laplac)
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
circles = cv2.HoughCircles(laplac,cv2.HOUGH_GRADIENT, 1, 15,\
 param1 = 130, param2 = 20, minRadius = 0, maxRadius =50)


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