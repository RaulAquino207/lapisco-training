'''
Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha os momentos CENTRAIS de todas
estas imagens. Imprima os resultados de cada imagem em um arquivo e na tela do prompt de comandos.
Cada linha do arquivo gerado deve representar os atributos obtidos em uma imagem.

spatial moments
double m00, double m10,double m01,double m20,double m11,double m02,double m30,double m21,double m12,double 	m03

central moments
double mu20,double mu11,double mu02,double mu30,double mu21,double mu12,double 	mu03

central normalized moments
double nu20,double nu11,double nu02,double nu30,double nu21,double nu12,double nu03
'''


import cv2
import os
import glob
import csv


def extract_central_moments(images):
    print('[INFO] Extracting central moments.')
    central_moments = []

    for i, image in enumerate(images):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(images)))

        # Load the rgb image
        file = cv2.imread(image)

        # Convert to grayscale
        file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

        # Extract the moments
        moments = cv2.moments(file)

        # Create a list with the features extracted
        central_moments.append([moments['mu20'], moments['mu11'], moments['mu02'], moments['mu30'],
                                moments['mu21'], moments['mu12'], moments['mu03']])

    print('\n')

    return central_moments


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

    # Extract central Moments
    features = extract_central_moments(image_paths)

    # Save the results in a csv file.
    save_results('CentralMoments', features)