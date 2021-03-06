#! usr/bin/env python

'''
 video_detection.py: 
 Code run on test video to track bubbles

 Not as useful for this application, will be cannibalized and mixed with static_detection
'''

import cv2
import numpy as np

# checks for two contours too close together
def close(c1, list):
	(x, y), _ = cv2.minEnclosingCircle(c1)
	for contour in list:
		(xl, yl), _ = cv2.minEnclosingCircle(contour)
		if abs(xl - x ) < 5 or abs(yl - y) < 5:
			return True
	return False		

# computes boundaries for canny edge detection
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged
#def inside(c1, list):


# load stock video
cap = cv2.VideoCapture('blow.mp4')

# read the first two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()



while cap.isOpened():

	# edge detection method 1 	
	diff = cv2.absdiff(frame1, frame2)
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	_, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations = 3)
	
	# canny edge detection
	edges = auto_canny(blur)

	# contour detection
	contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# filter through contours to get circles
	contour_list = []
	lengths = []
	for contour in contours:

		# approxPolyDP method
		'''
		approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
		area = cv2.contourArea(contour)
		l = len(approx)
		if ((l > 8) & (area > 30)):
			lengths.append(l)
			(x, y), radius = cv2.minEnclosingCircle(contour)
			cv2.putText(frame1, "{}".format('Bubble'), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
			cv2.circle(frame1, (int(x), int(y)), int(radius), (0, 0, 255), 1)
		'''

		# min enclosing circle method

		(x, y), radius = cv2.minEnclosingCircle(contour)
		if cv2.contourArea(contour) < 200 or cv2.contourArea(contour) > 5000:
			continue
		elif close(contour, contour_list) == True:
			continue
		contour_list.append(contour)
		
		cv2.circle(frame1, (int(x), int(y)), int(radius), (0, 0, 255), 1)
		
	

	# draw all the contours over bubbles
	#cv2.drawContours(frame1, contour_list, -1, (0, 255, 0), 1)

	# display frame with contours
	cv2.imshow("feed", frame1)

	# compare next two frames
	frame1 = frame2
	ret, frame2 = cap.read()

	# press esc to close windows
	if cv2.waitKey(40) == 27:
		break

cv2.destroyAllWindows()