#! usr/bin/env python

'''
 video_detection.py: 
 Code run on test video to track bubbles
'''

import cv2
import numpy as np


# load stock video
cap = cv2.VideoCapture('blow.mp4')

# read the first two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
	diff = cv2.absdiff(frame1, frame2)
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations = 3)
	contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	'''
	for contour in contours:
		(x, y), radius = cv2.minEnclosingCircle(contour)
		if cv2.contourArea(contour) < 700:
			continue
		cv2.circle(frame1, (int(x), int(y)), int(radius), (0, 0, 255), 1)
		cv2.putText(frame1, "Status: {}".format('Bubble'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
	'''

	#draw all the contours over bubbles
	cv2.drawContours(frame1, contours, -1, (0, 255, 0), 1)

	# display frame with contours
	cv2.imshow("feed", frame1)

	# compare next two frames
	frame1 = frame2
	ret, frame2 = cap.read()

	# press esc to close windows
	if cv2.waitKey(40) == 27:
		break

cv2.destroyAllWindows()