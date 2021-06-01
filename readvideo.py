
import cv2 as cv

vid  = cv.VideoCapture('vid1.mp4') #replace 'vid1.mp4' with 0 i u use the webcam :)

while(True):
    ret, hotvideo = vid.read()
#changing the color 
    changeColor = cv.cvtColor(hotvideo,cv.COLOR_BGRA2YUV_I420)

    cv.imshow('', changeColor) # REPLACE changeColor WITH hotvideo to see the normal one 
    if cv.waitKey(1) & 0xFF == ord('q'): # when u click q in the keybord u quit
        break


#SAVING THE VIDEO

while(vid.isOpened()):
    ret , frame = vid.read()

    if ret == True:
        print(vid.get(cv.VID_PROP_FRAME_WIDTH))
        print(vid.get(cv.VID_PROP_FRAME_HEIGHT))


    


vid.release()
cv.destroyAllWindows()

