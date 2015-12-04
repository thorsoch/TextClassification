#svmmaker
# takes in parameters and trains a svm model with those parameters

import sklearn
from sklearn import svm
from sklearn import grid_search, datasets
import csv
import random
import numpy as np
import pickle

print("allfeatures.csv is opening")

with open("allfeatures.csv", 'rU') as f:  #opens PW file
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
	print(z2)

print("Training 50 Model")

clf = svm.SVC(kernel = 'linear', C = 50, verbose = True) 
#clf = svm.SVC(kernel = 'rbf', decision_function_shape='ovo', C = INSERT_HERE, gamma = INSERT_HERE) 

ok = clf.fit(X, Y)

print("Writing 50 Model")

with open("goodSVM_linear50", "wb") as f:
	pickle.dump(ok, f)

print("Training 75 Model")

clf = svm.SVC(kernel = 'linear', C = 75, verbose = True)

ok = clf.fit(X, Y)

print("Writing 75 Model")

with open("goodSVM_linear75", "wb") as f:
	pickle.dump(ok, f)

print("Training 500 Model")

clf = svm.SVC(kernel = 'linear', C = 500, verbose = True)

ok = clf.fit(X, Y)

print("Writing 500 Model")

with open("goodSVM_linear500", "wb") as f:
	pickle.dump(ok, f)

print("Training 1000 Model")

clf = svm.SVC(kernel = 'linear', C = 1000, verbose = True)

ok = clf.fit(X, Y)

print("Writing 1000 Model")

with open("goodSVM_linear1000", "wb") as f:
	pickle.dump(ok, f)

print("Script Complete")
