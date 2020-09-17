'''
Questão 18
Abrir uma imagem colorida, transformar para tom de cinza e aplicar o operador gradiente Laplaciano,
aplique a técnica de Equalização no resultado obtido na detecção das bordas, onde a maior intensidade de borda seja 255,
e a menor intensidade da borda seja 0.
'''
#library import
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('../input_images/image.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#apply the Laplacian Filter
laplace = cv.Laplacian(grayscale_img, ddepth=cv.CV_64F, ksize=3)

#convert to uint8
laplace = cv.convertScaleAbs(laplace)

#equalize the image of the laplacian filter
equalized_laplacian = cv.equalizeHist(laplace)

#show the input image
cv.imshow('Input grayscale image', grayscale_img)

#show the result of the laplacian filter
cv.imshow('Laplacian filter result', laplace)

#show the result of the equalized image of the laplacian filter
cv.imshow('Equalized Laplacian', equalized_laplacian)

cv.waitKey(0)

# plt.figure(1)
# plt.subplot(221)
# plt.imshow(equalized_laplacian, cmap='gray')
# plt.subplot(222)
# plt.hist(equalized_laplacian.ravel(), 256, [0, 256])
# plt.show()