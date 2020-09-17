'''
Questão 16
Abrir uma imagem colorida, transformar para tom de cinza e aplicar uma Equalização de histograma utilizando a OpenCv,
visualizando a imagem de entrada e seu respectivo histograma inicialmente, e,
em seguida, o resultado da equalização e seu histograma. Esta técnica aumenta o contraste da imagem.
'''
#library import
import cv2 as cv
import matplotlib.pyplot as plt
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#equalize image
equalized_image = cv.equalizeHist(grayscale_img)
#calculate histograms of the original image and the equalized image using only openCV
original_hist = cv.calcHist(grayscale_img, channels=[0], mask=None, histSize=[256], ranges=[0, 256])
equalized_hist = cv.calcHist(equalized_image, channels=[0], mask=None, histSize=[256], ranges=[0, 256])
#show the original, the equalized image and their histograms
#in python we can calculate and show the histogram using only matplotlib
plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_img, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_img.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(equalized_image, cmap='gray')
plt.subplot(224)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.show()
