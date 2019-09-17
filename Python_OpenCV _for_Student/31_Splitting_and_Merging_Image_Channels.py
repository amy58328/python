import cv2
import numpy as np

#Load two images
img1 = cv2.imread('fruits.jpg')
print(img1.shape)
b,g,r = cv2.split(img1)
print(b.shape)
img2 = cv2.merge((r,b,g))
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('b', b)

b[:] = 0
cv2.imshow('b0', b)

z= np.zeros(b.shape, np.uint8)
gChannel=cv2.merge((b, g, z))
cv2.imshow('gChannel', gChannel)

cv2.waitKey(0)
cv2.destroyAllWindows()
