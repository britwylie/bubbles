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
_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)


params = cv2.SimpleBlobDetector_Params()

params.filterByColor = True
params.blobColor = 0
params.minThreshold = 10
params.maxThreshold = 200

## check opencv version and construct the detector
is_v2 = cv2.__version__.startswith("2.")
if is_v2:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(thresh)

# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(blob_out, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)

# wait for ESC key
cv2.waitKey(0)

cv2.destroyAllWindows()