import cv2 as cv 
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("2.jpg")

face_detect = face_cascade.detectMultiScale(img,1.1 , 4)

for (x,y,w,h) in face_detect:
    cv.rectangle(img, (x,y) , (x+w, y+h),(255,0,0), thickness=3)

cv.imshow("wjh dyal titiza ", img)
cv.waitKey(0)