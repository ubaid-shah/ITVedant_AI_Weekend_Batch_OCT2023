import cv2
cap=cv2.VideoCapture('p.mp4')
face_class=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    ret,frame=cap.read()
    
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face_rec=face_class.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=9)

    
    for (x, y, w, h) in face_rec: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2) 
        
    
    cv2.imshow('p',frame)
    
    if cv2.waitKey(10)& 0xFF==ord('q'):
        break
        
        
cap.release()
cv2.destroyAllWindows()
