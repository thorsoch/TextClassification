from collections import Counter
import os
import glob
import re
import csv
import pickle
from bisect import bisect_left

# Prepare the path for all .txt files. 

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, "Training", "*", "*.txt")

# Create category paths seperately, in case we need them. 

child_path = os.path.join(base_path, "Training", "Child(0)", "*.txt")
history_path = os.path.join(base_path, "Training", "History(1)", "*.txt")
religion_path = os.path.join(base_path, "Training", "Religion(2)", "*.txt")
science_path = os.path.join(base_path, "Training", "Science(3)", "*.txt")
sample_path = os.path.join(base_path, "Training", "Sample(4)", "*.txt")

paths = [child_path, history_path, religion_path, science_path]

# Function that opens the file at PATH, 
# parses out words, and returns them as
# lower case and splitted.

def parse(path):
	file = open(path)
	text = file.read()
	words = text.lower().split()
	words = list(map(remSym, words))
	words = list(filter(removeLength, words))
	return words

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
	wordlist = []
	mainwordlist = []
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
			row[-2] = file
			matrix += [row]
		j += 1
	return matrix

# Takes in all the words, and makes a count of every word in all the files of designated path

def makeCount(all_words, path, classnum):
	all_words.sort()
	matrix = [all_words + ["CLASS"]]
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
		print(path[-20:] + "on iteration " + str(i))
	return [matrix, total]

if __name__ == "__main__":

	print("Making Words")

	words = makeWordList()
	remove = removeWords()
	removefunc = removeFilter(remove)

	print("Removing nonsense words")

	cleanwords = list(filter(removefunc, words))

	print("Finished making cleanwords, writing out now")

	with open("allwords", 'wb') as f:
		pickle.dump(cleanwords, f)
	#with open("allwords", 'rb') as f:
		#cleanwords = pickle.load(f)

	print("cleanwords writing done. starting child")

	#finalmatrix = makeMatrix(cleanwords)
	#print("matrix done")
	matrix = makeCount(cleanwords, child_path, 0)

	print("writing out child")

	with open("child.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("child writing done. starting history")

	matrix = makeCount(cleanwords, history_path, 1)

	print("writing out history")

	with open("history.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("history writing done. starting religion")

	matrix = makeCount(cleanwords, religion_path, 2)

	print("writing out religion")

	with open("religion.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("religion writing done. starting science")

	matrix = makeCount(cleanwords, science_path, 3)

	print("writing out science")

	with open("science.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)

	print("science writing done.")

	print("Done writing out: cleanword & 4 word counts.")

#with open("allwords", 'wb') as f:
	#pickle.dump(my_list, f)
#with open("allwords", 'rb') as f:
#    my_list = pickle.load(f)
