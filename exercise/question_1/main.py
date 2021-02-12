import glob
import os
from chain_code import ChainCode
from recovery_image import RecoveryImage
from black_box_normalization import BlackBox
from mode_chain_codes import ModeChainCode

'''
Questão 1 - Considerando as imagens disponibilizadas no Class-
Room (number1.rar), implemente o que se pede:

Part 1 - file 'chain_code.py'
Part 2 - file 'chain_code.py'   
Part 3 - file 'recovery_image.py'
Part 4 - file 'black_box_normalization.py'
Part 5 - file 'mode_chain_codes'
'''

#Vectors where the len() of the signals and chain codes were.
signalLenght = []
chain_codes = []
path = '../input_images/number1/'
#Navigating the path where the images are.
for r, d, f in os.walk(path):
    for filename in f:
        #Taking the chain code out of each of my images.
        chain = ChainCode(os.path.join(path, filename))
        chain_code, signal = chain.applying_chain_code()

        #Storing the chain code and len of my signals in the respective vectors.
        chain_codes.append(chain_code)
        signalLenght.append(signal)

        #Doing the opposite way, redrawing the images.
        draw_recovery = RecoveryImage(chain_code)

#Doing the black box normalization.
black_box = BlackBox(chain_codes, signalLenght)

#Storing in "mode_chain_codes", the mode of the values of normalized chain codes.
mode_chain_codes = ModeChainCode(black_box.new_chain_codes)

#Drawing from the returned fashion.
draw_recovery = RecoveryImage(mode_chain_codes.chain_code_mode)