import numpy as np
import cv2
import sys

def nothing(x):
	pass

fn = sys.argv[1]

img = cv2.imread(fn)

if img is None:
	print('Failed to load image file:', fn)
	sys.exit(1)

cv2.imshow('Original', img)

cv2.namedWindow('BW')
cv2.createTrackbar('Trackbar1', 'BW', 100, 255, nothing)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

while True:
	thrs1 = cv2.getTrackbarPos('Trackbar1', 'BW')
	ret, balck_and_white= cv2.threshold(gray,thrs1,255,cv2.THRESH_BINARY)
	cv2.imshow('BW', balck_and_white)
	ch = cv2.waitKey(5)
	if ch == 27:
		break

cv2.waitKey(0)
cv2.destroyAllWindows()
