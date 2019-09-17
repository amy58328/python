import numpy as np
import cv2
import sys

def nothing(x):
    pass

cap = cv2.VideoCapture(0)


cv2.namedWindow('BW')
cv2.createTrackbar('Trackbar1', 'BW', 127, 255, nothing)

cv2.namedWindow('Edge')
cv2.createTrackbar('Trackbar2', 'Edge', 100, 255, nothing)
cv2.createTrackbar('Trackbar3', 'Edge', 200, 255, nothing)




while True:
	ret, img = cap.read()
	cv2.imshow('Original', img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Gray', gray)
	thrs1 = cv2.getTrackbarPos('Trackbar1', 'BW')
	ret, balck_and_white= cv2.threshold(gray,thrs1,255,cv2.THRESH_BINARY)
	cv2.imshow('BW', balck_and_white)
	thrs2 = cv2.getTrackbarPos('Trackbar2', 'Edge')
	thrs3 = cv2.getTrackbarPos('Trackbar3', 'Edge')
	edge = cv2.Canny(gray, thrs2,thrs3)
	cv2.imshow('Edge', edge)
	ch = cv2.waitKey(5)
	if ch == 27:
		break

cv2.waitKey(0)
cv2.destroyAllWindows()
