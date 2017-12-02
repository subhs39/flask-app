#Non-Action Reduction
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
subtract=cv2.createBackgroundSubtractorMOG2()

while True:
	ret,img=cap.read()
	action=subtract.apply(img)

	cv2.imshow("normal",img)
	cv2.imshow("Action",action)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()