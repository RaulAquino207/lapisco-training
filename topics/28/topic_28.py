'''
Questão 28
Abrir uma imagem colorida, transformar para tom de cinza e aplique e aplique a limiarização automática da
própria Opencv, para que o limiar não dependa da aplicação e nem da luminosidade do local.
'''

import cv2

# Read a rgb image
image = cv2.imread('../input_images/image.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply an adaptive threshold
'''
The adaptiveMethod decides how the threshold value is calculated:

cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
The blockSize determines the size of the neighbourhood area and C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.
'''
thresholded_image = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Show the result of the adaptive threshold
cv2.imshow('Threshold result', thresholded_image)
cv2.waitKey(0)