import numpy as np
import cv2
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('test.jpg')
img = cv2.resize(img, (800, 600))
img2 = img.copy()
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(len(faces))

roi=[]
face_xywh=[]
for (x,y,w,h) in faces:
	face_xywh.append((x,y,w,h))
	#cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi.append(img[y:y+h, x:x+w])

roi_New=[]
roi_New.append(cv2.resize(roi[0], (face_xywh[1][2], face_xywh[1][3])))
roi_New.append(cv2.resize(roi[1], (face_xywh[0][2], face_xywh[0][3])))

cv2.imshow("roi_0", roi[0])
cv2.imshow("roi_1", roi[1])  

cv2.imshow("roi_2", roi_New[0])
cv2.imshow("roi_3", roi_New[1]) 

x1=face_xywh[0][0]
y1=face_xywh[0][1]
w1=face_xywh[0][2]
h1=face_xywh[0][3]
roi_New[1]=cv2.flip(roi_New[1], 1)
img2[y1:y1+h1, x1:x1+w1]=roi_New[1]

x2=face_xywh[1][0]
y2=face_xywh[1][1]
w2=face_xywh[1][2]
h2=face_xywh[1][3]

img2[y2:y2+h2, x2:x2+w2]=roi_New[0]

cv2.imshow('img',img)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()