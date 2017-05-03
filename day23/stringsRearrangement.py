from itertools import permutations

def stringsRearrangement(inputArray):
    for perm in permutations(inputArray):
        if neighborsDifferByOne(perm):
            return True 
    return False

def neighborsDifferByOne(inputArray):
    if len(inputArray) <= 1:
        return True
    return differByOne(inputArray[0], inputArray[1]) and neighborsDifferByOne(inputArray[2:])

def differByOne(word, anotherWord):
    if len(word) != len(anotherWord):
        return False

    differencesCount = 0
    for i in xrange(len(word)):
        if word[i] != anotherWord[j]:
            differencesCount += 1

    if differencesCount == 0 or differencesCount >= 2:
        return False

    return True


def main():
    assert stringsRearrangement([], True)
    assert stringsRearrangement(["aba", "bbb", "bab"], False)
    assert stringsRearrangement(["ab", "bb", "aa"], True)
    assert stringsRearrangement(["qq", "qq", "qq"], False)
    assert stringsRearrangement(["aaa", "aba", "aaa", "aba", "aaa"], True)
    assert stringsRearrangement(["ab", "ad", "ef", "eg"], False)
    assert stringsRearrangement(["abc", "abx", "axx", "abx", "abc"], True)
    assert stringsRearrangement(["f", "g", "a", "h"], True)
