import cv2
import pytesseract
from pytesseract import Output


# img_life=cv2.imread(r'C:\Users\admin\Documents\Ubaid_CV\Data\OCR\life.png')
# img_b=cv2.imread(r'C:\Users\admin\Documents\Ubaid_CV\Data\OCR\b.png')

# img_ocr=cv2.imread(r'C:\Users\admin\Documents\Ubaid_CV\Data\OCR\ocr.jpg')
img_c=cv2.imread(r'C:\Users\admin\Documents\Ubaid_CV\Data\OCR\c.png')

# blur_img=cv2.blur(img_b,(7,7))
img_gray=cv2.cvtColor(img_c,cv2.COLOR_BGR2GRAY)

result=pytesseract.image_to_string(img_gray)
print(result)

with open('result.txt','w') as f:
  f.write(str(result))