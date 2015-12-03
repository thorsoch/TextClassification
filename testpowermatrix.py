import powerparse
import csv
import ast
import os
import glob
from collections import Counter
import re

# Prepare path for all test .txt files.

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, "Practice", "*.txt")

print("Opening bigramspredictors.csv")

with open("bigramspredictors.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	bigrams = list(list(rec) for rec in csv.reader(f, delimiter=','))

# Takes in all the words and makes a matrix of the frequency of words in each document.

def makeMatrix(all_words):
	matrix = [all_words + ["FILE"]]
	rowLength = len(all_words)
	i = 0
	for file in glob.glob(txt_path):
		row = [0.0] * (rowLength + 1)
		new_wordlist = powerparse.parse(file) #[((w,a), 1), 
		for item in new_wordlist:
			pos = powerparse.binary_search(all_words, item[0], 0, rowLength)
			if pos > -1:
				row[pos] = item[1]
		row[-1] = re.search('[0-9]+\.txt', file).group() # Extracts file name (Ex: "123.txt")
		matrix += [row]
		i += 1
		print(txt_path[-20:] + " on iteration " + str(i))
	return matrix

print("Starting makeMatrix()")
a = [item for sublist in bigrams for item in sublist]
a = list(map(ast.literal_eval, a))
finalmat = makeMatrix(a)

print("Writing out testpowerfilteredMatrix.csv")

with open("testpowerfilteredMatrix.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)

print("Script complete.")