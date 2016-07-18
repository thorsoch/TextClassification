import csv 
import sys
import pickle
csv.field_size_limit(sys.maxsize)

"""
This file is used to parse text files to create a csv which will contain the counts of all words across all files.

Call this file as "python importcsv.py MIN MAX FILES..."

MIN: The minimum frequency a word requires to be contained.
MAX: The maximum frequency a word can have without being omitted.
FILES...: The csv files made by parse.py you would like to include.
"""

def makeCutCsv(counts, name, summ, freqBarU = 0, freqBarT = 1000000):
	wordslen = len(cleanwords) + 1
	indall = range(0, wordslen)
	index = [i for (i, j) in zip(indall, summ) if j > freqBarU and j < freqBarT]
	finalMatrix = [[cleanwords[i] for i in index], [counts[i] for i in index]]

	with open(name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalMatrix)

if __name__ == "__main__":
	cmdargs = sys.argv
	MIN = cmdargs[1] # The minimum frequency we count.
	MAX = cmdargs[2]
	files = cmdargs[3:]
	if len(cmdargs) < 3:
		print("Error: Incorrect number of arguments.")
		raise Exception

	all_data = {}
	file_names = []
	first = True
	for fi in files:
		with open(fi, 'rU') as f:
			reader = csv.reader(f)
			data = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists
			all_data[fi] = [int(a) for a in data[1]]
			file_names += [fi]
			if first:
				summ = data[1]
			else:
				summ = [int(a) + int(b) for (a, b) in zip(summ, data[1])]
		first = False

	print("Opening allwords")
	with open("allwords", 'rb') as f:
		cleanwords = pickle.load(f)

	print(cleanwords)

	print("setting up logistics")
	cleanwords.sort()

	print(all_data)

	for fi in file_names:
		makeCutCsv(all_data[fi], fi + "2", summ, MIN, MAX)

	print("Script complete")
