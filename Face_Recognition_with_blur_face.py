import cv2

videos = cv2.VideoCapture(0)
videos.set(3,640)
videos.set(4,480)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


while (videos.isOpened()):
    suucess, img = videos.read()
    faces = face_cascade.detectMultiScale(img,1.3,4)

    for(x,y,w,h) in faces:
        RDI = img[y:y+h,x:x+w]
        blur = cv2.GaussianBlur(RDI,(99, 99), 0)
        img[y:y+h,x:x+w] = blur

        cv2.imshow("Blurred face", img)
        if cv2.waitKey(1) & 0xff == ord('q'):
             break

videos.release()
cv2.destroyAllWindows()
