import cv2
import numpy as np

img=cv2.imread('fruit.jpg')

edges = cv2.Canny(img,50,175)
edges1 = cv2.Canny(img,100,200)

kernel=np.ones((3,3),dtype=np.uint8)

dilat=cv2.dilate(edges1,kernel)
ero=cv2.erode(dilat,kernel)

cv2.imshow('dilat',dilat) 
cv2.imshow('ero',ero) 
cv2.imshow('edges1',edges1) 

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
