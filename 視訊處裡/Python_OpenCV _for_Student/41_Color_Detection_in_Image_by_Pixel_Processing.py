import numpy as np
import cv2
import math

refBlue = 0
refGreen = 0
refRed = 0

targetBlue = 0
targetGreen = 0
targetRed = 255

TH = 50

def Eucledian_Distance(b, g, r):
	return math.sqrt( (b-refBlue)*(b-refBlue) + (g-refGreen)*(g-refGreen) + (r-refRed)*(r-refRed))

def ColorDetection():
	for i in range(rows):
		for j in range(cols):
			error=Eucledian_Distance(frame[i][j][0],frame[i][j][1], frame[i][j][2]) 
			if error < TH:
				frame[i][j][0]=targetBlue
				frame[i][j][1]=targetGreen
				frame[i][j][2]=targetRed

frame = cv2.imread('sample.jpg')
rows,cols,channels = frame.shape
frame2=frame.copy()
ColorDetection()
cv2.imshow('Original',frame2)
cv2.imshow('Color Detection',frame)

cv2.waitKey(0)
cv2.destroyAllWindows()