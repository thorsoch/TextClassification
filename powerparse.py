from collections import Counter
import os
import glob
import re
import csv
import pickle
import numpy as np
from bisect import bisect_left

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.collocations import *

# Prepare the path for all .txt files. 

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, "Training", "*", "*.txt")

tokenizer = RegexpTokenizer(r'\w+')
bigram_measures = nltk.collocations.BigramAssocMeasures()

# Create category paths seperately, in case we need them. 

child_path = os.path.join(base_path, "Training", "Child_0", "*.txt")
history_path = os.path.join(base_path, "Training", "History_1", "*.txt")
religion_path = os.path.join(base_path, "Training", "Religion_2", "*.txt")
science_path = os.path.join(base_path, "Training", "Science_3", "*.txt")

paths = [child_path, history_path, religion_path, science_path]

# Function that opens the file at PATH, 
# parses out words, and returns them as
# lower case and splitted.

def parse(path):
	file = open(path)
	text = file.read()
	words = [t.lower() for t in tokenizer.tokenize(text)] #Puctuation removal
	words = list(filter(removeLength, words))

	finder = BigramCollocationFinder.from_words(words)
	scored = finder.score_ngrams(bigram_measures.raw_freq)
	scored.sort()

	return scored

# Takes input x, and removes all characters not a lower case alphabet.

def remSym(x):
	return re.sub("[^a-z]", "", x)

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
	# wordlist = []
	mainwordlist = {}
	count = 0
	i = 0
	for file in glob.glob(txt_path):
		new_wordlist = [i[0] for i in parse(file)] #[(1,2), (1,3)...]
		# wordlist += new_wordlist
		# wordlist = list(set(wordlist))
		# if i > 100:
		# 	mainwordlist += wordlist
		# 	wordlist = []
		# 	i = 0
		# i += 1
		for tuple in new_wordlist:
			mainwordlist[tuple] = 1
		count += 1
		print("Appending tuples from file: " + str(count))
	print("Done with for loop over all files")
	# print("Appending last wordlist")
	# mainwordlist += wordlist
	print("Length of mainwordlist:")
	mainlen = len(mainwordlist)
	print(mainlen)
	print("First five")
	print(mainwordlist.keys()[:5])
	print("Last five")
	print(mainwordlist.keys()[-5:])
	print("Making mainwordlist unique")
	# keys = {}
	# term = 0
	# for tuple in mainwordlist:
	# 	keys[tuple] = 1
	# 	term += 1
	# 	print("Added tuple " + str(term) + " out of " + str(mainlen))
	return mainwordlist.keys()

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
	matrix = [all_words + ["CLASS"]]
	rowLength = len(all_words)
	i = 0
	total = [0.0] * (rowLength + 1)
	total[-1] = classnum
	for file in glob.glob(path):
		row = [0.0] * (rowLength + 1)
		new_wordlist = parse(file)
		for item in new_wordlist:
			pos = binary_search(all_words, item[0], 0, rowLength)
			if pos > -1:
				row[pos] = item[1]
		total = [x + y for x, y in zip(total, row)]
		i += 1
		print(path[-20:] + " on iteration " + str(i))
	return [matrix, total]

# def makeCount2(all_words, path, classnum):
# 	matrix = [all_words + ["CLASS"]]
# 	total = np.array([0.0] * len(all_words))
# 	count = 1
# 	for file in glob.glob(path):
# 		new_worddict = dict(parse(file))
# 		total += np.array([new_worddict.get(tuple, 0.0) for tuple in all_words])
# 		print("Added normalized counts of file: " + str(count))
# 		count += 1
# 	print("Finished all file counts.")
# 	total = total.tolist()
# 	total.append(classnum)
# 	return [matrix, total]

if __name__ == "__main__":

	print("Making Words")

	words = makeWordList()

	print("Finished making words, writing out now")

	with open("allwordsBi", 'wb') as f:
		pickle.dump(words, f)

############################################

	# print("Opening allwordBi")

	# with open("allwordsBi", 'rb') as f:
	# 	words = pickle.load(f)

############################################

	print("words writing done. starting child")

	#finalmatrix = makeMatrix(cleanwords)
	#print("matrix done")
	matrix = makeCount(words, child_path, 0)

	print("writing out child")

	with open("childpower.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("child writing done. starting history")

	matrix = makeCount(words, history_path, 1)

	print("writing out history")

	with open("historypower.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("history writing done. starting religion")

	matrix = makeCount(words, religion_path, 2)

	print("writing out religion")

	with open("religionpower.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("religion writing done. starting science")

	matrix = makeCount(words, science_path, 3)

	print("writing out science")

	with open("sciencepower.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("science writing done.")

	print("Done writing out: cleanword & 4 word counts.")

	print("Script complete.")

#with open("allwords", 'wb') as f:
	#pickle.dump(my_list, f)
#with open("allwords", 'rb') as f:
#    my_list = pickle.load(f)
