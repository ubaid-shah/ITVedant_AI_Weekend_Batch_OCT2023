import cv2

img=cv2.imread(r'C:\Users\admin\Documents\Ubaid_CV\Data\drive-download-20231104T040630Z-001\cow-salt-peper.png')

blur_img=cv2.blur(img,(7,7))
g_blur=cv2.GaussianBlur(img,(7,7),5)


cv2.imshow('blur_img',blur_img)
cv2.imshow('g_blur',g_blur)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()