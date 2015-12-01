import sklearn
from sklearn import svm
import csv
import random

with open("filterstemmatrix.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	matrix = list(list(rec) for rec in csv.reader(f, delimiter=','))

X = [] # X = matrix of train
Y = [] # Y = class Values

z = 0
for row in matrix:
	if z == 0:
		z = 1
		continue
	X += [row[:-1]]
	Y += [row[-1]]

clf = svm.SVC(kernel = 'linear') #'rbf' has gamma parameter
# clf = svm.SVC(kernel = 'rbf', decision_function_shape='ovo') 
# This is for radial (I think, not actually sure)

def garb2(a):
	return float(a)*1000.0

Y = map(int, Y)
z2 = 0
for row in X:
	X[z2] = map(float, row)
	z2 += 1

# clf.predict(Matrix for test)

# Change the stuff below to test various ways
def garb(a):
	return int(round(random.random()*len(X))) - 1

randomIndexTrain = map(garb, range(10000))
randomIndexTest = map(garb, range(20))
xtrain = [X[i] for i in randomIndexTrain]
ytrain = [Y[i] for i in randomIndexTrain]
xtest = [X[i] for i in randomIndexTest]
ytest = [Y[i] for i in randomIndexTest]

clf.fit(xtrain, ytrain)
clf.predict(xtest)

