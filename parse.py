from collections import Counter
import os
import glob
import re
import csv
import pickle
from bisect import bisect_left
import sys

"""
This file is used to parse text files to create csvs which will contain the counts of all words across all files per forlder.

Call this file as "python parse.py FOLDER_PATHS..."
FOLDER_PATHS: Paths to folders containing the text files. The first folder in the list will be given class id 0, the next one will be 1 and so on.
"""

cmdargs = sys.argv
FILE_PATHS = cmdargs[1:]
if len(cmdargs) < 2:
	print("Error: Incorrect number of arguments.")
	raise Exception

# Prepare the path for all .txt files. 

base_path = os.path.abspath(os.path.dirname(__file__))

txt_paths =[]
for path in FILE_PATHS:
	txt_path = [os.path.join(base_path, path, "*.txt")]
	txt_paths += txt_path

print(txt_paths)

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
	for txt_path in txt_paths:
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
	for path in txt_paths:
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

	j = 0
	for path in txt_paths:
		matrix = makeCount(cleanwords, path, j)
		with open(FILE_PATHS[j] + "words.csv", "wb") as f:
			writer = csv.writer(f)
			writer.writerows(matrix)
		j += 1

	print("Script complete.")
