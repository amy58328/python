import cv2
import numpy as np
import random
import pygame

def InsertLogo(i, j):
	if (j+rowsLogo < rowsFrame and i+colsLogo<colsFrame):
		roi = frame[j:j+rowsLogo, i:i+colsLogo]
		dst_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
		dst_fg = cv2.bitwise_and(img2,img2,mask = mask)
		dst = cv2.add(dst_bg,dst_fg)
		frame[j:j+rowsLogo, i:i+colsLogo] = dst


pygame.init()

img2 = cv2.imread('logo.png')
img2 = cv2.resize(img2, (100, 100)) 
rowsLogo,colsLogo,channelsLogo = img2.shape
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 5, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rowsFrame, colsFrame, channelsFrame = frame.shape

lower_blue = np.array([110, 50, 50], dtype=np.uint8)
upper_blue = np.array([130,255,255], dtype=np.uint8)

xLogo=random.randrange(1,colsFrame)
yLogo=random.randrange(1,rowsFrame)
n= 0 
number = 0
black = (255,255,255)

while(True):
	mode = True
	ret, frame = cap.read()
	frame=cv2.flip(frame,1)
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
	maskBlue = cv2.erode(maskBlue, kernel, iterations = 2)
	maskBlue = cv2.dilate(maskBlue, kernel, iterations = 2)
	cv2.imshow('maskBlue',maskBlue) 

	text = "your score:"
	cv2.putText(frame, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA) 
	# sprintf(test, "%d", number);
	test = str(number)
	cv2.putText(frame, test, (200, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 1, cv2.LINE_AA) 
	
	centerBlue = None
	cnts = cv2.findContours(maskBlue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((xBlue, yBlue), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		xBlue=int(M["m10"] / M["m00"])
		yBlue=int(M["m01"] / M["m00"])
		centerBlue = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		if radius > 10:
			mode = False
			cv2.circle(frame, centerBlue, 5, (0, 0, 255), -1)

	# Insert the first Logo
	if (mode == True):
		InsertLogo(xLogo, yLogo)
		# xLogo=xLogo+10
		# if (xLogo+colsLogo>colsFrame):
		# 	xLogo = 0
		n += 1
		if(n== 30):
			xLogo=random.randrange(colsLogo,colsFrame - colsLogo)
			yLogo=random.randrange(rowsLogo,rowsFrame - rowsLogo)
			n = 0
		# Show the result
		cv2.imshow('frame',frame)
	else:
		# InsertLogo(xBlue, yBlue)
		InsertLogo(xLogo, yLogo)
		if(xBlue > xLogo and xBlue < xLogo + colsLogo):
			if(yBlue > yLogo and yBlue < yLogo + rowsLogo):
				number += 1
				xLogo=random.randrange(colsLogo,colsFrame - colsLogo)
				yLogo=random.randrange(rowsLogo,rowsFrame - rowsLogo)
		cv2.imshow('frame',frame)

	print(number)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()