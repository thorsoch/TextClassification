import os
import csv
import glob
import parse
from collections import Counter
import re


# Prepare path for all test .txt files.

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, "Practice", "*.txt")

print("Opening unstemmedpredictors.csv")

with open("unstemmedpredictors.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	pred = list(list(rec) for rec in csv.reader(f, delimiter=','))

# Takes in all the words and makes a matrix of the frequency of words in each document.

def makeMatrix(all_words):
	all_words.sort()
	matrix = [all_words + ["FILE"]]
	rowLength = len(all_words)
	i = 0
	for file in glob.glob(txt_path):
		row = [0] * (rowLength + 1)
		new_wordlist = parse.parse(file)
		d = Counter(new_wordlist)
		for key in d:
			pos = parse.binary_search(all_words, key, 0, rowLength)
			if pos > -1:
				row[pos] = d[key]
		row[-1] = re.search('[0-9]+\.txt', file).group() # Extracts file name (Ex: "123.txt")
		matrix += [row]
		i += 1
		print(txt_path[-20:] + " on iteration " + str(i))
	return matrix

pred2 = [item for sublist in pred for item in sublist]

print("Starting to make word matrix.")

finalmat = makeMatrix(pred2)

print("Making proportion matrix")

z = 0
rownum = 0
for row in finalmat:
	rownum += 1
	print("Making proportions for file: " + str(rownum))
	if z == 0:
		z += 1
		continue
	rowpart = [int(x) for x in row[0:len(row)-2]]
	totalcount = sum([int(x) for x in rowpart])
	i=0
	if totalcount != 0:
		for val in rowpart:
			row[i] = val/(totalcount*1.0)
			i += 1

with open("testfilteredprop.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)

print("Script complete.")


