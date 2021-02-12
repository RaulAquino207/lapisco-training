import cv2
import os
import glob
import csv
import numpy as np
from skimage import feature

class Extraction():
    def __init__(self, path_image):
        self.path_image = path_image

    def extract_hu_moments(self):
        print('[INFO] Extracting HU Moments.')
        complete_hu_moments = []

        for i, image in enumerate(self.path_image):
            print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(self.path_image)))

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

        self.save_results('HUMoments', complete_hu_moments)
        return complete_hu_moments

    def extract_lbp(self, number_points, radius, eps=1e-7):
        print('[INFO] Extracting LBP.')
        lbp_features = []

        for i, image in enumerate(self.path_image):
            print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(self.path_image)))

            # Load the rgb image
            file = cv2.imread(image)

            # Convert to grayscale
            file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

            # Extract lbp
            lbp = feature.local_binary_pattern(file, number_points, radius, method='uniform')

            # Calculates the histogram of the lbp image
            hist, ret = np.histogram(lbp.ravel(), bins=np.arange(0, number_points + 3), range=(0, number_points + 2))

            hist = hist.astype('float')
            hist /= (hist.sum() + eps)
            # print('hist', hist)

            # Create the feature vector extracted by lbp
            image_lbp = [item for item in list(hist)]

            lbp_features.append(image_lbp)

        print('\n')

        self.save_results('LBP', lbp_features)
        return lbp_features

    def extract_glcm(self, distances, angles):
        print('[INFO] Extracting GLCM.')
        glcm_features = []

        for i, image in enumerate(self.path_image):
            print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(self.path_image)))

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

        self.save_results('GLCM', glcm_features)
        return glcm_features

    def save_results(self, extractor_name, features):

        # Show the extracted features in command prompt
        for vector in features:
            print(vector)

        # Save all features in a csv file
        with open(extractor_name + '.csv', 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(features)