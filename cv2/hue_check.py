import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
	_,img=cap.read()
	# lower_yellow = np.array([20, 100, 100], dtype = "uint8")
	# upper_yellow = np.array([30, 255, 255], dtype="uint8")
	# mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
	# mask_white = cv2.inRange(gray_image, 200, 255)
	# mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
	# mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)
	# cv2.imshow("yellow",mask_yw_image)

	yellow_threshold = [220,220,30]
	yellow_select_image = np.copy(img)
	yellow_thresholds = (img[:,:,0] > yellow_threshold[0]) \
	| (img[:,:,1] > yellow_threshold[1]) \
	| (img[:,:,2] < yellow_threshold[2])
	 
	yellow_select_image[yellow_thresholds] = [0,0,0]
	cv2.imshow("yellow",yellow_select_image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()