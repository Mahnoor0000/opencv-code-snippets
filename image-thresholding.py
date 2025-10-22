import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('smarties.png',cv.IMREAD_GRAYSCALE)

_, mask = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

kernel = np.ones((3,3),np.uint8)

open = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
titles = ['images','mask','open']
images = [img,mask,open]

for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
