import csv 
import sys
import pickle
csv.field_size_limit(sys.maxint)

print("Opening child")

with open("childpower.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataChild = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists

print("Opening history")

with open("historypower.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataHistory = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Opening religion")

with open("religionpower.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataReligion = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Opening science")

with open("sciencepower.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	dataScience = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

print("Starting sums")
print("Starting first sum")
summ = [float(a)+float(b) for (a, b) in zip(dataChild[1], dataHistory[1])]
print("Starting second sum")
summ = [float(a)+float(b) for (a, b) in zip(summ, dataReligion[1])]
print("Starting third sum")
summ = [float(a)+float(b) for (a, b) in zip(summ, dataScience[1])]

print("Opening allwords")
with open("allwordsBi", 'rb') as f:
	cleanwords = pickle.load(f)

print("setting up logistics")
cleanwords.sort()
cleanwords += ["CLASS"]

freqBarU = 0.64 #0.22442 for 10000 bigrams, 0.64 for 3000 bigrams
#freqBarT = 130000

print("Making ints for child")
childCounts = [float(a) for a in dataChild[1]]
print("Making ints for history")
historyCounts = [float(a) for a in dataHistory[1]]
print("Making ints for religion")
religionCounts = [float(a) for a in dataReligion[1]]
print("Making ints for science")
scienceCounts = [float(a) for a in dataScience[1]]

def makeCutCsv(counts, name, summ):
	wordslen = len(cleanwords) + 1
	indall = range(0, wordslen)
	index = [i for (i, j) in zip(indall, summ) if j > freqBarU]
	finalMatrix = [[cleanwords[i] for i in index], [counts[i] for i in index]]

	with open(name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalMatrix)

print("Making child cuts")
makeCutCsv(childCounts, "childpowerCut.csv", summ)
print("Making history cuts")
makeCutCsv(historyCounts, "historypowerCut.csv", summ)
print("Making religion cuts")
makeCutCsv(religionCounts, "religionpowerCut.csv", summ)
print("Making science cuts")
makeCutCsv(scienceCounts, "sciencepowerCut.csv", summ)
print("Making totals cuts")
makeCutCsv(summ, "totalspower.csv", summ)

print("Script complete: 4 cut csvs and totals cut made.")
