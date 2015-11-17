import os
import glob

# Prepare the path for all .txt files. 

base_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(base_path, "Training", "*", "*.txt")

# Create category paths seperately, in case we need them. 

child_path = os.path.join(base_path, "Training", "Child(0)", "*.txt")
history_path = os.path.join(base_path, "Training", "History(1)", "*.txt")
religion_path = os.path.join(base_path, "Training", "Religion(2)", "*.txt")
science_path = os.path.join(base_path, "Training", "Science(3)", "*.txt")

# Function that opens the file at PATH, 
# parses out words, and returns them as
# lower case and splitted.

def parse(path):
	file = open(path)
	text = file.read()
	words = text.lower().split()
	return words

i = 0
for file in glob.glob(txt_path):
	i += 1
print(i)

i = 0
for file in glob.glob(child_path):
	i += 1
for file in glob.glob(history_path):
	i += 1
for file in glob.glob(religion_path):
	i += 1
for file in glob.glob(science_path):
	i += 1
print(i)
