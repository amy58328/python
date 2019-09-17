import cv2
import numpy as np

# define range of skin color in HSV
lower_Hue = np.array([0, 43, 74], dtype=np.uint8)
upper_Hue = np.array([20, 255, 255], dtype=np.uint8)

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskskin = cv2.inRange(hsv, lower_Hue, upper_Hue)


    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    maskskin = cv2.erode(maskskin, kernel, iterations = 2)
    maskskin = cv2.dilate(maskskin, kernel, iterations = 2)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= maskskin)

    #  
    centerskin = None
    cnts = cv2.findContours(maskskin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        skin = max(cnts, key=cv2.contourArea)
        ((xskin, yskin), radius) = cv2.minEnclosingCircle(skin)
        M = cv2.moments(skin)
        xskin=int(M["m10"] / M["m00"]) 
        yskin=int(M["m01"] / M["m00"]) 
        centerskin = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])-200)
        if radius > 10:
            mode = False
            cv2.circle(frame, centerskin, 5, (0, 0, 255), -1)
    # 
    cv2.imshow('frame',frame)
    cv2.imshow('mask',maskskin)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break













cv2.destroyAllWindows()