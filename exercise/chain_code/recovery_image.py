import cv2 as cv
import numpy as np
'''
3. Código 3: A partir de um código da cadeia de um dos números, desenhe
o número correspondente ao código
'''
class RecoveryImage():
    def __init__(self, chain_code):
        self.chain_code = chain_code
        self.recovery_chain_code()

    def recovery_chain_code(self):
        # print(self.chainCode)
        self.recovery_img = np.zeros((500,500))
        self.current_point = (100, 170)
        # print(self.current_point)
        for value in self.chain_code:
            self.current_point = self.recovery_image(self.recovery_img, self.current_point, value)
            cv.imshow('recovery image', self.recovery_img)
            cv.waitKey(1)

    def recovery_image(self, recovery_img, point, chainCode):
        if chainCode == 0:
            recovery_img[point[0] - 1, point[1]] = 255
            # print('0')
            return (point[0] - 1, point[1])

        elif chainCode == 1:
            recovery_img[point[0], point[1] + 1] = 255
            # print('1')
            return (point[0], point[1] + 1)

        elif chainCode == 2:
            recovery_img[point[0] + 1, point[1]] = 255
            # print('2')
            return (point[0] + 1, point[1])

        elif chainCode == 3:
            recovery_img[point[0], point[1] - 1] = 255
            # print('4')
            return (point[0], point[1] - 1)

        else:
            print('inicio')
