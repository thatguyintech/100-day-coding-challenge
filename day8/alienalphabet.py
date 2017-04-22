##############
## Solution ##
##############

def alienAlphabet(orderedWords):
    # edge cases
    if len(orderedWords) <= 0:
        return ""
    if len(orderedWords) == 1:
        return "".join(set(orderedWords[0]))

    # linearization of a DAG
    graph = createDependencyGraph(orderedWords)
    alphabet = topologicalSort(graph)

    return "".join(alphabet)

#############
## Helpers ##
#############

def createDependencyGraph(orderedWords):
    # prepoulate graph with all letters
    graph = {letter: [] for word in orderedWords for letter in word}

    # add dependencies
    for word, nextWord in zip(orderedWords, orderedWords[1:]):
        for letter, otherLetter in zip(word, nextWord):
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
def topologicalSort(graph):
    visited = set()
    postOrderStack = []

    def dfs(start):
        visited.add(start)

        # recurse
        for child in graph[start]:
            if child not in visited:
                dfs(child)

        # done exploring your children, add yourself to the postorder
        postOrderStack.append(start)        

    # run dfs from all source nodes
    sources = getSources(graph)
    for node in sources:
        dfs(node)

    # reversed returns an iterator
    return reversed(postOrderStack)

# Source nodes are ones that don't have any incoming edges
def getSources(graph):
    nonSourceNodes = set()
    for nodeList in graph.values():
        for node in nodeList:
            nonSourceNodes.add(node)
    return set(graph.keys()) - nonSourceNodes

###########
## Tests ##
###########

def testGetSources():
    graph = {'b':['a','d'], 'a':['c'], 'c':[], 'd':['a']}
    assert getSources(graph) == set(['b'])

def testTopologicalSort():
    graph = {'b':['a','d'], 'a':['c'], 'c':[], 'd':['a']}
    topologicalSortResult = topologicalSort(graph)
    assert topologicalSortResult.next() == 'b'
    assert topologicalSortResult.next() == 'd'
    assert topologicalSortResult.next() == 'a'
    assert topologicalSortResult.next() == 'c'

def testAlienAlphabet():
    assert alienAlphabet([]) == ''
    assert set(alienAlphabet(['baa'])) == set('ba') # might be wrong assumption here
    assert alienAlphabet(['baa', 'baa']) == 'ba' # might be the wrong assumption here
    assert alienAlphabet(['abcd', 'baa', 'c', 'd', 'e']) == 'abcde'
    assert alienAlphabet(['baa', 'abcd', 'abca', 'cab', 'cad']) == 'bdac'

def tests():
    testGetSources()
    testTopologicalSort()
    testAlienAlphabet()

def main():
    tests()

if __name__ == '__main__':
    main()

