import glob
import os
from extractors import Extraction

'''
Questão 2 - Utilizando os extratores LBP, HU e GLCM, extraia as
características das imagens disponibilizadas no ClassRoom (num-
ber1.rar) e crie um arquivo contendo linha por linha as caracterís-
ticas extraídas a fim de montar um dataset. Não precisa incluir o
Rótulo
'''
path = '../input_images/number1/'
#Navigating the path where the images are.
for r, d, f in os.walk(path):
    for filename in f:
        #Making extractions.
        extractions = Extraction(glob.glob(os.path.join(path, filename)))
        extractions.extract_hu_moments()
        extractions.extract_lbp(number_points=24, radius=8)
        extractions.extract_glcm(distances=[5], angles=[0])
