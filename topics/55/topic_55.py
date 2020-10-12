'''
Usar o método de classificação pelo vizinho mais próximo (KNN em inglês) usando a biblioteca de Machine Learning da OpenCv.
Deve-se fazer com os métodos Hold Out e Leave One Out. Tudo deve ser feito utilizando a estrutura Mat da OpenCv.
'''

import cv2
import numpy as np
import math
import pandas as pd
import operator
import csv


def hold_out(df, train_size, shuffle=True):

    # Shuffle the dataframe if the shuffle is set to true
    if shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    # Convert the rows of the dataframe into a list of lists
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    # Split the data into train and test
    X_train = data[:int(train_size*len(data))]
    X_test = data[int(train_size*len(data)):]

    # Get the correspondent labels to each feature vector
    y_train = [int(x[-1]) for x in X_train]
    y_test = [int(x[-1]) for x in X_test]

    # Remove the labels from the train and test vectors
    X_train = [x[:-1] for x in X_train]
    X_test = [x[:-1] for x in X_test]

    return X_train, X_test, y_train, y_test


def leave_one_out(df, shuffle=True):

    # Shuffle the dataframe if the shuffle is set to true
    if shuffle:
        df = df.sample(frac=1).reset_index(drop=True)

    # Convert the rows of the dataframe into a list of lists
    data = []
    for row in df.iterrows():
        index, values = row
        data.append(values.tolist())

    # Create a list of lists, in which each iteration of leave one out will be stored
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    for i in range(len(data)):
        train = data.copy()
        train.remove(data[i])

        test = data[i]

        # Get the correspondent labels to each feature vector
        y_train.append([int(x[-1]) for x in train])
        y_test.append(int(test[-1]))

        # Remove the labels from the train and test vectors
        X_train.append([x[:-1] for x in train])
        X_test.append(test[:-1])

    return X_train, X_test, y_train, y_test


def read_data(file):
    # Load the features of a file in a dataframe
    return pd.read_csv(file, sep=',', header=None)


def euclidean_dist(x1, x2):
    dist = 0.0
    for x, y in zip(x1, x2):
        dist += pow(float(x) - float(y), 2)
    dist = math.sqrt(dist)

    return dist


def knn_clf(X_train, X_test, y_train, k_neighbors=3):
    assert (k_neighbors % 2), 'Number of neighbors must be odd!'

    predict = []
    for x1 in X_test:
        class_prediction = np.zeros(max(y_train) + 1)
        euclidean_distance = []

        for x2, label2 in zip(X_train, y_train):
            eu_dist = euclidean_dist(x1, x2)
            euclidean_distance.append((label2, eu_dist))
            euclidean_distance.sort(key=operator.itemgetter(1))
            smaller_k_distances = euclidean_distance[:k_neighbors]

            for label, dist in smaller_k_distances:
                class_prediction[int(label)] += 1

        predict.append(max(range(len(class_prediction)), key=class_prediction.__getitem__))

    return predict


if __name__ == '__main__':

    # Read the file with the features to classify
    filename = 'features.txt'
    features = read_data(filename)

    # Split the database using hold out
    X_train, X_test, y_train, y_test = hold_out(features, train_size=0.9)

    # Reshape train label data to fit the format of opencv
    y_train = np.reshape(y_train, (-1, 1))

    # Apply knn (you can change the number of neighbors)
    knn = cv2.ml.KNearest_create()
    knn.train(np.asarray(X_train, np.float32), cv2.ml.ROW_SAMPLE, y_train)

    # Predict in the test data (you can vary the number of k)
    ret, results, neighbors, dist = knn.findNearest(np.asarray(X_test, np.float32), k=3)

    # Convert the results to a list
    predictions = [int(x) for x in results]

    # Calculates the accuracy using hold out
    count = 0
    for x, y in zip(y_test, predictions):
        if x == y:
            count += 1

    accuracy = count/len(y_test)
    print('Accuracy using hold out: {:.4f}'.format(accuracy))

    # Save the true and the predicted labels to use in question 59 and 60
    with open('true_and_predict_55.csv', 'w') as outfile:
        rows = [y_test, predictions]
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(rows)

    # Split the database using leave one out
    X_train, X_test, y_train, y_test = leave_one_out(features)

    # Apply knn (you can change the number of neighbors)
    predictions = np.zeros(int(max(y_train[0])) + 1)
    count = 0
    for train_set, test_set, label_train, label_test in zip(X_train, X_test, y_train, y_test):

        # Reshape train label data to fit the format of opencv
        label_train = np.reshape(label_train, (-1, 1))

        knn = cv2.ml.KNearest_create()
        knn.train(np.asarray(train_set, np.float32), cv2.ml.ROW_SAMPLE, label_train)

        # Predict in the test data (you can vary the number of k)
        test_list = []
        test_list.append(test_set)
        ret, results, neighbors, dist = knn.findNearest(np.asarray(test_list, np.float32), k=3)

        if results[0] == label_test:
            count += 1

    accuracy = count / len(y_test)

    print('Accuracy using leave one out: {:.4f}'.format(accuracy))