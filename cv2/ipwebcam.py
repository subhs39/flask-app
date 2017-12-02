from urllib.request import urlopen
import cv2
import numpy as np

url='http://192.168.43.1:8080/shot.jpg'
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Use urllib to get the image from the IP camera
    imgResp = urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


    # put the image on screen
    cv2.imshow('IPWebcam',img)


    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()