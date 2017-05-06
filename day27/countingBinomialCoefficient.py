def countingBinomialCoefficient(num, prime):

    # edge cases
    if num <= 2:
        return 0
    
    prevRow = [1, 1]
    
    count = 0
    
    for rowNum in xrange(2, num):
        row = [1] * (rowNum+1)
        
        for i in xrange(len(prevRow)-1):
            row[i+1] = prevRow[i] + prevRow[i+1]
            if row[i+1] % prime == 0:
                count += 1
            
        prevRow = row

    return count
