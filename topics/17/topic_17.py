'''
Questão 17
Abrir uma imagem colorida, transformar para tom de cinza e aplicar uma Equalização de histograma utilizando apenas o
conhecimento de manipulação da imagem, sem a OpenCv, visualizando a imagem de entrada e seu respectivo histograma inicialmente, e,
em seguida, o resultado da equalização e seu histograma. Esta técnica aumenta o contraste da imagem.
'''
#library import
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../input_images/image.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

original_hist = np.zeros([256], np.uint8)
equalized_hist = np.zeros([256], np.uint8)
#flatten return a copy of the array collapsed into one dimension.
img_flat = grayscale_img.flatten()

for pixel in img_flat:
    original_hist[pixel] += 1

#print(original_hist)
#calculates the cumulative distribution function of the histogram
cdf = [sum(original_hist[:i + 1]) for i in range(len(original_hist))]
'''
for i in range(len(original_hist)):
    cpf = sum(original_hist[:i + 1])
    print(cpf)
'''
cdf = np.array(cdf)
#print(cdf)
#normalize the cdf to be between 0-255
normal_cdf = ((cdf - cdf.min())*255)/(cdf.max() - cdf.min())
normal_cdf = normal_cdf.astype('uint8')
equalized_image = normal_cdf[img_flat]
equalized_image = np.reshape(equalized_image, grayscale_img.shape)
print('equalized_image = normal_cdf[img_flat]')
print('equalized',equalized_image[:20], equalized_image.shape)
print('normal_cdf',normal_cdf[:20], normal_cdf.shape)
print('img_flat',img_flat[:20], img_flat.shape)




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

