import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv-logo.png')
imgGRAY = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgGRAY, 127,255,0 )

contour, hierarchy = cv.findContours(imgGRAY, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print('Number of contours = ' + str(len(contour)))

cv.drawContours(img, contour, -1, (0,0,255), 2)
cv.imshow('real',img)
cv.imshow('GRAY',imgGRAY)

cv.waitKey(0)
cv.destroyAllWindows()

