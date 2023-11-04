import cv2

img=cv2.imread(r'C:\Users\admin\Documents\Ubaid_CV\Data\handwritten.png')

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,128,255,cv2.THRESH_BINARY_INV)

ad_thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,15)


cv2.imshow('img',ad_thresh)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()