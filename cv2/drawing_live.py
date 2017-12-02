import cv2
import numpy as np

def until(left,right,depth):
	flag=flag1=flag3=0
	previous=[]
	current=[]
	previous().tuple.append(left)
	if previous[::-1]==current[0::]:
		flag=1
	if 

	

def tell_percentage(faces):
	x=faces[0][0]+faces[0][2]/2
	y=faces[0][1]+faces[0][2]/2
	x_percentage=(x/640)*100
	y_percentage=(y/480)*100
	return 100-x_percentage,100-y_percentage

def tell_dir(x,y):
	if x>60:
		dir1="Right"
	elif x<40:
		dir1="Left"
	else:
		dir1="Middle"
	if y>60:
		dir2="Up"
	elif y<40:
		dir2="Down"
	else:
		dir2="Middle"
	return dir1,dir2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while True:
	ret, frame =cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y), (x+w, y+h), (255,0,0),2)
	if len(faces) is not 0:
		x,y=tell_percentage(faces)
		print(x,"%\t",y,"%")
		dir1,dir2 =tell_dir(x,y)
		print (dir1,"  ",dir2)
	else:
		print("no faces detected")
	frame=cv2.flip(frame,1)
	cv2.imshow("drawing",frame)
	# cv2.line(frame,(15,15),(200,150),(255,0,0),3)
	if cv2.waitKey(1) & 0xFF== ord('q'):
		break




cap.release()
cv2.destroyAllWindows()


