import parse
import csv

print("Opening totals.csv")

with open("totals.csv", 'rU') as f:  #opens PW file
	reader = csv.reader(f)
	totals = list(list(rec) for rec in csv.reader(f, delimiter=','))

print("Starting parse.makeMatrix()")

finalmat = parse.makeMatrix(totals[0])

print("Writing out matrix.csv")

with open("matrix.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(finalmat)

print("Script complete.")