import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    _,img=cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY_INV) 
    edges = cv2.Canny(thresh,50,150,apertureSize = 3)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
       
    try:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),4)
    except:
        pass
    cv2.imshow("normal",img)
    cv2.imshow("canny",edges)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
