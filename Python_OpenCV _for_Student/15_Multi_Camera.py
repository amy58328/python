import cv2
import numpy as np

if __name__ == '__main__':

    cap = cv2.VideoCapture(0) 
    cap1 = cv2.VideoCapture(1)

    while True:
        flag, img = cap.read()
        img=cv2.flip(img, 1)
        flag1, img1= cap1.read()
        img1=cv2.flip(img1, 1)
        cv2.imshow('frame', img)
        cv2.imshow('frame1', img1)
        ch = cv2.waitKey(5)
        if ch == 27:
            break