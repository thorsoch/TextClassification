import csv 
import sys
import pickle
csv.field_size_limit(sys.maxint)

print("Opening child")

with open("childstem.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataChild = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

print("Opening history")

with open("historystem.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataHistory = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Opening religion")

with open("religionstem.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataReligion = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Opening science")

with open("sciencestem.csv", 'rU') as f:  #opens PW file
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
with open("allwordsstem", 'rb') as f:
	cleanwords = pickle.load(f)

print("setting up logistics")
cleanwords.sort()
cleanwords += ["CLASS"]

freqBarU = 1864
freqBarT = 160000

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
	index = [i for (i, j) in zip(indall, summ) 	if j > freqBarU and j < freqBarT]
	finalMatrix = [[cleanwords[i] for i in index], [counts[i] for i in index]]

	with open(name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalMatrix)

print("Making child cuts")
makeCutCsv(childCounts, "childstemCut.csv", summ)
print("Making history cuts")
makeCutCsv(historyCounts, "historystemCut.csv", summ)
print("Making religion cuts")
makeCutCsv(religionCounts, "religionstemCut.csv", summ)
print("Making science cuts")
makeCutCsv(scienceCounts, "sciencestemCut.csv", summ)
print("Making totals cuts")
makeCutCsv(summ, "totalsstem.csv", summ)

print("Script complete: 4 cut csvs and totals cut made.")


