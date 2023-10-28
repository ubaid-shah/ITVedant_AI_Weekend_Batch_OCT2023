import cv2
cap=cv2.VideoCapture('q.mp4')
face_class=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_class=cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    ret,frame=cap.read()
    
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img_gray=cv2.equalizeHist(img_gray)
    
    face_rec=face_class.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=9)
    eye_rec=eye_class.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=20)
    
    for (x, y, w, h) in face_rec: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2) 
        
    for (x2,y2,w2,h2) in eye_rec:
        eye_center = (x + x2 + w2//2, y + y2 + h2//2)
        radius = int(round((w2 + h2)*0.25))
        cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    
    cv2.imshow('p',frame)
    
    if cv2.waitKey(10)& 0xFF==ord('q'):
        break
        
        
cap.release()
cv2.destroyAllWindows()
    
