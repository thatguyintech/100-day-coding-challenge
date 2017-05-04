def differByOne(word, anotherWord):
    return sum(c1 != c2 for c1, c2 in zip(word, anotherWord)) == 1

def tuplelizeDuplicates(inputArray):
    dups = {elem:0 for elem in inputArray}
    outputTuples = []
    for elem in inputArray:
        if elem in dups:
            outputTuples.append((elem, dups[elem]))
            dups[elem] += 1
    return outputTuples

def createGraph(inputTuples):
    g = {elem:set() for elem in inputTuples}

    size = len(inputTuples)

    for i in xrange(size):
        for j in xrange(size):

            if i == j:
                continue

            v1 = inputTuples[i]
            v2 = inputTuples[j]

            if differByOne(v1[0], v2[0]):
                g[v1].add(v2)
                g[v2].add(v1)
    return g

def derp(graph, startTuple, visited=set()):
    # do dfs
    for vertexTuple in graph[startTuple]:
        if vertexTuple not in visited:
            visited.add(vertexTuple)
            if derp(graph, vertexTuple, visited):
                return True

    return False

def hamiltonianPath(graph):
    if len(graph) == 0:
        return True

    visited = set()
    for node in graph:
        if node not in visited and derp(graph, node, visited):
            return True
        visited.add(node)

    return False

def testDifferByOne():
    assert not differByOne("", "")
    assert not differByOne("a", "a")
    assert not differByOne("aaa", "aaa")
    assert not differByOne("abcdeff", "abcedff")
    assert differByOne("a", "b")
    assert differByOne("abc", "abb")
    assert differByOne("abc", "bbc")
    assert differByOne("abcdefg", "abcdefz")

def testTuplelizeDuplicates():
    assert tuplelizeDuplicates(["qq", "qq", "qq"]) == [("qq", 0), ("qq", 1), ("qq", 2)]

def testCreateGraph():
    assert createGraph(tuplelizeDuplicates(["aba", "bbb", "bab"])) == {("aba", 0): set([]), ("bbb", 0): set([("bab", 0)]), ("bab", 0): set([("bbb", 0)])}
    assert createGraph(tuplelizeDuplicates(["qq", "qq", "qq"])) == {('qq', 1): set([]), ('qq', 0): set([]), ('qq', 2): set([])}
    assert createGraph(tuplelizeDuplicates(["ab", "ad", "ef", "eg"])) == {('ab', 0): set([('ad', 0)]), ('ef', 0): set([('eg', 0)]), ('ad', 0): set([('ab', 0)]), ('eg', 0): set([('ef', 0)])}

def testHamiltonianPath():
    assert hamiltonianPath(createGraph([]))
    assert not hamiltonianPath(createGraph(["aba", "bbb", "bab"]))
    assert hamiltonianPath(createGraph(["ab", "bb", "aac"]))
    assert not hamiltonianPath(createGraph(["qq", "qq", "qq"]))
    assert hamiltonianPath(createGraph(["aaa", "aba", "aaa", "aba", "aaa"]))
    assert not hamiltonianPath(createGraph(["ab", "ad", "ef", "eg"]))
    assert hamiltonianPath(createGraph(["abc", "abx", "axx", "abx", "abc"]))
    assert hamiltonianPath(createGraph(["f", "g", "a", "h"]))

def main():
    testDifferByOne()
    testTuplelizeDuplicates()
    testCreateGraph()
    testHamiltonianPath()

if __name__ == "__main__":
    main()