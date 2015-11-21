.PHONY: initialcounts trimmedcounts

initialcounts:
	python parse.py
trimmedcounts:
	python importcsv.py