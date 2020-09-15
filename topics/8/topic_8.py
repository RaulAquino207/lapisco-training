'''
Questão 8
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem um redimensionamento da imagem, reduzindo e depois aumentando seu tamanho, visualizem os resultados e salvem.
Obs: uma imagem 320×240 deve virar uma 160×120 em primeiro caso e 640×480 em segundo caso.
'''
#library import
import cv2 as cv
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#analyzing the type of images for better understanding
print(type(img), type(grayscale_img))
'''
The shape method can be used without problem because the cv2 library returns numpy.ndarray, and the "shape [: 2]"
is only necessary in an image with 3 color channels (RGB), in the grayscale image just use the shape method
'''
# rows, cols = img.shape[:2]
rows, cols = grayscale_img.shape
#showing the image size
print(rows,cols)
#using the resize method to resize my image
double_sized_image = cv.resize(grayscale_img,(2 * rows, 2 * cols))
half_sized_image = cv.resize(grayscale_img, (int(rows/2), int(cols/2)))
#showing the images
cv.imshow('Input grayscale image', grayscale_img)
cv.imshow('Double sized image', double_sized_image)
cv.imshow('Half sized image', half_sized_image)
#waitkey makes the image show until 0 is pressed
cv.waitKey(0)
#storing the results
cv.imwrite('double_sized_result.jpg', double_sized_image)
cv.imwrite('half_sized_result.jpg', half_sized_image)


