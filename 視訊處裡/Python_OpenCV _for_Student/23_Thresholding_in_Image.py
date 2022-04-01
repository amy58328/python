import numpy as np
import cv2
import sys

#fn = sys.argv[1]

try:
	fn = sys.argv[1]
except IndexError:
	print("Need a file name.")
	exit(1)

img = cv2.imread(fn)

if img is None:
	print('Failed to load image file:', fn)
	#sys.exit(1)
	exit(1)

cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
ret, balck_and_white= cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow('BW', balck_and_white)

cv2.waitKey(0)
cv2.destroyAllWindows()