import glob
import os
from chain_code import ChainCode
from recovery_image import RecoveryImage
from black_box_normalization import BlackBox
from mode_chain_codes import ModeChainCode
from extractors import Extraction

'''
Questão 1 - Considerando as imagens disponibilizadas no Class-
Room (number1.rar), implemente o que se pede:
'''
signalLenght = []
chain_codes = []
path = '../input_images/number1/'
for r, d, f in os.walk(path):
    for filename in f:
        #Taking the chain code out of each of my images.
        chain = ChainCode(os.path.join(path, filename))
        chain_code, signal = chain.applying_chain_code()

        #Storing the chain code and len of my signals in the respective vectors.
        chain_codes.append(chain_code)
        signalLenght.append(signal)

        draw_recovery = RecoveryImage(chain_code)

        extractions = Extraction(glob.glob(os.path.join(path, filename)))
        extractions.extract_hu_moments()
        extractions.extract_lbp(number_points=24, radius=8)
        extractions.extract_glcm(distances=[5], angles=[0])

black_box = BlackBox(chain_codes, signalLenght)
mode_chain_codes = ModeChainCode(black_box.new_chain_codes)
draw_recovery = RecoveryImage(mode_chain_codes.chain_code_mode)