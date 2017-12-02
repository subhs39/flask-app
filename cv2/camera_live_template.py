import cv2
import numpy as np
from urllib.request import urlopen
url='http://192.168.137.118:8080/shot.jpg'
while True:
    imgResp = urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('imgb/template_image.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)

    """if loc is not null or whatever do url2+/LEFT or whatever
		similarly goes for other objects like loc1,loc2,loc3
		that is Stop,Left,Right    """
    for pt in zip(*loc[::-1]):
    	cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    cv2.imshow('Detected',img)
    if cv2.waitKey(1) & 0xFF== ord('q'):
    	break
cv2.destroyAllWindows()