
seq1 = list(range(10))  # Create list of numbers from 0 to 9
seq2 = list(range(0,10,2))  # Create list of numbers from 0 to 9 with step 2
res = [] # Create empty list in global visibility area

def intersection(seq1, seq2):
    res = [] # Start with empty list as local variable
    for x in seq1: # Scan seq1
        if x in seq2: # Common item?
            res.append(x) # Add to end
    return res

print(intersection(seq1, seq2))
print("List:", res)
