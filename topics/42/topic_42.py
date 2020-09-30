'''
As questões 41-45 serão sobre o uso da biblioteca "blob"

Abrir uma imagem colorida, transformar para tom de cinza e aplique a transformada de canny para detectar bordas.
Apliquem a biblioteca “blob” para determinar quantos contornos existem na imagem. Apresentem o resultado obtido e a
imagem de entrada. O retorno deve ser a mesma quantidade de objetos existentes.
'''

import cv2 as cv
import numpy as np

img = cv.imread('../input_images/objects_canny.png')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(grayscale_img, 80, 180)

'''
A Blob is a group of connected pixels in an image that share some common property ( E.g grayscale value ). 
In the image above, the dark connected regions are blobs, and the goal of blob detection is to identify and 
mark these regions.
'''
# Define the parameters
params = cv.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.8

# Distance Between Blobs
params.minDistBetweenBlobs = 20

# Create a blob detector with the parameters
detector = cv.SimpleBlobDetector_create(params)

# Detect objects
blobs = detector.detect(canny_img)

# Print how many objects are in the image
print(len(blobs))

# Show the input image
cv.imshow('Input grayscale image', grayscale_img)
cv.waitKey(0)