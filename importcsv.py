import csv 
import sys
import pickle
csv.field_size_limit(sys.maxsize)

with open("child.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataChild = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

with open("history.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataHistory = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

with open("religion.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataReligion = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

with open("science.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataScience = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

summ = [int(a)+int(b) for (a, b) in zip(dataChild[1], dataHistory[1])]
summ = [int(a)+int(b) for (a, b) in zip(summ, dataReligion[1])]
summ = [int(a)+int(b) for (a, b) in zip(summ, dataScience[1])]

with open("allwords", 'rb') as f:
	cleanwords = pickle.load(f)

cleanwords.sort()

freqBar = 10
wordslen = len(cleanwords) + 1
indall = range(0, wordslen)
index = [i for (i, j) in zip(indall, summ) if j > freqBar] # Selects all the indices of frequency > freqBar

childCounts = [int(a) for a in dataChild[1]]
historyCounts = [int(a) for a in dataHistory[1]]
religionCounts = [int(a) for a in dataReligion[1]]
scienceCounts = [int(a) for a in dataScience[1]]

def makeCutCsv(counts, name, summ):
	wordslen = len(cleanwords) + 1
	indall = range(0, wordslen)
	index = [i for (i, j) in zip(indall, summ) if j > 10]
	finalMatrix = [[cleanwords[i] for i in index], [counts[i] for i in index]]

	with open(name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalMatrix)

makeCutCsv(childCounts, "childCut.csv", summ)
makeCutCsv(historyCounts, "historyCut.csv", summ)
makeCutCsv(religionCounts, "religionCut.csv", summ)
makeCutCsv(scienceCounts, "scienceCut.csv", summ)
makeCutCsv(summ, "totals.csv", summ)


