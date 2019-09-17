import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    change0 = cv2.flip(frame, 0)
    change1 = cv2.flip(frame, 1)
    change2 = cv2.flip(frame, -1)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('change0',change0)
    cv2.imshow('change1',change1)
    cv2.imshow('change2',change2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()