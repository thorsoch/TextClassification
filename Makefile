.PHONY: initialcounts trimmedcounts wordmatrix powerparse powercounts powermatrix stemparse stemcounts stemmatrix

initialcounts:
	python parse.py
trimmedcounts:
	python importcsv.py
wordmatrix:
	python wordmatrix.py
stemparse:
	ipython stemparse.py
stemcounts:
	ipython stemimportcsv.py
stemmatrix:
	ipython stemwordmatrix.py
powerparse:
	ipython powerparse.py
powercounts:
	ipython powerimportcsv.py
powermatrix:
	ipython powerwordmatrix.py