import cv2 as cv 

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

vid = cv.VideoCapture('vid1.mp4')

while vid.isOpened():
    _, frame = vid.read()
    face_detect = face_cascade.detectMultiScale(vid,1.1, 4)

    for (x,y,w,h) in face_detect:
        cv.rectangle(frame, (x,y) , (x+w, y+h) ,(255,0,0), thickness=3)

        cv.imshow(" ", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

frame.release()
cv.destroyAllWindows()
        