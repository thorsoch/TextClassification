.PHONY: initialcounts trimmedcounts wordmatrix powerparse powercounts powermatrix stemparse stemcounts stemmatrix custommatrix1 testmatrix testmatrixstem

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

