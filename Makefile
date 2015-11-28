.PHONY: initialcounts trimmedcounts wordmatrix powerparse

initialcounts:
	python parse.py
trimmedcounts:
	python importcsv.py
wordmatrix:
	python wordmatrix.py
powerparse:
	ipython powerparse.py
powercounts:
	python powerimportcsv.py