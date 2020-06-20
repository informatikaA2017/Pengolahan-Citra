import cv2
import numpy as np


#Scalling / Meresize gambar
img = cv2.imread('./images/messi.jpg') #Mendefinisikan gambar

#Metode resize opencv untuk meresize gambar
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
#Metode resize opencv untuk meresize gambar
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('img', res) #Menampilkan gambar
cv2.waitKey(0) #delay ketika tombol ditekan
cv2. destroyAllWindows() #Menghancurkan semua window

#Translation
img2 = cv2.imread('./images/messi.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img2,M,(cols,rows)) #Menerapkan transformasi ke gambar

cv2.imshow('img',dst) #Menampilkan gambar
cv2.waitKey(0) #delay ketika tombol ditekan
cv2.destroyAllWindows() #Menghancurkan semua window

#Rotation
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) #Menghitung matriks dari rotasi 2D
dst = cv2.warpAffine(img,M,(cols,rows)) #Menerapkan transformasi ke gambar

cv2.imshow('img',dst) #Menampilkan gambar
cv2.waitKey(0) #delat ketika tombol ditekan
cv2.destroyAllWindows() #Menghancurkan semua window

#Affine Transformation
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2) #menghitung transformasi dari tiga pasang titik yang sesuai

dst = cv2.warpAffine(img,M,(cols,rows)) #Menerapkan transformasi ke gambar

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

#Perspective Transformation
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2) #Menghitung transformasi dari 4 pasang point yang sesuai

dst = cv2.warpPerspective(img,M,(300,300)) #Menerapkan transformasi perspektif ke gambar

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()