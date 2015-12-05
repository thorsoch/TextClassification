import sklearn
from sklearn import svm
from sklearn import grid_search, datasets
import csv
import random
import numpy as np
import pickle

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
  {'C': [75, 100, 150], 'kernel': ['linear']}
  # ,
  # {'C': list(np.logspace(-1, 1, 5)), 'gamma': list(np.logspace(-1, 1, 5)), 'kernel': ['rbf']}
 ]

size = len(X)
ind = random.sample(range(size), size/5)
sampleX = [X[x] for x in ind]
sampleY = [Y[x] for x in ind]

svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, param_grid, cv = 5, verbose = 4)

# def garb(a):
#  	return int(round(random.random()*len(X))) - 1

# randomIndexTrain = map(garb, range(500))
# randomIndexTest = map(garb, range(20))
# xtrain = [X[i] for i in randomIndexTrain]
# ytrain = [Y[i] for i in randomIndexTrain]
# xtest = [X[i] for i in randomIndexTest]
# ytest = [Y[i] for i in randomIndexTest]

#ok = clf.fit(xtrain, ytrain)
# """ 
# This does the crossvalidation. It will take a long time. The ok variable contains
# the best parameters which can be accessed by ok.best_params_.
# ok.predict(X) can be run on a test set.
# """

print("Beginning Cross Validation")

ok = clf.fit(sampleX, sampleY)

print("Cross Validation complete.")

print("Writing out object")

with open("svm_linear_word_CV_0", "wb") as f:
	pickle.dump(ok, f)

print("Best Score is: ")
print(ok.best_score_)

print("Best Parameters are: ")
print(ok.best_params_)

print("Grid Scores are: ")
print(ok.grid_scores_)

print("Script complete.")



# def garb(a):
# 	return int(round(random.random()*len(X))) - 1

# randomIndexTrain = map(garb, range(10000))
# randomIndexTest = map(garb, range(20))
# xtrain = [X[i] for i in randomIndexTrain]
# ytrain = [Y[i] for i in randomIndexTrain]
# xtest = [X[i] for i in randomIndexTest]
# ytest = [Y[i] for i in randomIndexTest]

# clf.fit(xtrain, ytrain)
# clf.predict(xtest)

