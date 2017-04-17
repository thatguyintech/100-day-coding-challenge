Question of the day:

Implement BFS and DFS, both iteratively and recurively if possible.
Use them to find a node with a value of `val` in a binary tree, if
the node exists. If not, just return nothing.

## Ideas

BFS can be done iteratively by queuing up children nodes and exploring
them in the order they are dequeued. The search cannot be done
recursively due to the nature of the queue action.

Runtime `O(nodes)` - visit each node at least once  
Space `O(nodes)` - at most store every node in the biggest layer

DFS can be done recursively by just calling the function again on a
node's children, until you find what you're looking for. To do
iteratively, just use a stack to process the nodes to explore.

Runtime `O(nodes)` - visit each node at least once
Space `O(height)` - at most we're storing # nodes proportional to
                    the height of one path down the tree from the root

## Code

[Python](./bfsdfs.py)

