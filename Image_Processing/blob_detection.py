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
from datetime import datetime
import os

# cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.namedWindow('image')


blob_out = img.copy()

# grayscale version of jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)


erode = cv2.erode(blur, None, iterations = 2)
dil = cv2.dilate(erode, None, iterations = 2)

th, im_th = cv2.threshold(dil, 90, 245, cv2.THRESH_TOZERO)

im_floodfill = cv2.equalizeHist(im_th.copy())

_, next_trial = cv2.threshold(im_floodfill, 0, 254, cv2.THRESH_BINARY_INV)

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
#_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Input Image to detector", next_trial)

params = cv2.SimpleBlobDetector_Params()

params.filterByColor = True
params.blobColor = 0

params.minThreshold = 50
params.maxThreshold = 255

params.minDistBetweenBlobs = 5

params.filterByArea = True
params.minArea = 5
params.maxArea = 300

params.filterByConvexity = True
params.minConvexity = 0

params.filterByCircularity = True
params.minCircularity = 0.1

params.filterByInertia = False

## check opencv version and construct the detector
is_v2 = cv2.__version__.startswith("2.")
if is_v2:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(next_trial)

# Count the number of circles
total_count = 0
for i in keypoints:
	total_count = total_count + 1

# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(blob_out, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Uncomment to create filled blue bubbles instead of red circles
#for x in range(1,len(keypoints)):
#  im_with_keypoints =cv2.circle(img, (np.int(keypoints[x].pt[0]),np.int(keypoints[x].pt[1])), radius=np.int(keypoints[x].size), color=(255, 0, 0), thickness=-1)

# write some text
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerofText = (10, 1000)
fontScale              = 3
fontColor              = (255, 255, 255)
lineType               = 5

cv2.putText(im_with_keypoints, '{} Bubbles found'.format(str(total_count)), bottomLeftCornerofText, font, fontScale, fontColor, lineType)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)

location = "blob_detect_{}.JPG".format(f'{datetime.now():%Y-%m-%d_%H:%M:%S%z}')
print(location)

if not cv2.imwrite(os.path.join(os.path.expanduser('~'),'Desktop','blob_detect.png'.format(f'{datetime.now():%Y-%m-%d_%H:%M:%S%z}')), im_with_keypoints):

	raise Exception("Could not write image")
# wait for ESC key


cv2.waitKey(0)

cv2.destroyAllWindows()
