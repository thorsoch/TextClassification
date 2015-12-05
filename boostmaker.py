#svmmaker
# takes in parameters and trains a svm model with those parameters

import sklearn
import csv
import random
import sklearn
from sklearn import grid_search, datasets
from sklearn.ensemble import GradientBoostingClassifier
import csv
import random
import pickle

print("trainingwordpower.csv is opening")

with open("trainingword.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	matrix1 = list(list(rec) for rec in csv.reader(f, delimiter=','))

with open("trainingwordpower.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	matrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

with open("traningpower.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	matrix2 = list(list(rec) for rec in csv.reader(f, delimiter=','))

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

file_names1 =[]
X1 = [] # X = matrix of train
Y1 = [] # Y = class Values

z = 0
for row in matrix1:
	if z == 0:
		z = 1
		continue
	X1 += [row[:-2]]
	Y1 += [row[-1]]
	file_names1 += [row[-2]]

file_names2 =[]
X2 = [] # X = matrix of train
Y2 = [] # Y = class Values

z = 0
for row in matrix2:
	if z == 0:
		z = 1
		continue
	X2 += [row[:-2]]
	Y2 += [row[-1]]
	file_names2 += [row[-2]]

print("Changing strings into numbers")

Y = map(int, Y)
z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1
	print(z2)

Y1 = map(int, Y)
z2 = 0
for row in X:
	X1[z2] = map(float, row)
	z2 += 1
	print(z2)

Y2 = map(int, Y)
z2 = 0
for row in X:
	X2[z2] = map(float, row)
	z2 += 1
	print(z2)

gbc = GradientBoostingClassifier(verbose = 1, learning=0.01, n_estimators=500, max_depth=2)
#clf = svm.SVC(kernel = 'rbf', decision_function_shape='ovo', C = INSERT_HERE, gamma = INSERT_HERE) 

print("Training wordpowermodel")

ok = gbc.fit(X, Y)

print("Writing wordpowermodel")

with open("boostwordpowermodel", "wb") as f:
	pickle.dump(ok, f)

print("Training wordmodel")

ok = gbc.fit(X1, Y1)

print("Writing wordmodel")

with open("boostwordmodel", "wb") as f:
	pickle.dump(ok, f)

print("Training powermodel")

ok = gbc.fit(X2, Y2)

print("Writing powermodel")

with open("boostpowermodel", "wb") as f:
	pickle.dump(ok, f)

print("Script complete.")
