Question of the day: https://leetcode.com/problems/path-sum/#/description

"Given a binary tree and a sum, determine if the tree
has a root-to-leaf path such that adding up all the
values along the path equals the given sum."

## Ideas ##

The tree isn't organized, i.e. it's not a binary search
tree. That means I'll have to do some kind of extensive
searching, and since I want a path, DFS should work.

In the case of DFS, I can implement it recursively such that
the base case is if I'm at a leaf node, check if the sum
I'm searching for is equal to the value of this node.
Otherwise, recurse on the node's children and subtract
the node's value from the sum.

This solution would be O(n) runtime and O(1) space. Can't
get any better asymptotically since we need to search
all paths in order to be sure we didn't miss a possible
solution.

## Code ##

[Python](./pathsum.py)

## Follow up ##

TODO: (suggestions from @jabagawee) for a challenge,
try this with BFS as well. or change the problem description
from "root-to-leaf path" to "any path starting from the root"
or "any path traveling down the tree" or "any path at all"

or generalize to any n-ary tree. or any graph. then start
doing runtime and space analyses on each of these solutions.