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

print("allfeaturestest.csv is opening")

a = ["trainingword.csv", "trainingwordpower.csv", "trainingpower.csv"]

with open(a[0], 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	testmatrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

with open("goodSVM_radial_7_25", "rb") as f: #"goodSVM"
	goodmodel = pickle.load(f)

print("Splitting labels and predictors")
file_names =[]
classlabel = []
X = [] # X = matrix of train

z = 0
z2 = 0
for row in testmatrix:
	if z == 0:
		z = 1
		continue
	X += [row[:-2]]
	file_names += [row[-2]]
	classlabel += [row[-1]]
	z2 += 1

classlabel = map(int, classlabel)

print("Changing strings into numbers")
z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1

print("Predicting labels")

predicted = goodmodel.predict(X)

def numonly(x):
	return int(re.sub("[^0-9]", "", x))

print("Cleaning up text file names.")

predicted = list(map(int, list(predicted))

confusion = [[0,0,0,0]]*4

# rows are predicted, columns are actual

for i in range(len(predicted)):
	confusion[classlabel[i]][predicted[i]] += 1

#inclass error rate and total error rate

Terror = 1 - (confusion[0][0] + confusion[1][1] + confusion[2][2] + confusion[3][3])/(len(predicted)*1.0)

Cerror = 1 - (confusion[0][0])/(float(confusion[0][0] + confusion[1][0] + confusion[2][0] + confusion[3][0]))
Herror = 1 - (confusion[1][1])/((confusion[0][1] + confusion[1][1] + confusion[2][1] + confusion[3][1])*1.0)
Rerror = 1 - (confusion[2][2])/((confusion[0][2] + confusion[1][2] + confusion[2][2] + confusion[3][1])*1.0)
Serror = 1 - (confusion[3][3])/((confusion[0][3] + confusion[1][3] + confusion[2][3] + confusion[3][3])*1.0)

print("Total error: " + Terror + " Child error: " + Cerror + " History error: " + Herror + " Religion error: "
	+ Rerror + " Science error: " + Serror)

print("Writing out testsvmpred_linear50.csv")

with open("confusion.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(confusion)

with open("roc.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows([classlabel, predicted])
	
print("Script complete.")

# CHpos = confusion[0][0]/((confusion[0][0] + confusion[1][0] + confusion[2][0] + confusion[3][0])*1.0)
# CHneg = confusion[0][1]/((confusion[0][1] + confusion[1][1])*1.0)

# was child but History
# is child and child


