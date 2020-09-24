'''
Questão 31
Após fazer a questão 30, destaque cada objeto encontrado desenhando um retângulo indicando onde os mesmos se encontram.
Utilizar a função “cvContourBoundingRect” para determinar cada contorno.
Ressalto que é necessário percorrer os contornos encontrados na função “cvFindContours” de forma correta.
'''
import cv2 as cv
import numpy as np

img = cv.imread('../input_images/objects_canny.png')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(img, 80, 255)

contours, hierarchy = cv.findContours(canny_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours_poly = [None] * len(contours)
bound_rect = [None] * len(contours)

for i, contour in enumerate(contours):
    '''
    Contour Approximation
    It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. 
    It is an implementation of Douglas-Peucker algorithm. Check the wikipedia page for algorithm and demonstration.
    We use the function: cv.approxPolyDP (curve, approxCurve, epsilon, closed)
    '''
    contours_poly[i] = cv.approxPolyDP(contour, 2, True)

    '''
    Straight Bounding Rectangle
    It is a straight rectangle, it doesn't consider the rotation of the object. 
    So area of the bounding rectangle won't be minimum.
    We use the function: cv.boundingRect (points)
    '''
    bound_rect[i] = cv.boundingRect(contours_poly[i])

print(bound_rect)
# Create a copy of the image to draw the contours
contour_img = np.copy(img)

# Draw the rectangles for every object
for i, contour in enumerate(contours_poly):
    cv.rectangle(contour_img, (int(bound_rect[i][0]), int(bound_rect[i][1])),
                  (int(bound_rect[i][0]) + int(bound_rect[i][2]), int(bound_rect[i][1]) + bound_rect[i][3]),
                  (255, 0, 0), 2)

# Show the input image
cv.imshow('Input grayscale image', grayscale_img)

# Show the contours found
cv.imshow('Contours', contour_img)
cv.waitKey(0)