.PHONY: initialcounts trimmedcounts wordmatrix propmatrix

initialcounts:
	python parse.py
trimmedcounts:
	python importcsv.py
wordmatrix:
	python wordmatrix.py
propmatrix:
	python propmatrix.py