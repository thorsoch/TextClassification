.PHONY: initialcounts trimmedcounts wordmatrix powerparse powercounts powermatrix
		stemparse stemcounts stemmatrix custommatrix1 testmatrix testmatrixstem
		testmatrixcustom testmatrixpower svmmodel filteredmatrixword filteredmatrixpower
		svmmaker svmtester trainingwordfeatures svmmodelradial boostmodelCV svmmodellinearwordCV
		svmmodellinearpowerCV svmmodelradialwordCV svmmodelradialpowerCV

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
svmmodellinearCV:
	ipython svm.py
filteredmatrixword:
	ipython filteredwordmatrix.py
filteredmatrixpower:
	ipython filteredpowermatrix.py
svmmaker:
	ipython svmmaker.py
svmtester:
	ipython svmtester.py
trainingwordfeatures:
	ipython parse.py
	ipython importcsv.py
	ipython filteredwordmatrix.py
svmmodelradialCV:
	ipython svmradial.py
boostmodelCV:
	ipython boost.py
svmmodellinearwordCV:
	ipython svmlinearword.py
svmmodellinearpowerCV:
	ipython svmlinearpower.py
svmmodelradialwordCV:
	ipython svmradialword.py
svmmodelradialpowerCV:
	ipython svmradialpower.py
boostmodelwordCV:
	ipython boostword.py
boostmodelpowerCV:
	ipython boostpower.py
boostmaker:
	ipython boostmaker.py
boostmakerwordpower:
	ipython boostmakerwordpower.py
boosttester:
	ipython boosttester.py
svmmakerradial:
	ipython svmmakerradial.py
svmmakerradial2:
	ipython svmmakerradial2.py
svmmodelradial2CV:
	ipython svmradial2.py
svmmodelradial3CV:
	ipython svmradial3.py
svmmodelradial4CV:
	ipython svmradial4.py
svmmodelradial5CV:
	ipython svmradial5.py	
svmmodelradial6CV:
	ipython svmradial6.py
svmmodelradialword2CV:
	ipython svmradialword2.py



