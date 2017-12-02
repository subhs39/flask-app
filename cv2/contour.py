import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
	ret,img=cap.read()
	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	#gauss=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
	ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
	#ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)
	_,contours,_ = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
	if len(contours)>0:
		c=max(contours,key=cv2.contourArea)
		M=cv2.moments(c)
		cx=int(M['m10']/M['m00'])
		cy=int(M['m01']/M['m00'])
		cv2.line(img,(cx,0),(cx,480),(255,0,0),1)
		cv2.line(img,(0,cy),(640,cy),(255,0,0),1)
		cv2.drawContours(img, contours, -1, (0,255,0), 1)
		#print(cx , cy)
		if cx >= 400:
			print("Turn Left")
		elif cx < 400 and cx > 280:
			print("On Track !")
		elif cx <= 280:
			print("Turn Right")
		else:
			print("i dont see a line")
	cv2.imshow("normal",img)
	#cv2.imshow("gaussian",gauss)
	cv2.imshow("thresh",thresh)
	if cv2.waitKey(1) & 0xFF== ord('q'):
		break

cap.release()
cv2.destroyAllWindows()