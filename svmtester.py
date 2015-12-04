#svmtester
# takes in parameters and trains a svm model with those parameters

import sklearn
from sklearn import svm
from sklearn import grid_search, datasets
import csv
import random
import numpy as np
import pickle

print("allfeaturestest.csv is opening")

with open("allfeaturestest.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	testmatrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

with open("goodSVM", "rb") as f: #"goodSVM"
	goodmodel = pickle.load(f)

print("Changing strings into numbers")

print("Splitting labels and predictors")
file_names =[]
X = [] # X = matrix of train

z = 0
z2 = 0
for row in testmatrix:
	if z == 0:
		z = 1
		continue
	X += [row[:-1]]
	file_names += [row[-1]]
	z2 += 1
	print(z2)

z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1
	print(z2)

predicted = goodmodel.predict(X)

def numonly(x):
	return int(re.sub("[^0-9]", "", x))

file_names = map(numonly, file_names)

final = zip(file_names, list(predicted))
final.sort()
x = map(list, final)

x = [["id", "category"]] + x

with open("testsvmpredictions.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(x)
	


