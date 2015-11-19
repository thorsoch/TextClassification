from collections import Counter
import os
import glob
import re
import csv

# Prepare the path for all .txt files. 

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, "Training", "*", "*.txt")

# Create category paths seperately, in case we need them. 

child_path = os.path.join(base_path, "Training", "Child(0)", "*.txt")
history_path = os.path.join(base_path, "Training", "History(1)", "*.txt")
religion_path = os.path.join(base_path, "Training", "Religion(2)", "*.txt")
science_path = os.path.join(base_path, "Training", "Science(3)", "*.txt")
sample_path = os.path.join(base_path, "Training", "Sample(4)", "*.txt")

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
	run = 0
	for file in glob.glob(sample_path):
		new_wordlist = parse(file)
		wordlist += new_wordlist
		wordlist = list(set(wordlist))
		if i > 100:
			mainwordlist += wordlist
			wordlist = []
			i = 0
			run += 1
		i += 1
		print(str(i) + " " + str(run))
	mainwordlist += wordlist
	return list(set(mainwordlist))

# Returns a list of words to remove.

def removeWords():
	remove = open('remove.txt')
	removewords = remove.read()
	removewords = removewords.split(",")
	return removewords

# Takes in all the words and makes a matrix of the frequency of words in each document.

def makeMatrix(all_words):
	matrix = [[all_words]]
	rowLength = len(all_words)
	for file in glob.glob(sample_path):
		row = [0] * (rowLength + 1)
		new_wordlist = parse(file)
		d = Counter(new_wordlist)
		for key in d:
			if key in all_words:
				row[all_words.index(key)] = d[key]

		row[-1] = 4 # This number assigns class
		matrix += [row]
	return matrix

if __name__ == "__main__":
	words = makeWordList()
	remove = removeWords()
	removefunc = removeFilter(remove)
	cleanwords = list(filter(removefunc, words))
	finalmatrix = makeMatrix(cleanwords)
	with open("output.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmatrix)


