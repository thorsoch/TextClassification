#svmmaker
# takes in parameters and trains a svm model with those parameters

import sklearn
from sklearn import svm
from sklearn import grid_search, datasets
import csv
import random
import numpy as np
import pickle

# Open up the training set.

print("trainingword.csv is opening")

with open("trainingword.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	matrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

print("Splitting labels and predictors")
file_names =[]
X = [] # X = matrix of train
Y = [] # Y = class Values

z = 0
for row in matrix:
	if z == 0:
		z = 1
		continue
	X += [row[:-2]]
	Y += [row[-1]]
	file_names += [row[-2]]

print("Changing strings into numbers")

Y = map(int, Y)
z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1

print("Training c = 7.4, gamma = 81.667 Model")

clf = svm.SVC(kernel = 'rbf', C = 7.4, gamma = 81.667, verbose = True)

ok = clf.fit(X, Y)

# Change the model name.

print("Writing c = 7.4, gamme = 81.667 Model")

with open("goodSVM_radial_7_4_81667_word", "wb") as f:
	pickle.dump(ok, f)

print("Script Complete")
