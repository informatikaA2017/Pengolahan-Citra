import cv2
import numpy as np

img = cv2.imread('./images/messi.jpg')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()