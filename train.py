import os
from random import shuffle
from sklearn import svm, neighbors
import pickle
import numpy as np
import pandas as pd
import warnings

encoding_file_path = './encoded-images-data.csv'
labels_fName = 'labels.pkl'

if os.path.isfile(encoding_file_path):
    df = pd.read_csv(encoding_file_path)
else:
    warnings.warn('{} does not exist'.format(encoding_file_path))
    quit()

if os.path.isfile(labels_fName):
    with open(labels_fName, 'rb') as f:
        le = pickle.load(f)
else:
    warnings.warn('{} does not exist'.format(labels_fName))
    quit()

# Read the dataframe into a numpy array
# shuffle the dataset
full_data = np.array(df.astype(float).values.tolist())
shuffle(full_data)

# Extract features and labels
# remove id column (0th column)
X = np.array(full_data[:, 1:-1])
y = np.array(full_data[:, -1:])

# fit the data into a support vector machine
# clf = svm.SVC(C=1, kernel='poly', probability=True)
clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf.fit(X, y.ravel())

# save the classifier pickle
fName = "classifier.pkl"
print("Saving classifier to '{}'".format(fName))
with open(fName, 'wb') as f:
    pickle.dump((le, clf), f)
