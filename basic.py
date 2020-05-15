import cv2
import numpy as np

img = cv2.imread('./images/messi.jpg')

px = img[100,100]
print(px)

blue = img[100,100,0]
print(blue)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()