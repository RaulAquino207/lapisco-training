import cv2 as cv
# import xml.etree.ElementTree as ET
#
# xml_string = './imglab_main.xml'
# tree = ET.parse(xml_string)
# root = tree.getroot()
#
# # ./opencv_createsamples -info cars.info -num 291 -w 48 -h 24 -vec cars.vec -bg bg.txt
# # ./opencv_traincascade -data data -vec cars.vec -bg bg.txt -numPos 10 -numNeg 500 -numStages 10 -w 48 -h 24 -featureType LBP
#
# num = 1
# for image in root:
#     for box in image:
#         for i in image.attrib:
#             num += 1
#             img = image.attrib[i]
#             print('pos/'+img +' '+ '1' +' '+ box.get('left')+' '+box.get('top')+' '+box.get('width')+' '+box.get('height'))
# #             file2 = open('cars.info', 'a')
# #             file2.write('pos/'+img +' '+ '1' +' '+ box.get('left')+' '+box.get('top')+' '+box.get('width')+' '+box.get('height'))
#
# print('quantidade de marcações: ', num)

cap = cv.VideoCapture('./exemplo_portao.avi')
while(cap.isOpened()):

    ret, img = cap.read()

    cars_cascade = cv.CascadeClassifier('./data/cascade_cars.xml')
    cars = cars_cascade.detectMultiScale(img, 1.1, 15)

    for (x, y, w, h) in cars:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)

    cv.imshow('Normal', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
         break

# img = cv.imread('./pos/1616_2_open_797.jpg')
# cars_cascade = cv.CascadeClassifier('./data/cascade_cars.xml')
# cars = cars_cascade.detectMultiScale(img, 1.1, 10)
#
# print(cars)
# for (x,y,w,h) in cars:
#     cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
#
# cv.imshow('CARS', img)
# cv.waitKey(0)