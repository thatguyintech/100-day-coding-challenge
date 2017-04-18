##############
## Solution ##
##############

def alienAlphabet(orderedWords):
    # edge cases
    if len(orderedWords) <= 0:
        return ''
    if len(orderedWords) == 1:
        return removeDups(orderedWords[0])

    # linearization of a DAG
    graph = createDependencyGraph(orderedWords)
    alphabet = topSort(graph)

    return "".join(alphabet)

#############
## Helpers ##
#############

def createDependencyGraph(orderedWords):
    graph = {}
    for i, word in enumerate(orderedWords[:-1]):
        nextWord = orderedWords[i+1]
        shorter = min(len(word), len(nextWord))
        for j in xrange(shorter):
            letter = word[j]
            otherLetter = nextWord[j]

            if letter not in graph:
                graph[letter] = []
            if otherLetter not in graph:
                graph[otherLetter] = []

            if letter != otherLetter:
                graph[letter].append(otherLetter)
                break

    return graph

# graph is represented as key:value pair
# key = node
# value = [list, of, connected, nodes]
#
# the graph is also given to be a DAG so all the connected
# nodes are from outgoing edges
#
# this function returns the resulting linearization in a list
def topSort(graph):
    sources = getSources(graph)
    visited = set()
    postOrderStack = []

    def dfs(start, graph, visitedSet, postOrderStack):
        visitedSet.add(start)

        # recurse
        for child in graph[start]:
            if child not in visitedSet:
                dfs(child, graph, visitedSet, postOrderStack)

        # done exploring your children, add yourself to the postorder
        postOrderStack.append(start)        

    # run dfs from all source nodes
    for node in sources:
        dfs(node, graph, visited, postOrderStack)

    return postOrderStack[::-1]

def getSources(graph):
    # initialize all nodes to 0
    nodes = {k:0 for k in graph.keys()}

    # mark non-source nodes as 1
    for key in graph.keys():
        for node in graph[key]:
            nodes[node] = 1

    # only the nodes marked `0` are sources
    sourcePairs = filter(lambda pair: pair[1] == 0, nodes.items())
    return [x for x,y in sourcePairs]

def removeDups(s):
    # python's `set` implementation is basically a dictionary with
    # dummy values, that's why adding elements and finding elements
    # are constant time : http://markmail.org/message/ktzomp4uwrmnzao6
    seen = set()
    ret = list()
    for char in s:
        if char not in seen:
            ret.append(char)
            seen.add(char)
    return "".join(ret)

###########
## Tests ##
###########

def testGetSources():
    graph = {'b':['a','d'], 'a':['c'], 'c':[], 'd':['a']}
    assert(getSources(graph) == ['b'])

def testTopSort():
    graph = {'b':['a','d'], 'a':['c'], 'c':[], 'd':['a']}
    assert(topSort(graph) == ['b','d','a','c'])

def testRemoveDups():
    assert(removeDups('') == '')
    assert(removeDups('aaa') == 'a')
    assert(removeDups('aba') == 'ab')
    assert(removeDups('aab') == 'ab')
    assert(removeDups('baa') == 'ba')
    assert(removeDups('a') == 'a')
    assert(removeDups('asdfasdfasdfasdf') == 'asdf')

def testAlienAlphabet():
    assert(alienAlphabet([]) == '')
    assert(alienAlphabet(['baa']) == 'ba') # might be wrong assumption here
    assert(alienAlphabet(['baa', 'baa']) == 'ba') # might be the wrong assumption here
    assert(alienAlphabet(['abcd', 'baa', 'c', 'd', 'e']) == 'abcde')
    assert(alienAlphabet(['baa', 'abcd', 'abca', 'cab', 'cad']) == 'bdac')

def tests():
    testGetSources()
    testTopSort()
    testRemoveDups()
    testAlienAlphabet()

tests()
