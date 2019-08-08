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

# cmd arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.namedWindow('image')


blob_out = img.copy()

# grayscale version of jpg
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)


erode = cv2.erode(blur, None, iterations = 1)
dil = cv2.dilate(erode, None, iterations = 1)

th, im_th = cv2.threshold(dil, 150,190, cv2.THRESH_BINARY_INV);

im_floodfill = cv2.equalizeHist(im_th.copy())

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
#_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Input Image to detector", im_floodfill)

params = cv2.SimpleBlobDetector_Params()

params.filterByColor = True
params.blobColor = 0

params.minThreshold = 30
params.maxThreshold = 200

params.minDistBetweenBlobs = 3

params.filterByArea = True
params.minArea = 1
params.maxArea = 10

params.filterByConvexity = False
params.minConvexity = 0.2

params.filterByCircularity = True
params.minCircularity = 0.1

params.filterByInertia = False

## check opencv version and construct the detector
is_v2 = cv2.__version__.startswith("2.")
if is_v2:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(im_floodfill)

# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(blob_out, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)

# wait for ESC key
cv2.waitKey(0)

cv2.destroyAllWindows()
