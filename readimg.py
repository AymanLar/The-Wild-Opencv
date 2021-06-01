
#first lines 

import cv2 as cv

img = cv.imread('1.jpg',-1)
imgTwo = cv.imread('2.jpg',0)

print(img)
print(imgTwo)
cv.imshow('titiiiza2', imgTwo)
cv.imshow('Titiiza1', img)
cv.waitKey(delay=0)

cv.destroyAllWindows()

