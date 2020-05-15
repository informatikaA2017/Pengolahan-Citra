import cv2
import numpy as np

img = cv2.imread('./images/messi.jpg')

#Access Pixel Value
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

# accessing RED value
red = img.item(10,10,2)
print(red)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

print(img.shape)
print(img.size)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()