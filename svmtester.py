#svmtester
# takes in parameters and trains a svm model with those parameters

import sklearn
from sklearn import svm
from sklearn import grid_search, datasets
import csv
import random
import numpy as np
import pickle
import re

print("practiceword.csv is opening")

with open("practiceword.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	testmatrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

with open("goodSVM_radial_15_15", "rb") as f: #"goodSVM"
	goodmodel = pickle.load(f)

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

print("Changing strings into numbers")
z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1
	print(z2)

print("Predicting labels")

predicted = goodmodel.predict(X)

def numonly(x):
	return int(re.sub("[^0-9]", "", x))

print("Cleaning up text file names.")

file_names = map(numonly, file_names)

print("Resorting file names and labels")

final = zip(file_names, list(predicted))
final.sort()
x = map(list, final)

x = [["id", "category"]] + x

print("Writing out practicesvmpred_radial_15_15.csv")

with open("practicesvmpred_radial_15_15.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(x)
	
print("Script complete.")


