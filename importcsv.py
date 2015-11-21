import csv 
import sys
import pickle
csv.field_size_limit(sys.maxsize)

print("Opening child")

with open("child.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataChild = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

print("Opening history")

with open("history.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataHistory = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Opening religion")

with open("religion.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataReligion = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Opening science")

with open("science.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataScience = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Starting sums")
print("Starting first sum")
summ = [int(a)+int(b) for (a, b) in zip(dataChild[1], dataHistory[1])]
print("Starting second sum")
summ = [int(a)+int(b) for (a, b) in zip(summ, dataReligion[1])]
print("Starting third sum")
summ = [int(a)+int(b) for (a, b) in zip(summ, dataScience[1])]

print("Opening allwords")
with open("allwords", 'rb') as f:
	cleanwords = pickle.load(f)

print("setting up logistics")
cleanwords.sort()

freqBar = 360

print("Making ints for child")
childCounts = [int(a) for a in dataChild[1]]
print("Making ints for history")
historyCounts = [int(a) for a in dataHistory[1]]
print("Making ints for religion")
religionCounts = [int(a) for a in dataReligion[1]]
print("Making ints for science")
scienceCounts = [int(a) for a in dataScience[1]]

def makeCutCsv(counts, name, summ):
	wordslen = len(cleanwords) + 1
	indall = range(0, wordslen)
	index = [i for (i, j) in zip(indall, summ) if j > freqBar]
	finalMatrix = [[cleanwords[i] for i in index], [counts[i] for i in index]]

	with open(name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalMatrix)

print("Making child cuts")
makeCutCsv(childCounts, "childCut.csv", summ)
print("Making history cuts")
makeCutCsv(historyCounts, "historyCut.csv", summ)
print("Making religion cuts")
makeCutCsv(religionCounts, "religionCut.csv", summ)
print("Making science cuts")
makeCutCsv(scienceCounts, "scienceCut.csv", summ)
print("Making totals cuts")
makeCutCsv(summ, "totals.csv", summ)

print("Script complete: 4 cut csvs and totals cut made.")


