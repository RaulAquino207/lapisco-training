'''
Questão 48
Abrir uma sequência de imagens coloridas, transformar para tom de cinza cada imagem e obtenha os momentos de HU
(também conhecidos como momentos invariantes) de todas estas imagens.
Imprima os resultados de cada imagem em um arquivo e na tela do prompt de comandos.
Cada linha do arquivo gerado deve representar os atributos obtidos em uma imagem.
'''
import cv2
import os
import glob
import csv


def extract_hu_moments(images):
    print('[INFO] Extracting HU Moments.')
    complete_hu_moments = []

    for i, image in enumerate(images):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(images)))

        # Load the rgb image
        file = cv2.imread(image)

        # Convert to grayscale
        file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

        # Extract the moments
        moments = cv2.moments(file)

        # Create a list with the features extracted
        hu_moments = cv2.HuMoments(moments)
        new_moments = [moment[0] for moment in hu_moments]
        print(new_moments)

        complete_hu_moments.append(new_moments)

    print('\n')

    return complete_hu_moments


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

    # Extract HU Moments
    features = extract_hu_moments(image_paths)

    # Save the results in a csv file.
    save_results('HUMoments', features)