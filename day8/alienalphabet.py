class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linearize(DAG):
    sourceNodes = sources(DAG)
    visited = set()

    def dfs(node, visited, postOrderStack):
        if node.next == None:
            # sink node
            postOrderStack.append(node)
        dfs(node.next)

    for node in sourceNodes:
        # run DFS to get post order numbers
        # don't need the actual numbers, just put the node into a stack
        # when you're about to label the post number

    return

def sources(graph):
    s = set()

    for node in graph:
        for child in graph[node]:
            s.add(child)

    return set(graph.keys()) - s

def tests():
    graph = {'A':['D'], 'B':['D'], 'C':['D'], 'D':['E','F'],'F':['G'],'G':['H'],'E':['H'],'H':['I'],'I':['J']}
    assert(sources(graph) == set(['A', 'B', 'C']))

tests()
