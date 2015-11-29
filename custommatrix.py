#Power feature matrix
from collections import Counter
import os
import glob
import re
import parse
import nltk
from nltk.corpus import gutenberg

def parsetotext(path):
	file = open(path)
	text = file.read()
	return text

def makePowerMatrix():
	matrix = [["uniquecount", "sentence length", "avg word length", "digit prop", "capital prop",
				"quotation", "question", "exclamation", "noun", "adj", "adv", "verb", "foreign", 
				"preposition", "pronoun", "interjection", "FILE", "CLASS"]]
	rowLength = len(matrix)
	i = 0
	j = 0
	for path in parse.paths: #parse.paths
		for file in glob.glob(path):
			row = [0.0] * 22

			wholetext = parsetotext(file)
			textlist = parse.parse(file)
			textlistNL = parse.parse(file, False) # not lower case
			doclen = len(wholetext)
			wordcount = len(textlist)

			period = wholetext.count(".")
			question = wholetext.count("?")
			exclamation = wholetext.count("!")
			quotations = wholetext.count("'") + wholetext.count('"')
			uniquecount = len(list(set(textlist)))

			num_words = len(gutenberg.words(file))
			num_sents = len(gutenberg.sents(file))

			if wordcount != 0:
				row[0] = uniquecount/(wordcount*1.0)
				lenmap = map(len, textlist)
				row[2] = sum(lenmap)/(wordcount*1.0)
			if num_sents != 0:
				row[1] = round(num_words/num_sents)

			if doclen != 0:
				row[3] = sum(c.isdigit() for c in wholetext)/(doclen*1.0)
				a = [x.isupper() for x in [y[0] for y in textlistNL]]
				row[4] = sum(a)/(doclen*1.0)

			row[5] = quotations
			row[6] = question
			row[7] = exclamation

			text = nltk.word_tokenize(wholetext)
			a = nltk.pos_tag(text)
			tag_fd = nltk.FreqDist(tag for (word, tag) in a)
			a = tag_fd.most_common()
			count = sum([y for (x, y) in a])
			if count != 0:
				row[8] = sum([y for (x, y) in a if x in ["NN", "NNP", "NNPS", "NNS"]])/(count*1.0) #Noun NN NNP NNPS NNS
				row[9] = sum([y for (x, y) in a if x in ["JJ", "JJR", "JJS"]])/(count*1.0) #Adj JJ JJR JJS
				row[10] = sum([y for (x, y) in a if x in ["RB", "RBR", "RBS", "WRB"]])/(count*1.0) #Adv RB RBR RBS WRB
				row[11] = sum([y for (x, y) in a if x in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]])/(count*1.0) #Verb VB VBD VBG VBN VBP VBZ
				row[12] = sum([y for (x, y) in a if x in ["FW"]])/(count*1.0) #foreign
				row[13] = sum([y for (x, y) in a if x in ["IN"]])/(count*1.0) #prepo
				row[14] = sum([y for (x, y) in a if x in ["PRP", "PRP$", "WP", "WP$"]])/(count*1.0) #pronoun
				row[15] = sum([y for (x, y) in a if x in ["UH"]])/(count*1.0) #interjection

			# if wordcount != 0:
			# 	row[16] = len([y for y in textlist if y in childW])/(wordcount*1.0)
			# 	row[17] = len([y for y in textlist if y in historyW])/(wordcount*1.0)
			# 	row[18] = len([y for y in textlist if y in religionW])/(wordcount*1.0)
			# 	row[19] = len([y for y in textlist if y in scienceW])/(wordcount*1.0)

			row[-1] = j # This number assigns class
			row[-2] = re.search('[0-9]+\.txt', file).group() # Extracts file name (Ex: "123.txt")
			matrix += [row]
			i += 1
			print(path[-20:] + " on iteration " + str(i))
		j += 1
	return matrix
# Number of unique words/Number of words
# Number of words/Number of periods
# Average wordlength
# Proportion of Document that is numbers
# Capital letter to lower case ratio (only first letter of word)
# Number of quotation marks
# Number of exclamation points, question marks
# Part of Speech percentages
# What percent of those words are in document x4
# TF of words occuring ("I", "")

if __name__ == "__main__":
	matrix = makePowerMatrix()
	with open("customMatrix.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(matrix)
