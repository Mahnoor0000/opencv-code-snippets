import cv2 as cv
import numpy as np

img = cv.imread('messi5.jpg')
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

template = cv.imread('messi-face.png',0)
w,h = template.shape[::-1]

res = cv.matchTemplate(grey_img,template,cv.TM_CCOEFF_NORMED)
print(res)

threshold = 0.4

loc = np.where(res>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w ,pt[1]+h),(0,0,255),1)


cv.imshow('Image',img)

cv.waitKey(0)
cv.destroyAllWindows()