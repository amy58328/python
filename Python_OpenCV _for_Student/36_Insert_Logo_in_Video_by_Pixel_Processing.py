import numpy as np
import cv2



def InsertLogo(img1, img2, x, y):
	# I want to put logo on top-left corner, So I create a ROI
	rows,cols,channels = img2.shape
	roi = img1[x:x+rows, y:y+cols ]
	# Now create a mask of logo and create its inverse mask also
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	# Now black-out the area of logo in ROI
	img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
	# Take only region of logo from logo image.
	img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
	# Put logo in ROI and modify the main image
	dst = cv2.add(img1_bg,img2_fg)
	img1[x:x+rows, y:y+cols ] = dst
	return img1

	
def InsertLogo_2(img1, img2, x, y):
	# Direct access pixels of images to put logo
	rows,cols,channels = img2.shape
	roi = img1[x:x+rows, y:y+cols ]
	# Now create a mask of logo and create its inverse mask also
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	for i in range(rows):
		for j in range(cols):
			if mask[i][j] != 0:
				img1[i+x][j+y]=img2[i][j]
	return img1
	
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rowsFrame,colsFrame,channelsFrame = frame.shape

blank_image = np.zeros((len(frame),len(frame[0]),3), np.uint8)
logo = cv2.imread('logo.png')
logo = cv2.resize(logo, (100, 100)) 
rowsLogo,colsLogo,channelsLogo = logo.shape
x=0
y=0
speed=10

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    InsertLogo_2(frame, logo, x, y)
    x=x+speed
    if x+rowsLogo > rowsFrame:
        x=0
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()