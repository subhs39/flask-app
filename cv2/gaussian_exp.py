import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
	ret,img=cap.read()
	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gauss=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

	cv2.imshow("normal",img)
	cv2.imshow("gaussian",gauss)
	if cv2.waitKey(1) & 0xFF== ord('q'):
		break
cap.release()
cv2.destroyAllWindows()