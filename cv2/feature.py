import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('feature1.jpg',0)
img2 = cv2.imread('feature2.jpg',0)

# img1 = cv2.flip(img1,1)
# img2 = cv2.flip(img2,1)

#This is the detector we're going to use for the features.
orb = cv2.ORB_create()
#Here, we find the key points and their descriptors with the orb detector.
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
#This is our BFMatcher object.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#Here we create matches of the descriptors, then we sort them based on their distances.
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)
#Here, we've drawn the first 10 matches. The output:
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
#cv2.imshow("final",img3)
plt.imshow(img3)
plt.show()