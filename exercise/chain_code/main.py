import cv2 as cv
import os
from chain_code import ChainCode
from recovery_image import RecoveryImage
from black_box_normalization import BlackBox
from mode_chain_codes import ModeChainCode

'''
Questão 1 - Considerando as imagens disponibilizadas no Class-
Room (number1.rar), implemente o que se pede:
'''
signalLenght = []
chain_codes = []
path = '../input_images/number1/'
for r, d, f in os.walk(path):
    for filename in f:
        chain = ChainCode(os.path.join(path, filename))
        chain_code, signal = chain.applying_chain_code()

        chain_codes.append(chain_code)
        signalLenght.append(signal)

        draw_recovery = RecoveryImage(chain_code)


black_box = BlackBox(chain_codes, signalLenght)
# print(black_box.new_chain_codes)

mode_chain_codes = ModeChainCode(black_box.new_chain_codes)
# print(draw_number.chain_code_mode)

draw_recovery = RecoveryImage(mode_chain_codes.chain_code_mode)