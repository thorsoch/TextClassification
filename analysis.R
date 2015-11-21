library(data.table)
a = fread("totals.csv")
b = as.data.frame(a)
words = as.character(b[1, ])
counts = as.numeric(b[2, ])

# Returns the number of words
# that occur more than CUTOFF

margincount = function(cutoff) {
  return(sum(counts > cutoff))
}


# Choose the left hand cutoff 
# margins then call the function above.

margins = 360:5000
margincounts = sapply(margins, margincount)
plot(margins, margincounts)
abline(v = 500)
abline(v = 10)
abline(h = 10000)

# Find the alpha for 10000 words.

cutoff_locs = head(which(margincounts <= 10000))
alphacutoffs = margins[cutoff_locs]
margincounts[cutoff_locs]


# Extract all the words that pass
# our conditions above. 

indicies = which(counts > 500)
selectedwords = words[indicies]

# Load up word matrix.

wordmatrix = fread("matrix.csv")
wordmatrix = as.data.frame(wordmatrix)

# Fix up the naming of the columns.

names(wordmatrix) = as.character(wordmatrix[1, ])
wordmatrix = wordmatrix[-1, ]
wordmatrix[1:10, 1:10]
head(wordmatrix$aa)

# Double check the sum of columns equals counts variable.

testcounts = apply(wordmatrix[, 1:3], 2, function (x) sum(as.numeric(x)))
testcounts

