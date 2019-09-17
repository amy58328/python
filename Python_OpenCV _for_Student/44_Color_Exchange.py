# Change blue color to yellow color
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
yellow = np.full(frame.shape, (0, 255,255), dtype=np.uint8)
    
# define range of blue color in HSV
lower_blue = np.array([110, 50, 50], dtype=np.uint8)
upper_blue = np.array([150,255,255], dtype=np.uint8)

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations = 2)
    mask = cv2.dilate(mask, kernel, iterations = 2)
    mask_inv = cv2.bitwise_not(mask)
    # Bitwise-AND mask and original image
    fg = cv2.bitwise_and(yellow,yellow, mask= mask)
    bg = cv2.bitwise_and(frame, frame, mask= mask_inv)
    final = cv2.add(fg, bg)
    cv2.imshow('frame',frame)
    cv2.imshow('final',final)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()