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

margins = 10:5000
margincounts = sapply(margins, margincount)
plot(margins, margincounts)
abline(v = 500)
abline(v = 10)


# Extract all the words that pass
# our conditions above. 

indicies = which(counts > 500)
selectedwords = words[indicies]

