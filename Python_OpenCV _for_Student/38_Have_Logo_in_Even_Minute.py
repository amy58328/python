from datetime import datetime
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
img=cv2.imread('logo2.png')
img=cv2.resize(img,(640,480))
row, col, para=img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

font=cv2.FONT_HERSHEY_SIMPLEX
while(True):
	ret, frame=cap.read()
	frame=cv2.resize(frame,(640,480))
	time=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	date=datetime.now().strftime('%M')
	if(int(date)%2==0):
		for i in range(row):
			for j in range(col):
				if(mask_inv[i][j]==255):
					frame[i][j]=img[i][j]
	cv2.putText(frame, time, (250,410),font,1,(0,0,255))
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.waitKey(0)
cv2.destroyAllWindows()