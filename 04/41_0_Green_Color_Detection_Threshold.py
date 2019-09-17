import cv2
import numpy as np

refBlue = 0
refGreen = 255
refRed = 0

targetBlue = 0
targetGreen = 0
targetRed = 255

TH=20

def nothing(x):
	pass

# define range of the referenced color in HSV
refBGR=np.uint8([[[refBlue,refGreen,refRed ]]])
refHSV = cv2.cvtColor(refBGR,cv2.COLOR_BGR2HSV)
refHue= refHSV[0][0][0]
print(refHSV[0][0][0], refHSV[0][0][1], refHSV[0][0][2])

lower_Hue = np.array([refHue-TH, 50, 50], dtype=np.uint8)
upper_Hue = np.array([refHue+TH,255,255], dtype=np.uint8)

cap = cv2.VideoCapture(0)

cv2.namedWindow('mask')
cv2.createTrackbar('TH', 'mask', 10, 255, nothing)

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    TH = cv2.getTrackbarPos('TH', 'mask')
    lower_Hue = np.array([refHue-TH, 50, 50], dtype=np.uint8)
    upper_Hue = np.array([refHue+TH,255,255], dtype=np.uint8)    
    mask = cv2.inRange(hsv, lower_Hue, upper_Hue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()