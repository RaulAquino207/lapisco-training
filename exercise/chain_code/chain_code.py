import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

'''
1. Código 1: Implemente o algoritmo da cadeia, escolha um dos números
e imprima o código encontrado.
'''

class ChainCode():
    def __init__(self, path_image):
        self.path_image = path_image
        self.dim = (300, 300)

        self.img = cv.imread(self.path_image)
        self.img = cv.resize(self.img, self.dim, interpolation=cv.INTER_AREA)
        # grayscale_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        # ret, threshold_img = cv.threshold(grayscale_img, 110, 255, cv.THRESH_BINARY_INV)

        self.imgBin = 255 - self.img[:, :, 0]
        self.newImg = np.zeros(np.shape(self.imgBin))
        self.kernel = np.ones((3, 3), np.uint8)

        self.newImg = self.normalize((self.imgBin > 100) * 1)

        self.imCopy = np.copy(self.newImg)
        self.imPlot = np.zeros(np.shape(self.img))
        self.imPlot[:, :, 0] = self.imPlot[:, :, 1] = self.imPlot[:, :, 2] = self.imCopy

        self.newImg = cv.dilate(self.newImg, self.kernel, iterations=1) - self.newImg
        # self.dilate_img = cv.dilate(threshold_img, kernel, iterations=1) - threshold_img
        self.max_xy = np.where(self.newImg == 255)

        self.chainCode = []
        self.signalLenght = []
        self.counter = 0

    def normalize(self, v):
        v = (v - v.min()) / (v.max() - v.min())
        result = (v * 255).astype(np.uint8)
        return result

    def check_neighborhood_4(self, img, point):
        if img[point[0] - 1, point[1]] == 255:
            img[point[0] - 1, point[1]] = 0
            # print('0')
            self.chainCode.append(0)
            self.signalLenght.append(self.counter)
            self.counter = self.counter + 1
            return (point[0] - 1, point[1])

        elif img[point[0], point[1] + 1] == 255:
            img[point[0], point[1] + 1] = 0
            # print('1')
            self.chainCode.append(1)
            self.signalLenght.append(self.counter)
            self.counter = self.counter + 1
            return (point[0], point[1] + 1)

        elif img[point[0] + 1, point[1]] == 255:
            img[point[0] + 1, point[1]] = 0
            # print('2')
            self.chainCode.append(2)
            self.signalLenght.append(self.counter)
            self.counter = self.counter + 1
            return (point[0] + 1, point[1])

        elif img[point[0], point[1] - 1] == 255:
            img[point[0], point[1] - 1] = 0
            # print('4')
            self.chainCode.append(3)
            self.signalLenght.append(self.counter)
            self.counter = self.counter + 1
            return (point[0], point[1] - 1)

        else:
            print('none')

    def applying_chain_code(self):
        self.newImRGB = np.zeros(np.shape(self.img))
        self.newImRGB[:, :, 0] = self.newImRGB[:, :, 1] = self.newImRGB[:, :, 2] = self.newImg
        cv.circle(self.newImRGB, (self.max_xy[1][0], self.max_xy[0][0]), int(2), (0, 0, 255), 2)
        self.starPoint = (self.max_xy[0][0], self.max_xy[1][0])
        self.point = self.check_neighborhood_4(self.newImg, self.starPoint)
        while (self.point != self.starPoint):
            # print(self.point, self.starPoint)
            cv.circle(self.imPlot, (self.point[1], self.point[0]), int(6), (0, 0, 255), 1)
            cv.imshow('image', self.imPlot)
            cv.waitKey(1)
            cv.circle(self.imPlot, (self.point[1], self.point[0]), int(7), (0, 255, 255), 1)
            self.point = self.check_neighborhood_4(self.newImg, self.point)

        '''
        2. Código 2: Plote uma figura com o código da cadeia de todos os números
        1‘s.
        '''
        print(self.chainCode)
        plt.plot(self.chainCode)
        # print(self.counter)
        # print('signalLenght', len(self.signalLenght))
        plt.show()

        return self.chainCode, len(self.signalLenght)