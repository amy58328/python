from openni import openni2
import numpy as np
import cv2

def mousecallback(event,x,y,flags,param):
     if event==cv2.EVENT_LBUTTONDBLCLK:
         print(y, x, dpt[y,x])


if __name__ == "__main__": 
    # openni2.initialize()

    # dev = openni2.Device.open_any()
    # print(dev.get_device_info())

    # depth_stream = dev.create_depth_stream()
    # depth_stream.start()

    # cv2.namedWindow('depth')
    # cv2.setMouseCallback('depth',mousecallback)

    cap = cv2.VideoCapture(1)


while True:

    # frame = depth_stream.read_frame()
    # dframe_data = np.array(frame.get_buffer_as_triplet()).reshape([480, 640, 2])
    # dpt1 = np.asarray(dframe_data[:, :, 0], dtype='float32')
    # dpt2 = np.asarray(dframe_data[:, :, 1], dtype='float32')
    
    # dpt2 *= 255
    # dpt = dpt1 + dpt2
    
    # cv2.imshow('depth', dpt)
    

    ret,frame = cap.read()

    cv2.imshow("Camera",frame)
    
    key = cv2.waitKey(1)
    if int(key) == ord('q'):
        break

# depth_stream.stop()
# dev.close()