import cv2
import sys

def face_off(faces):
	global frame
	roi=[]
	face_xywh=[]
	for (x,y,w,h) in faces:
		face_xywh.append((x,y,w,h))
		roi.append(frame[y:y+h, x:x+w])

	roi_New=[]
	roi_New.append(cv2.resize(roi[0], (face_xywh[1][2], face_xywh[1][3])))
	roi_New.append(cv2.resize(roi[1], (face_xywh[0][2], face_xywh[0][3])))

	x1=face_xywh[0][0]
	y1=face_xywh[0][1]
	w1=face_xywh[0][2]
	h1=face_xywh[0][3]
	roi_New[1]=cv2.flip(roi_New[1], 1)
	frame[y1:y1+h1, x1:x1+w1]=roi_New[1]

	x2=face_xywh[1][0]
	y2=face_xywh[1][1]
	w2=face_xywh[1][2]
	h2=face_xywh[1][3]
	roi_New[0]=cv2.flip(roi_New[0], 1)
	frame[y2:y2+h2, x2:x2+w2]=roi_New[0]


cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    frame2=frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    print(len(faces))
    if len(faces)>=2:
        face_off(faces)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('frame2', frame2)
	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()