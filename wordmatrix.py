import parse
import csv

with open("totals.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	totals = list(list(rec) for rec in csv.reader(f, delimiter=','))

finalmat = parse.makeMatrix(totals[0])

with open("matrix.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)