import os
import cv2 as cv

# To save the path of the negative/positive images in the text document bg.txt/cars.info.
# path = './neg'
# path = './pos'
# for r, d, f in os.walk(path):
#     for filename in f:
#         print(filename)
#         file1 = open('bg.txt', 'a')
#         file1.write('neg/' + filename + '\n')
#         file2 = open('cars.info', 'a')
#         file2.write('pos/' + filename + ' 1 0 0 100 40' + '\n')

# https://opencv.org/releases/
# ./opencv_createsamples -info cars.info -num 550 -w 48 -h 24 -vec cars.vec -bg bg.txt
# ./opencv_traincascade -data data -vec cars.vec -bg bg.txt -numPos 10 -numNeg 500 -numStages 10 -w 48 -h 24 -featureType LBP

img = cv.imread('./test/test-3.pgm')
cars_cascade = cv.CascadeClassifier('./data/cascade_cars.xml')
cars = cars_cascade.detectMultiScale(img, 1.1, 1)

print(cars)
for (x,y,w,h) in cars:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)

cv.imshow('CARS', img)
cv.waitKey(0)