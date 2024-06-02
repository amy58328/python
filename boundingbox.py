import cv2

while True:
    input_arr = input("input coordinate：").strip('[]').strip('()').split(',')
    image = cv2.imread(f'./temp.jpg')
    w_deform = 1.559375
    h_deform = 2.079167
    
    if ( len(input_arr) == 4):

        
        x1, y1 = int(int(input_arr[0])/w_deform), int(int(input_arr[1])/h_deform)  
        x2, y2 = int(int(input_arr[2])/w_deform), int(int(input_arr[3])/h_deform)  

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2) 

    else:
        x = int(int(input_arr[0])/w_deform)
        y = int(int(input_arr[1])/h_deform)

        cv2.circle(image,(x,y),5,(0,255,0),-1)


    cv2.imshow('Image with Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()