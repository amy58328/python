import cv2
import numpy as np

#Load two images
img = cv2.imread('fruits.jpg')
rows,cols,channels = img.shape

# BChannel Image by pixel processing 
bimg=img.copy()
for i in range(rows):
	for j in range(cols):
		bimg[i][j][1]=0
		bimg[i][j][2]=0
		
# gChannel Image by pixel processing 
gimg=img.copy()
for i in range(rows):
	for j in range(cols):
		bimg[i][j][0]=0
		bimg[i][j][2]=0
		
# gChannel Image by pixel processing 
rimg=img.copy()
for i in range(rows):
	for j in range(cols):
		bimg[i][j][0]=0
		bimg[i][j][1]=0

cv2.imshow('Original Image', img)
cv2.imshow('BChannel Image', bimg)
cv2.imshow('GChannel Image', gimg)
cv2.imshow('RChannel Image', rimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
