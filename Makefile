.PHONY: initialcounts trimmedcounts wordmatrix

initialcounts:
	python parse.py
trimmedcounts:
	python importcsv.py
wordmatrix:
