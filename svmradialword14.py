import sklearn
from sklearn import svm
from sklearn import grid_search, datasets
import csv
import random
import numpy as np
import pickle
import sys

csv.field_size_limit(sys.maxint)

print("trainingword.csv is opening")

with open("trainingword.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	matrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

print("Splitting labels and predictors")

X = [] # X = matrix of train
Y = [] # Y = class Values

z = 0
for row in matrix:
	if z == 0:
		z = 1
		continue
	X += [row[:-2]]
	Y += [row[-1]]

# clf = svm.SVC(kernel = 'linear') #'rbf' has gamma parameter
# Cost
# clf = svm.SVC(kernel = 'rbf', decision_function_shape='ovo') 
# Gamma and Cost
# This is for radial (I think, not actually sure)

print("Changing strings into numbers")

Y = map(int, Y)
z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1
	print(z2)

# clf.predict(Matrix for test)

# Change the stuff below to test various ways
# parameters = {'kernel':('linear', 'rbf'), 'C':[1,10], 'gamma':[1,10]}

print("Setting up logistics for CV")

param_grid = [
  {'C': [8.67], 'gamma': [80], 'kernel': ['rbf']}
 ]

print("Creating Stratified Sample")

samp_prop = 0.1
n = len(X) * samp_prop

child_n = round(n * 7164/22308)
history_n = round(n * 5352/22308)
religion_n = round(n * 2361/22308)
science_n = round(n * 7431/22308)

child_ind = random.sample(range(7164), int(child_n))
history_ind = random.sample(range(7164, 12516), int(history_n))
religion_ind = random.sample(range(12516, 14877), int(religion_n))
science_ind = random.sample(range(14877, 22308), int(science_n))

ind = child_ind + history_ind + religion_ind + science_ind
sampleX = [X[x] for x in ind]
sampleY = [Y[x] for x in ind]


svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, param_grid, cv = 5, verbose = 4)

#size = len(X)

print("Beginning Cross Validation")
#ind = random.sample(range(size), size/10)
#sampleX = [X[x] for x in ind]
#sampleY = [Y[x] for x in ind]

ok = clf.fit(X, Y)

print("Cross Validation complete.")

# print("Writing out object")

# with open("svm_radial_word_CV_0", "wb") as f:
# 	pickle.dump(ok, f)

print("Best Score is: ")
print(ok.best_score_)

print("Best Parameters are: ")
print(ok.best_params_)

print("Grid Scores are: ")
print(ok.grid_scores_)

print("Script complete.")