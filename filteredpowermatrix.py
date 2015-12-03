import powerparse
import csv
import ast

print("Opening bigramspredictors.csv")

with open("bigramspredictors.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	bigrams = list(list(rec) for rec in csv.reader(f, delimiter=','))

print("Starting powerparse.makeMatrix()")
a = [item for sublist in bigrams for item in sublist]
a = list(map(ast.literal_eval, a))
finalmat = powerparse.makeMatrix(a)

print("Writing out filterpowermatrix.csv")

with open("filterpowermatrix.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)

# print("Making proportion matrix")

# z = 0
# for row in finalmat:
# 	if z == 0:
# 		z += 1
# 		continue
# 	rowpart = [int(x) for x in row[0:len(row)-2]]
# 	totalcount = sum([int(x) for x in rowpart])
# 	i=0
# 	if totalcount != 0:
# 		for val in rowpart:
# 			row[i] = val/(totalcount*1.0)
# 			i += 1

# with open("powermatrixprop.csv", "wb") as f:
# 		writer = csv.writer(f)
# 		writer.writerows(finalmat)

print("Script complete.")