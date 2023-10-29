import cv2
import numpy as np

img=cv2.imread(r'temp_match_data\soccer_practice.jpg')
temp_img=cv2.imread(r'temp_match_data\ball.PNG')

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

temp_img_gray=cv2.cvtColor(temp_img,cv2.COLOR_BGR2GRAY)


methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

methods_labels = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

h,w=temp_img_gray.shape

# print(w,h)

for method in methods:
  img2=img_gray.copy()
  
  # print(methods_labels[method])
  
  result=cv2.matchTemplate(img2,temp_img_gray,method)
  
  
  min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
  
  # print(methods_labels[method],min_val,max_val,min_loc,max_loc)
  
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    location=min_loc
  else:
    location=max_loc
    
  bottom_right=(location[0]+w,location[1]+h)
  
  cv2.rectangle(img,location,bottom_right,(0,255,0),2)
  
  
  cv2.imshow(f'{methods_labels[method]}',img)
  #cv2.imshow('template',temp_img_gray)
  cv2.waitKey(0) & 0xFF
  cv2.destroyAllWindows()
  



