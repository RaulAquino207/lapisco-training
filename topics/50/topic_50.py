'''
Questão 50
Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha as Texturas de Haralick
que são calculadas à partir da matriz de co-ocorrência (GLCM em inglês) de todas estas imagens. Imprima os resultados de
cada imagem em um arquivo e na tela do prompt de comandos. Cada linha do arquivo gerado deve representar os atributos
obtidos em uma imagem.
'''

import cv2
import os
import glob
import csv
import numpy as np
from skimage import feature


def extract_glcm(images, distances, angles):
    print('[INFO] Extracting GLCM.')
    glcm_features = []

    for i, image in enumerate(images):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(images)))

        # Load the rgb image
        file = cv2.imread(image)

        # Convert to grayscale
        file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

        # Extract lbp
        glcm = feature.greycomatrix(file, distances, angles, 256, symmetric=False, normed=True)

        # Create a list with the features of GLCM
        glcm_properties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
        features = [feature.greycoprops(glcm, glcm_property)[0, 0] for glcm_property in glcm_properties]

        glcm_features.append(features)

    print('\n')

    return glcm_features


def save_results(extractor_name, features):

    # Show the extracted features in command prompt
    for vector in features:
        print(vector)

    # Save all features in a csv file
    with open(extractor_name + '.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(features)


if __name__ == '__main__':

    # Inform the path to the rgb images
    dataset = '../input_images/dataset'

    # Grab all the paths to the images with extension .jpg
    image_paths = glob.glob(os.path.join(dataset, '*.jpg'))

    # Extract GLCM
    features = extract_glcm(image_paths, distances=[5], angles=[0])

    # Save the results in a csv file.
    save_results('GLCM', features)