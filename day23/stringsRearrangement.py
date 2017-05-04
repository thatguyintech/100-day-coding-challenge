from itertools import permutations

def stringsRearrangement(inputArray):
    for perm in permutations(inputArray):
        if neighborsDifferByOne(perm):
            return True 
    return False

def neighborsDifferByOne(inputArray):
    if len(inputArray) <= 1:
        return True
    return differByOne(inputArray[0], inputArray[1]) and neighborsDifferByOne(inputArray[1:])

def differByOne(word, anotherWord):
    differencesCount = 0
    for i in xrange(len(word)):
        if word[i] != anotherWord[i]:
            differencesCount += 1
        if differencesCount > 1:
            return False

    return differencesCount == 1

def testDifferByOne():
    assert not differByOne("", "")
    assert not differByOne("a", "a")
    assert not differByOne("aaa", "aaa")
    assert not differByOne("abcdeff", "abcedff")
    assert differByOne("a", "b")
    assert differByOne("abc", "abb")
    assert differByOne("abc", "bbc")
    assert differByOne("abcdefg", "abcdefz")

def testNeighborsDifferByOne():
    assert neighborsDifferByOne([])
    assert neighborsDifferByOne([""])
    assert neighborsDifferByOne(["a", "b"])
    assert neighborsDifferByOne(["a", "b", "c"])
    assert neighborsDifferByOne(["ab", "bb"])
    assert neighborsDifferByOne(["ab", "bb", "bc"])
    assert neighborsDifferByOne(["ab", "bb", "bc", "ba"])
    assert neighborsDifferByOne(["abc", "bbc", "bac", "bad"])
    assert not neighborsDifferByOne(["a", "a"])

def testStringsRearrangement():
    assert stringsRearrangement([])
    assert not stringsRearrangement(["aba", "bbb", "bab"])
    assert stringsRearrangement(["ab", "bb", "aac"])
    assert not stringsRearrangement(["qq", "qq", "qq"])
    assert stringsRearrangement(["aaa", "aba", "aaa", "aba", "aaa"])
    assert not stringsRearrangement(["ab", "ad", "ef", "eg"])
    assert stringsRearrangement(["abc", "abx", "axx", "abx", "abc"])
    assert stringsRearrangement(["f", "g", "a", "h"])

def main():
    testDifferByOne()
    testNeighborsDifferByOne()
    testStringsRearrangement()

if __name__ == "__main__":
    main()
