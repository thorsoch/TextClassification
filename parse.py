from collections import Counter
import os
import glob
import re
import csv
import pickle
from bisect import bisect_left
import sys

"""
This file is used to parse text files to create a csv which will contain the counts of all words across all files.

Call this file as "python parse.py FOLDER_PATH CLASSNUM"
FOLDER_PATH: Path to folder containing the text files.
CLASSNUM (optional): The class to which this set of input files belong. Must be an integer.
"""

cmdargs = sys.argv
FILE_PATH = cmdargs[1]
freqBarU = 2508
freqBarT = 130000
if len(cmdargs) == 3:
	CLASSNUM = int(cmdargs[2])
else:
	CLASSNUM = 0
if len(cmdargs) > 3 or len(cmdargs) < 2:
	print("Error: Incorrect number of arguments.")
	raise Exception

# Prepare the path for all .txt files. 

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, FILE_PATH, "*.txt")

# Function that opens the file at PATH, 
# parses out words, and returns them as
# lower case and splitted.

def parse(path, lower=True):
	file = open(path)
	text = file.read()
	if lower:
		words = text.lower().split()
		words = list(map(remSym, words))
	else:
		words = text.split()
		words = list(map(remSym2, words))
	words = list(filter(removeLength, words))
	return words

# Takes input x, and removes all characters not a lower case alphabet.

def remSym(x):
	return re.sub("[^a-z]", "", x)
def remSym2(x):
	return re.sub("[^a-zA-Z]", "", x)

# Checks if a word is not in the list of words to remove. 

def removeFilter(removelist):
	def wordFilter(x):
		return x not in removelist
	return wordFilter

# Checks for valid word length

def removeLength(word):
	if len(word) < 1 or len(word) > 20:
		return False
	return True

# Creates word list by calling functions above.

def makeWordList():
	wordlist = []
	mainwordlist = []
	count = 0
	i = 0
	for file in glob.glob(txt_path):
		new_wordlist = parse(file)
		wordlist += new_wordlist
		wordlist = list(set(wordlist))
		if i > 100:
			mainwordlist += wordlist
			wordlist = []
			i = 0
		i += 1
		count += 1
	mainwordlist += wordlist
	return list(set(mainwordlist))

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
	hi = hi if hi is not None else len(a) # hi defaults to len(a)   
	pos = bisect_left(a,x,lo,hi)          # find insertion position
	return (pos if pos != hi and a[pos] == x else -1)

# Returns a list of words to remove.

def removeWords():
	remove = open('remove.txt')
	removewords = remove.read()
	removewords = removewords.split(",")
	return removewords

# Takes in all the words and makes a matrix of the frequency of words in each document.

def makeMatrix(all_words):
	all_words.sort()
	matrix = [all_words + ["FILE"] + ["CLASS"]]
	rowLength = len(all_words)
	i = 0
	j = 0
	for path in paths:
		for file in glob.glob(path):
			row = [0] * (rowLength + 2)
			new_wordlist = parse(file)
			d = Counter(new_wordlist)
			for key in d:
				pos = binary_search(all_words, key, 0, rowLength)
				if pos > -1:
					row[pos] = d[key]
			row[-1] = j # This number assigns class
			row[-2] = re.search('[0-9]+\.txt', file).group() # Extracts file name (Ex: "123.txt")
			matrix += [row]
			i += 1
			print(path[-20:] + " on iteration " + str(i))
		j += 1
	return matrix

# Takes in all the words, and makes a count of every word in all the files of designated path

def makeCount(all_words, path, classnum):
	all_words.sort()
	matrix = all_words + ["CLASS"]
	rowLength = len(all_words)
	i = 0
	total = [0] * (rowLength + 1)
	total[-1] = classnum
	for file in glob.glob(path):
		row = [0] * (rowLength + 1)
		new_wordlist = parse(file)
		d = Counter(new_wordlist)
		for key in d:
			pos = binary_search(all_words, key, 0, rowLength)
			if pos > -1:
				row[pos] = d[key]
		total = [x + y for x, y in zip(total, row)]
		i += 1
	return [matrix, total]

def makeCutCsv(counts, name, summ):
	wordslen = len(cleanwords) + 1
	indall = range(0, wordslen)
	index = [i for (i, j) in zip(indall, summ) if j > freqBarU and j < freqBarT]
	finalMatrix = [[cleanwords[i] for i in index], [counts[i] for i in index]]

	with open(name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalMatrix)

if __name__ == "__main__":

	print("Making Words")

	words = makeWordList()
	remove = removeWords()
	removefunc = removeFilter(remove)

	print("Removing nonsense words")

	cleanwords = list(filter(removefunc, words))
	with open("allwords", 'wb') as f:
		pickle.dump(cleanwords, f)

	print("cleanwords writing done")

	matrix = makeCount(cleanwords, txt_path, CLASSNUM)

	with open(FILE_PATH + "words.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("Script complete.")
