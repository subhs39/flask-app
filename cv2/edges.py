import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    # img = cv2.imread('dave.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    edges = cv2.Canny(gray,50,50,apertureSize = 3)
    cv2.imshow('edges',edges)

    minLineLength = 30
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength,maxLineGap)
    for x in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[x]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow('hough',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





"""5 steps to sucess 
1. sobel
2. canny
3. hough
4. tweaking
5. implementing
Then move on to the dog detection"""