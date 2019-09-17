import cv2
import numpy as np
import sys
import math

if __name__ == '__main__':

    try:
        fn = sys.argv[1]
    except IndexError:
        exit(1)

    src = cv2.imread(fn)
    dst = cv2.Canny(src, 50, 200)

    lines = cv2.HoughLines(dst, 1, math.pi/180.0, 50, np.array([]), 0, 0)

    if lines is not None:
        a,b,c = lines.shape
        #for i in range(a):
        for i in range(5):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0, y0 = a*rho, b*rho
            pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
            pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
            cv2.line(src, pt1, pt2, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow("source", src)
    cv2.imshow("detected lines", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()