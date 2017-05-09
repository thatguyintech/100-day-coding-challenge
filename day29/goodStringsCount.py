from math import factorial

def nChooseR(n, r):
    return factorial(n) / (factorial(n-r) * factorial(r))

def goodStringsCount(n):
    return nChooseR(26, n) * (2**n - n - 1)

def testGoodStringsCount():
    assert goodStringsCount(1) == 0
    assert goodStringsCount(2) == 325
    assert goodStringsCount(3) == 10400

def main():
    testGoodStringsCount()

if __name__ == "__main__":
    main()
