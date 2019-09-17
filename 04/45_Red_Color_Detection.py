import cv2
import numpy as np

# lower mask (0-10) for Red color
lower_red1 = np.array([0,50,50])
upper_red1 = np.array([10,255,255])

# upper mask (170-180) for Red color
lower_red2 = np.array([170,50,50])
upper_red2 = np.array([180,255,255])


cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # join masks for Red color
    mask0 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask1 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask0

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()