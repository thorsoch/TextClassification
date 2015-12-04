.PHONY: initialcounts trimmedcounts wordmatrix powerparse powercounts powermatrix
		stemparse stemcounts stemmatrix custommatrix1 testmatrix testmatrixstem
		testmatrixcustom testmatrixpower svmmodel filteredmatrixword filteredmatrixpower
		svmmaker

initialcounts:
	python parse.py
trimmedcounts:
	python importcsv.py
wordmatrix:
	python wordmatrix.py
powerparse:
	ipython powerparse.py
powercounts:
	ipython powerimportcsv.py
powermatrix:
	ipython powerwordmatrix.py
stemparse:
	ipython stemparse.py
stemcounts:
	ipython stemimportcsv.py
stemmatrix:
	ipython stemwordmatrix.py
custommatrix:
	ipython custommatrix.py
testmatrix:
	ipython testwordmatrix.py
testmatrixstem:
	ipython teststemmatrix.py
testmatrixcustom:
	ipython testcustommatrix.py
testmatrixpower:
	ipython testpowermatrix.py
svmmodel:
	ipython svm.py
filteredmatrixword:
	ipython filteredwordmatrix.py
filteredmatrixpower:
	ipython filteredpowermatrix.py
svmmaker:
	ipython svmmaker.py



