def countingBinomialCoefficient(num, prime):
    prevRow = []
    count = 0
   
    for rowNum in xrange(num+1):
        row = [1] * (rowNum+1)
       
        for i in xrange(len(prevRow)-1):
            row[i+1] = prevRow[i] + prevRow[i+1]

        for j in xrange(len(row)):
            if row[j] % prime != 0:
                count += 1
        prevRow = row

    return count

def testCountingBinomialCoefficient():
    # prime = 2
    assert countingBinomialCoefficient(0, 2) == 1
    assert countingBinomialCoefficient(1, 2) == 3
    assert countingBinomialCoefficient(2, 2) == 5
    assert countingBinomialCoefficient(3, 2) == 9
    assert countingBinomialCoefficient(4, 2) == 11
    assert countingBinomialCoefficient(5, 2) == 15

    # prime = 5
    assert countingBinomialCoefficient(0, 5) == 1
    assert countingBinomialCoefficient(1, 5) == 3
    assert countingBinomialCoefficient(2, 5) == 6
    assert countingBinomialCoefficient(3, 5) == 10
    assert countingBinomialCoefficient(4, 5) == 15
    assert countingBinomialCoefficient(5, 5) == 17
    assert countingBinomialCoefficient(6, 5) == 21

    # prime = 7
    assert countingBinomialCoefficient(5, 7) == 21 

    # BIG DATA (these don't finish running with the brute force implementation)
    # assert countingBinomialCoefficient(999999999, 7) == 2129970655314432
    # assert countingBinomialCoefficient(879799878, 17) == 6026990181372288
    # assert countingBinomialCoefficient(879799878, 19) == 8480245105257600

def main():
    testCountingBinomialCoefficient()

if __name__ == "__main__":
    main()
