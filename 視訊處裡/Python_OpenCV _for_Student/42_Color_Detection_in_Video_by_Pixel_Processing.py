import numpy as np
import cv2
import math

refBlue = 255
refGreen = 0
refRed = 0

targetBlue = 0
targetGreen = 0
targetRed = 255

TH = 10

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

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rows,cols,channels = frame.shape

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    frame2=frame.copy()
    ColorDetection()

    cv2.imshow('Original',frame2)
    cv2.imshow('Color Detection',frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()