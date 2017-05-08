class BinomialCoefficient(object):
    def __init__(self):
        self.coefficients = {}
        self.notDivisible = {}

    # returns the binomial expansion coefficient for TOTAL choose SUBGROUP
    # aka C(total, subgroup)
    def getBinomialCoefficient(self, total, subgroup):
        if (total, subgroup) in self.coefficients:
            return self.coefficients[(total, subgroup)]

        if total == subgroup or subgroup == 0:
            self.coefficients[(total, subgroup)] = 1
            return 1

        return self.getBinomialCoefficient(total-1, subgroup) + self.getBinomialCoefficient(total-1, subgroup-1)

    # returns the number of coefficients in Pascal's triangle up to
    # the NUMth row of the triangle that are not divisible by PRIME
    def binomialCoefficientsNotDivisibleByPrime(self, num, prime):
        if num == 0:
            self.notDivisible[prime] = {0: 1}
            return 1

        if prime in self.notDivisible and num in self.notDivisible[prime]:
            return self.notDivisible[prime][num]

        notDivisibleThisRow = len([i for i in xrange(num+1) if self.getBinomialCoefficient(num, i) % prime != 0])

        self.notDivisible[prime][num] = self.binomialCoefficientsNotDivisibleByPrime(num-1, prime) + notDivisibleThisRow
        return self.notDivisible[prime][num]

def testGetBinomialCoefficient(binomialCalculator):
    b = binomialCalculator

    assert b.getBinomialCoefficient(0, 0) == 1

    assert b.getBinomialCoefficient(1, 0) == 1
    assert b.getBinomialCoefficient(1, 1) == 1

    assert b.getBinomialCoefficient(2, 0) == 1
    assert b.getBinomialCoefficient(2, 1) == 2
    assert b.getBinomialCoefficient(2, 2) == 1

    assert b.getBinomialCoefficient(3, 0) == 1
    assert b.getBinomialCoefficient(3, 1) == 3
    assert b.getBinomialCoefficient(3, 2) == 3
    assert b.getBinomialCoefficient(3, 3) == 1

    assert b.getBinomialCoefficient(4, 0) == 1
    assert b.getBinomialCoefficient(4, 1) == 4
    assert b.getBinomialCoefficient(4, 2) == 6
    assert b.getBinomialCoefficient(4, 3) == 4
    assert b.getBinomialCoefficient(4, 4) == 1

    assert b.getBinomialCoefficient(5, 0) == 1
    assert b.getBinomialCoefficient(5, 1) == 5
    assert b.getBinomialCoefficient(5, 2) == 10
    assert b.getBinomialCoefficient(5, 3) == 10
    assert b.getBinomialCoefficient(5, 4) == 5
    assert b.getBinomialCoefficient(5, 5) == 1

def testCountBinomialCoefficientsNotDivisibleByPrime(binomialCalculator):
    b = binomialCalculator

    # prime = 2
    assert b.binomialCoefficientsNotDivisibleByPrime(0, 2) == 1
    assert b.binomialCoefficientsNotDivisibleByPrime(1, 2) == 3
    assert b.binomialCoefficientsNotDivisibleByPrime(2, 2) == 5
    assert b.binomialCoefficientsNotDivisibleByPrime(3, 2) == 9
    assert b.binomialCoefficientsNotDivisibleByPrime(4, 2) == 11
    assert b.binomialCoefficientsNotDivisibleByPrime(5, 2) == 15

    # prime = 5
    assert b.binomialCoefficientsNotDivisibleByPrime(0, 5) == 1
    assert b.binomialCoefficientsNotDivisibleByPrime(1, 5) == 3
    assert b.binomialCoefficientsNotDivisibleByPrime(2, 5) == 6
    assert b.binomialCoefficientsNotDivisibleByPrime(3, 5) == 10
    assert b.binomialCoefficientsNotDivisibleByPrime(4, 5) == 15
    assert b.binomialCoefficientsNotDivisibleByPrime(5, 5) == 17
    assert b.binomialCoefficientsNotDivisibleByPrime(6, 5) == 21

    # prime = 7
    assert b.binomialCoefficientsNotDivisibleByPrime(5, 7) == 21 

    # BIG DATA
    assert b.binomialCoefficientsNotDivisibleByPrime(999999999, 7)  == 2129970655314432
    assert b.binomialCoefficientsNotDivisibleByPrime(879799878, 17) == 6026990181372288
    assert b.binomialCoefficientsNotDivisibleByPrime(879799878, 19) == 8480245105257600

def main():
    b = BinomialCoefficient()
    testGetBinomialCoefficient(b)
    testCountBinomialCoefficientsNotDivisibleByPrime(b)

if __name__ == "__main__":
    main()
