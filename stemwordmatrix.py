import parse
import csv

print("Opening totalsstem.csv")

with open("totalsstem.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	totals = list(list(rec) for rec in csv.reader(f, delimiter=','))

print("Starting parse.makeMatrix()")

finalmat = parse.makeMatrix(totals[0])

print("Writing out matrix.csv")

with open("stemmatrix.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)

print("Making proportion matrix")

z = 0
for row in finalmat:
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

with open("stemmatrixprop.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)

print("Script complete.")